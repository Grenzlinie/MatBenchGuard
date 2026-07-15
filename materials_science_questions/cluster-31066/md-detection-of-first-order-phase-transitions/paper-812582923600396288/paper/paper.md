# Unraveling liquid polymorphism in silicon driven out-of-equilibrium

Cite as: J. Chem. Phys. 153, 054502 (2020); https://doi.org/10.1063/5.0015417
Submitted: 27 May 2020 . Accepted: 15 July 2020 . Published Online: 03 August 2020

Caroline Desgranges, and Jerome Delhommelle

![](./images/812582923600396288_1.jpg) ![](./images/812582923600396288_2.jpg) ![](./images/812582923600396288_3.jpg)

## ARTICLES YOU MAY BE INTERESTED IN

Simulations of activities, solubilities, transport properties, and nucleation rates for aqueous electrolyte solutions
The Journal of Chemical Physics 153, 010903 (2020); https://doi.org/10.1063/5.0012102

How to "measure" a structural relaxation time that is too long to be measured?
The Journal of Chemical Physics 153, 044501 (2020); https://doi.org/10.1063/5.0015227

A protocol for preparing explicitly solvated systems for stable molecular dynamics simulations
The Journal of Chemical Physics 153, 054123 (2020); https://doi.org/10.1063/5.0013849

![](./images/812582923600396288_4.jpg)

J. Chem. Phys. 153, 054502 (2020); https://doi.org/10.1063/5.0015417
© 2020 Author(s).

153, 054502

# Unraveling liquid polymorphism in silicon driven out-of-equilibrium

Cite as: J. Chem. Phys. 153, 054502 (2020); doi: 10.1063/5.0015417
Submitted: 27 May 2020 • Accepted: 15 July 2020 •
Published Online: 3 August 2020

![](./images/812582923600396288_5.jpg) ![](./images/812582923600396288_6.jpg) ![](./images/812582923600396288_7.jpg)

Caroline Desgranges and Jerome Delhommelle⁽ᵃ⁾

## AFFILIATIONS

Department of Chemistry, New York University, New York, New York 10003, USA and Department of Chemistry,
University of North Dakota, Grand Forks, North Dakota 58202, USA

⁽ᵃ⁾Author to whom correspondence should be addressed: jerome.delhommelle@und.edu

## ABSTRACT

Using nonequilibrium molecular dynamics simulations, we study the properties of supercooled liquids of Si under shear at $T = 1060$ K over a range of densities encompassing the low-density liquid (LDL) and high-density liquid (HDL) forms. This enables us to generate nonequilibrium steady-states of the LDL and HDL polymorphs that remain stabilized in their liquid forms for as long as the shear is applied. This is unlike the LDL and HDL forms at rest, which are metastable under those conditions and, when at rest, rapidly undergo a transition toward the crystal, i.e., the thermodynamically stable equilibrium phase. In particular, through a detailed analysis of the structural and energetic features of the liquids under shear, we identify the range of densities, as well as the range of shear rates, which give rise to the two forms. We also show how the competition between shear and tetrahedral order impacts the two-body entropy in steady-states of Si under shear. These results open the door to new ways of utilizing shear to stabilize forms that are metastable at rest and can exhibit unique properties, since, for instance, experiments on Si have shown that HDL is metallic with no bandgap, while LDL is semimetallic with a pseudogap.

Published under license by AIP Publishing. https://doi.org/10.1063/5.0015417

## I. INTRODUCTION

Recent experimental and computational studies have revealed that the liquid state can also exhibit the phenomenon of polymorphism.¹⁻⁷ Similarly to the solid state that has been known, for a long time, to exhibit different crystal structures or polymorphs, the liquid state can also exhibit different liquid polymorphs with distinct densities, structures, and entropies. In particular, different liquid forms have been shown to exist in atomic systems, including phosphorus,⁸ carbon,⁹,¹⁰ silicon,¹¹⁻¹⁴ in molecular fluids like water,¹⁵⁻²⁷ triphenyl phosphite,²⁸⁻³⁰ alcohols,³¹,³² and in aqueous organic solutions.³³ In the case of silicon, the presence of two liquids below the melting point of Si and the existence of a first order transition between the two have been established by computer simulations¹¹,³⁴,³⁵ using a classical force field, known as the Stillinger–Weber (SW) potential.³⁶ These two liquid forms, referred to as the low-density liquid (LDL) form and the high-density liquid (HDL) form, differ in density, structure, and transport properties, such as diffusivity and viscosity. For instance, the density is found to be greater by 5% in HDL than in LDL, the coordination number also decreases from 4.9 (HDL) to 4.24 (LDL), and LDL is a network liquid with a high amount of tetrahedral order.¹¹ Diffusivity is roughly two orders of magnitude smaller in LDL than in HDL.¹¹ Similarly, LDL is much more viscous than HDL. Equilibrium molecular dynamics simulations³⁷ have reported Green–Kubo calculations for the viscosity that showed, over the 1000 K–1100 K temperature interval, dramatically greater viscosities for LDL. An important characteristic of LDL, and of the LDL–HDL transition, is that these have only been observed below the melting point, where the Si crystal is the thermodynamically stable phase and the two liquid forms LDL and HDL are metastable.³⁸ LDL is indeed often thought as a precursor for the formation of amorphous Si at high supercooling and to crystal nucleation at low supercooling.³⁴,³⁵,³⁹ This metastability was leveraged to observe in the transient regime the two liquid forms LDL and HDL in a pioneering experiment that subjected a crystal of Si to ultrashort optical pulses of femtosecond duration.¹⁴ This triggered the melting of the crystal in LDL that rearranged then into HDL. These structural changes were also accompanied

by changes in the electronic properties, since LDL is semimetallic with a pseudogap, while HDL is metallic with no bandgap. These observations pave the way for a control of liquid polymorphism via the use of an external field. Moreover, while the experimental observations were made on transient states, and thus on a very short timescale, a suitable choice of external perturbations could allow for the observation of liquid polymorphs in the steady-state, i.e., for as long as the external field is switched on. In particular, shear is often a very useful tool to probe nonequilibrium phase transitions, including the solid-liquid transition $^{40-42}$ and the liquid-liquid transition in a model system for methanol, $^{32}$ and more generally, the nonequilibrium response of glasses $^{43}$ and supercooled liquids. $^{44,45}$

The aim of this study is to address the following questions: (i) can nonequilibrium steady-states of the LDL and HDL forms be obtained by subjecting supercooled systems of Si to shear? and (ii) how does the competition between shear and tetrahedral ordering impact the structure, rheology, and entropy of Si under shear? For this purpose, we use nonequilibrium molecular dynamics (NEMD) simulation to study the response of supercooled Si over a wide range of shear rates and densities. The model used for Si is the classical SW model. While this force field does not allow for the calculation of electronic properties, the SW model provides a solid basis to analyze the nonequilibrium response of Si under shear since the LDL and HDL forms have been extensively characterized at rest and the model provides an accurate picture for the decrease in tetrahedral ordering with increasing density. $^{11,34,35}$ Building on our previous work using the SLLOD algorithm, $^{32,41,45-47}$ we obtain liquid systems of Si that are driven out-of-equilibrium by the applied shear and remain in a steady-state for as long as shear is applied. Through a series of analyses of the variation of the structural, energetic, and rheological properties of silicon under shear, we elucidate the conditions (density and applied shear rate) for which LDL and HDL are obtained in driven Si. We also unravel the interplay between tetrahedral order and the shear-induced structural changes that take place in silicon under shear and characterize the nonequilibrium two-body entropy in steady-states of LDL and HDL under shear.

This paper is organized as follows: In Sec. II, we present the simulation method, model, structural, and energetic analyses to characterize the properties of supercooled systems of Si under shear. We then present the simulation results obtained at $T = 1060$ K over a range of densities extending from $2.28$ g/cm³ to $2.52$ g/cm³ and compare the properties of supercooled liquids of Si under shear to the equilibrium data for the LDL and HDL polymorphs. In particular, we identify that the features characterizing the LDL and HDL at rest are found in steady-state liquids of Si under shear, provided that the applied shear rate remains sufficiently low. We also discuss how the competition between shear and tetrahedral order impacts the two-body entropy in steady-states of Si under shear, before drawing the main conclusions from this work in Sec. IV.

## II. SIMULATION METHODS

We use nonequilibrium molecular dynamics (NEMD) $^{48-51}$ to study the response of liquid silicon undergoing shear flow. In this work, we carry out simulations using an in-house code in the isothermal ensemble (NVT) with the number of silicon atoms set to $N = 512$, a temperature of $T = 1060$ K, for which prior work has shown that there is a liquid-liquid transition, $^{11,34}$ and for seven values of the volume $V$ corresponding to densities ranging from $2.28$ g/cm³ to $2.52$ g/cm³, with a $0.04$ g/cm³ interval. To model the interactions between Si atoms, we use the well-established Stillinger-Weber (SW) potential. $^{36}$ As shown in previous work, $^{11,34,35}$ this model yields equilibrium pressures that are consistent with the results from $ab$ initio calculations. $^{52}$ It is defined as the sum of a two-body term and of a three-body term. The pairwise term $u_2$ is given by
$$
\begin{cases}
u_2(r_{ij}) = A\epsilon(B(r_{ij}/\sigma))^{-p}-(r_{ij}/\sigma)^{-q})\exp\left[\left((r_{ij}/\sigma-a)^{-1}\right]\right. & (r_{ij}/\sigma) < a, \\
u_2(r_{ij}) = 0 & (r_{ij}/\sigma) \geq a,
\end{cases} \tag{1}
$$
with the parameters $\epsilon = 50$ kcal/mol, $\sigma = 2.0951$ Å, $A = 7.04955627$, $B = 0.602224558$, $p = 4$, $q = 0$, and $a = 1.8$. The three-body term $u_3$ is written as
$$
u_3(\mathbf{r}_i, \mathbf{r}_j, \mathbf{r}_k) = \epsilon\left[h(r_{ij}, r_{ik}, \theta_{jik}) + h(r_{ji}, r_{jk}, \theta_{ijk}) + h(r_{ki}, r_{kj}, \theta_{ikj})\right], \tag{2}
$$
where the $h$ function is defined for $r < a$ as, e.g., in the case of $h(r_{ij}, r_{ik}, \theta_{jik})$,
$$
\begin{aligned}
h(r_{ij}, r_{ik}, \theta_{jik}) &= \lambda \exp\left[\nu(r_{ij}/\sigma - a)^{-1} + \nu(r_{ik}/\sigma - a)^{-1}\right] \\
&\quad \times \left(\cos\theta_{jik} + 1/3\right)^2,
\end{aligned} \tag{3}
$$
where $\theta_{jik}$ denotes the angle between vectors $\mathbf{r}_{ij}$ and $\mathbf{r}_{ik}$, subtended by vertex $i$, and where $\lambda = 21$ and $\nu = 1.2$.

We simulate a planar Couette flow in the $\mathbf{x}$ direction with a velocity gradient along the $\mathbf{y}$ direction using the SLLOD algorithm, together with the Lees-Edwards boundary conditions. $^{46}$ The equations of motion for an $N$-particle system subject to a steady external shear rate $\gamma$ are given by
$$
\begin{aligned}
\dot{\mathbf{q}}_i &= \frac{\mathbf{p}_i}{m} + \gamma y_i \mathbf{e}_x, \\
\dot{\mathbf{p}}_i &= \mathbf{F}_i - \gamma p_{y_i} \mathbf{e}_x - \alpha \mathbf{p}_i.
\end{aligned} \tag{4}
$$

In these equations, heat is dissipated via the use of a Gaussian thermostat, $^{53,54}$ which is the last term of the second line in Eq. (4). $\alpha$ is the thermostat multiplier and is defined as
$$
\alpha = -\frac{\sum_{i=1}^N \mathbf{p}_i.\mathbf{F}_i - \gamma \sum_{i=1}^N p_{x,i}.p_{y,i}}{\sum_{i=1}^N \mathbf{p}_i^2}. \tag{5}
$$

Here, the rate at which work done on the system by the external field $\gamma$ is compensated by the rate at which heat is removed from the system by the thermostat. This allows the system to reach a steady-state. $^{46}$ The choice of a Gaussian thermostat is not expected to impact the results, as the shear rates considered here are less than 1 (in reduced units). Previous work on atomic fluids has shown that profile-unbiased thermostats, $^{55,56}$ such as configurational thermostats, $^{57-61}$ provide a more physical basis for heat dissipation in liquids subjected to shear rates greater than 1 and allow for the onset of secondary flow profiles in strongly sheared liquid. $^{62}$

We integrate the equations of motion with a five-value Gear predictor-corrector algorithm and a time step of $1 \times 10^{-15}$ s. For each value of the shear rate $\gamma$, we start by running a first run of $2 \times 10^{6}$ time steps, or in other words, a trajectory of 2 ns, and check that the system has reached a steady-state. Then, we perform an additional production run of $2 \times 10^{6}$ time steps to compute time averages of various physical properties of the system, including the two-body energy $u_2$, the three-body energy $u_3$, the viscosity $\eta$, and the pressure $P$. In particular, the viscosity $\eta$ can be calculated as $^{63}$

$$
\eta = -\frac{\langle P_{xy} \rangle}{\gamma}. \tag{6}
$$

This method is very well suited to calculate transport properties in the steady-state, i.e., when a steady linear flow profile has developed across the fluid. $^{46}$ Other methods, such as the transient-time correlation function (TTCF) formalism, $^{45,47,64-66}$ apply when the response in the transient regime needs to be determined. Throughout this work, we use a system of reduced units for simulation parameters, such as the reduced shear rate $\gamma^*$, in which the unit of length is set to $\sigma$, the unit of energy to $\epsilon$, and the unit of mass to $m$, the atomic mass of Si.

Moreover, we use different order parameters to study the system. First, the global order parameter $Q_6$, introduced by Steinhardt *et al.*, $^{67}$ which measures the amount of crystalline order in a system,

$$
Q_6 = \left[ \frac{4\pi}{13} \sum_{m=-6}^{6} \left| \frac{\sum_i \sum_j Y_{6m}(\hat{\mathbf{r}}_{ij})}{\sum_i N_b(i)} \right|^2 \right]^{1/2}, \tag{7}
$$

where $\hat{\mathbf{r}}_{ij}$ is the unit vector joining two neighboring atoms $i$ and $j$ that are less than a distance of $4.1$ Å from each other (corresponding to the first minimum of the pair distribution function for the liquid), $Y_{6m}(\hat{\mathbf{r}}_{ij})$ is a spherical harmonics, and $N_b(i)$ is the number of neighbors for molecule $i$. $Q_6$ takes values greater than 0.3 for crystal phases and vanishes in the liquid. $^{68}$ We also use the order parameter $q_t$ that quantifies the average amount of tetrahedral order. $^{69,70}$ It is calculated as an average of the local $q_t(i)$ over all atoms $i$ in the system with

$$
q_t(i) = 1 - \frac{3}{8} \sum_{j=1}^{3} \sum_{k=j+1}^{4} \left( \cos \psi_{jk} + \frac{1}{3} \right)^2, \tag{8}
$$

where $j$ and $k$ are two atoms among the four nearest neighbors of atom $i$ and $\psi_{jk}$ is the angle formed by the line joining $i$ and $j$ and the line joining $i$ and $k$. Perfect tetrahedral order around an atom $i$ corresponds to $q_t(i) = 1$.

## III. RESULTS AND DISCUSSION

We start by commenting on the results obtained at rest ($\gamma = 0$) as a function of density, since they provide a baseline to understand how shear impacts the properties of supercooled Si. For a temperature $T = 1060$ K, previous work $^{11,34}$ has shown that there is a first-order liquid-liquid transition from a high-density liquid (HDL) to a low-density liquid (LDL). Since this temperature is below the melting point, we emphasize that these states are metastable. This means that, at rest, they can, and eventually will, evolve with time. Here, we show the results, at rest, obtained after $4 \times 10^{6}$ time steps or, equivalently, after 4 ns. We present in Fig. 1(a) the radial distribution function $g(r)$ for supercooled liquids of Si with densities ranging from $2.28$ g/cm$^3$ to $2.52$ g/cm$^3$. Examination of the evolution of the $g(r)$ as a function of density shows two distinct behaviors below and above a density of $2.4$ g/cm$^3$. The structural differences can be seen by looking at the features of the first two peaks in the $g(r)$. For the lower densities, the first maximum is reached at about $2.38$ Å with a value close to 4 for this distance. The first minimum is located at $2.95$ Å, which delimits the first coordination shell to be between $2$ Å and $2.95$ Å. The second peak is reached for $3.9$ Å with a maximum of about 2 (half of that in the first shell) and a second minimum located at $4.9$ Å, which means that the second coordination shell is between $2.95$ Å and $4.9$ Å. For densities greater than $2.4$ g/cm$^3$, the first maximum is reached for a distance of

![](./images/812582923600396288_8.jpg)

FIG. 1. (a) Pair correlation function g(r) for densities ranging from $\rho = 2.28$ g/cm$^3$ to $\rho = 2.52$ g/cm$^3$. (b) Coordination number obtained by integrating g(r). The same caption as in (a).

$2.42\ \text{Å}$ and a maximum probability of about 3 (i.e., 33% less than for the lower densities, and the first minimum can be seen for $2.97\ \text{Å}$). These features are in overall agreement with the structures found for LDL and HDL using *ab initio* molecular dynamics,⁷¹ with, most notably, the increased height of the first peak of $g(r)$ in LDL and a narrowing of the distance between the first and second maxima for HDL when compared to LDL. Unlike for the lower densities, a shoulder develops around $3.4\ \text{Å}$ between the first minimum $(2.97\ \text{Å})$ and the second maximum $(3.89\ \text{Å})$. In fact, this shoulder starts to form for $\rho = 2.40\ \text{g/cm}^3$ and becomes more predominant as the density of the system increases up to $\rho = 2.52\ \text{g/cm}^3$. It is the signature of the onset of structural order that has been referred to as medium-range order (MRO).⁷²,⁷³ We add that, for all systems, $g(r)$ converges toward one, showing that there is no long-range order. We also compute the value taken for $Q_6$ and find that, for all systems, $Q_6$ remains close to 0.014 throughout the time interval spanned during the simulations, confirming that we have obtained metastable liquids over the entire range of densities.

To analyze further the structure of these liquids, we calculate the coordination number $N_c$ by integrating g(r) as $\int 4\pi r^2 \rho g(r) dr$ and show the results in Fig. 1(b). For the lower densities, we find $N_c=4.23$ in the first coordination shell for $r<2.95\ \text{Å}$ (numbers given here for $\rho = 2.28\ \text{g/cm}^3$). This coordination number, together with

![](./images/812582923600396288_9.jpg)

FIG. 2. (a) Angle distribution for $\rho = 2.28\ \text{g/cm}^3$, $\rho = 2.32\ \text{g/cm}^3$, and $\rho = 2.44\ \text{g/cm}^3$. Distributions are shown for atoms with 3 (in red), 4 (in black), and 5 (in blue) first neighbors. (b) Left: tetrahedral local order parameter $q_t$ as a function of density. Right: Variation of 2-body SW energy vs 3-body SW energy for increasing density (the first filled circle in the right bottom corner is for $\rho = 2.28\ \text{g/cm}^3$). (c) Entropy $S_2$ as a function of density in supercooled liquids of Si at rest.

the $g(r)$ reported in Fig. 1(a), indicates that the lower end of the density range corresponds to the low-density liquid (LDL) of Si. Indeed, previous studies $^{11,34,35}$ have shown that the LDL is characterized by a largely tetrahedral structure with a coordination number between 4.20 and 4.24 at 1050 K in the NPH ensemble. On the other hand, for densities above $2.4\ \text{g/cm}^3$, the coordination number is $N_c = 4.83$ in the first coordination shell, i.e., $r < 2.98\ \mathring{\text{A}}$ (here on the example of $\rho = 2.44\ \text{g/cm}^3$). This is consistent with the larger $N_c$ reported for the high-density liquid (HDL) $^{11,34,35}$ for Si. This establishes that the range of densities studied here covers the two liquid forms LDL to HDL found at rest in supercooled Si.

We also consider other structural features and order parameters at rest to characterize in the next paragraphs how shear impacts the structure and properties of supercooled liquids of Si. In particular, we examine, as a function of density, the angle distributions for atoms with three, four, or five neighbors within a sphere of a $2.75\ \mathring{\text{A}}$ radius (i.e., the cutoff radius for the SW 3-body potential) and show the resulting plots in Fig. 2(a) for $\rho = 2.28\ \text{g/cm}^3$, $\rho = 2.32\ \text{g/cm}^3$, and $\rho = 2.44\ \text{g/cm}^3$. Figure 2(a) shows that, for all densities, the most frequent number of first neighbors is 4 (in black) with a distribution centered around the expected angle for a tetrahedral environment $(109.5^\circ)$. However, the corresponding probability steadily decreases with density from $85\%$ in the LDL $(\rho = 2.28\ \text{g/cm}^3)$ to $64\%$ in the HDL $(\rho = 2.44\ \text{g/cm}^3)$. Instead, atoms with both three and five first neighbors become more frequent, from $5\%$ to $9\%$ at $\rho = 2.28\ \text{g/cm}^3$ to $12\%$ and $21\%$ at $\rho = 2.44\ \text{g/cm}^3$, respectively. This finding is consistent with results from prior $ab\ initio$ equilibrium molecular dynamics calculations on LDL and HDL. $^{71}$ The decrease in tetrahedral order with density can also be measured by the order parameter $q_t$, as seen in the left panel of Fig. 2(b). The loss of tetrahedral order results in a decrease in $q_t$ from about 0.78 at low density $(\rho = 2.28\ \text{g/cm}^3)$ to $0.46\ (\rho = 2.52\ \text{g/cm}^3)$. This is accompanied by a combined increase in the 3-body energy and decrease in 2-body energy. Indeed, the 3-body energy in the SW potential is purely repulsive and reaches a minimum of 0 when there is a perfect tetrahedral environment around an atom. On the other hand, since a density increase results in a loss of tetrahedral order, the increase in 3-body energy with density is expected. Similarly, the decrease in the purely attractive 2-body energy is consistent with the increase in $N_c$ that results from the increase in density. Very interestingly, when at rest, both LDL and HDL liquids see their 2-body and 3-body energies fall onto the line shown in the right panel of Fig. 2(b). As we will see, this behavior differs markedly from what is observed under shear. Finally, we examine how entropy can be quantified in these highly nonequilibrium systems. Indeed, the evaluation of entropy for out-of-equilibrium systems has recently drawn considerable interest for metastable liquids undergoing a nucleation process $^{74-78}$ for systems driven out-of-equilibrium $^{79}$ and in active matter. $^{80}$ Here, we examine how the onset of tetrahedral ordering in LDL can be monitored by the decrease in the pair-correlation entropy $S_2$, defined as

$$
S_{2}=-\frac{\rho}{2} \int_{0}^{\infty}[g(r) \ln g(r)-(g(r)-1)] d r. \tag{9}
$$

Figure 2(c) shows that the enhanced structural features exhibited by the LDL form [see the $g(r)$ shown in Fig. 1(a)] result in a lower $S_2$ entropy than at high densities, i.e., for the HDL form. In other words, the results show that $S_2$ is sensitive enough, in the case of Si, to characterize the differences between LDL and HDL at rest and to serve as a baseline for the results under shear that we will discuss in the next paragraphs.

We now turn to the response of supercooled liquids of Si when subjected to shear. The results shown in Fig. 3 are obtained in the steady-state when a linear flow profile, with a slope equal to the imposed shear rate $\gamma^*$, has developed across the system. These systems remain liquid in the steady-state as a result of the continuous input of mechanical energy exerted by the imposition of this constant shear rate (structural features of the liquids under shear are presented in Figs. 3–5). The shear viscosity of supercooled liquids

![](./images/812582923600396288_10.jpg)

FIG. 3. (Left) Shear viscosity ($\eta$) as a function of shear rate ($\gamma^*$) for $\rho = 2.28\ \text{g/cm}^3$, $\rho = 2.32\ \text{g/cm}^3$, $\rho = 2.44\ \text{g/cm}^3$, and $\rho = 2.52\ \text{g/cm}^3$. (Right) Shear viscosity against the tetrahedral local order parameter $q_t$ (lines are plotted as a guide to the eye).

![](./images/812582923600396288_11.jpg)

of Si is shown on the left panel of Fig. 3 for $\rho = 2.28$ g/cm³, $\rho = 2.32$ g/cm³, $\rho = 2.44$ g/cm³, and $\rho = 2.52$ g/cm³. The liquids exhibit the expected shear-thinning behavior, with a decrease in shear viscosity with an increase in shear rate. The viscosity plots for the four densities become very similar for reduced shear rates beyond 0.01. As shown on the right panel of Fig. 3, these also amount to very similar values of the order parameter $q_t$ for the three densities, which implies that shear rates beyond 0.01 essentially wipe away any density-dependent structural features that can be seen in LDL and HDL systems at rest. On the other hand, when the reduced shear rate becomes lower than $1 \times 10^{-3}$, both shear viscosities and $q_t$ start to depend strongly on density and become much greater for $\rho = 2.28$ g/cm³ and $\rho = 2.32$ g/cm³ than for $\rho = 2.44$ g/cm³. For instance, for $\rho = 2.44$ g/cm³, the viscosity starts to reach the Newtonian plateau for shear rates of the order of $1 \times 10^{-3}$ with $\eta = 28$ mPa s. However, for the lower densities, the shear viscosity continues to increase as the shear rate decreases and reaches 460 mPa s ($\rho = 2.28$ g/cm³) and $\eta = 340$ mPa s ($\rho = 2.32$ g/cm³) for $\gamma^* = 1 \times 10^{-4}$. To determine the zero-shear (Newtonian) viscosity, we fit the data for the shear-rate dependent viscosity $\eta_N$ using an Eyring

![](./images/812582923600396288_12.jpg)

FIG. 5. (a) (Left) $\langle u_3 \rangle$ vs $\langle u_2 \rangle$ at rest for densities ranging from $2.28\ \text{g/cm}^3$ (bottom right corner) to $2.44\ \text{g/cm}^3$ (top left corner) is shown as circles. Also shown as red squares is $\langle u_3 \rangle$ vs $\langle u_2 \rangle$ under shear for reduced shear rates from $1 \times 10^{-4}$ (bottom right corner) to 1 (top left corner) at $\rho = 2.28\ \text{g/cm}^3$, while $\langle u_3 \rangle$ vs $\langle u_2 \rangle$ under shear for reduced shear rates from $1 \times 10^{-4}$ (bottom right corner) to 1 (top left corner) at $\rho = 2.44\ \text{g/cm}^3$ is shown as blue triangles. (Right) $g(r)$ for $\rho = 2.28\ \text{g/cm}^3$ (red is used at low shear and pink is used at high shear) and $\rho = 2.44\ \text{g/cm}^3$ (blue is used at low shear and cyan at high shear). (b) $S_2$ against $\rho$ for a shear rate of 0.001 (red circles) and a shear rate of 1 (blue circles).

model. $^{81}$ We find that, in accord with prior work, $^{37}$ the zero-shear rate viscosity for HDL is of the order of a few tens of mPa s with, e.g., $\eta_N = 15\ \text{mPa s}$ at $2.52\ \text{g/cm}^3$, while the zero viscosity for LDL is two orders of magnitude greater with, e.g., $\eta_N = 1614\ \text{mPa s}$ at $2.32\ \text{g/cm}^3$.

Most notably, we find that $q_t$ is in excess of 0.7 for $\gamma^* = 1 \times 10^{-4}$ for $\rho = 2.28\ \text{g/cm}^3$ and $\rho = 2.32\ \text{g/cm}^3$, while $q_t$ plateaus off around 0.5 at low shear rates for $\rho = 2.44\ \text{g/cm}^3$. This is a strong indication that, at low shear rates, the structural features of both LDL and HDL can be retained and that both liquid forms can be obtained under shear in the steady-state.

To ascertain this further, we focus on the results obtained for $\rho = 2.28\ \text{g/cm}^3$ and $\rho = 2.44\ \text{g/cm}^3$ and examine how shear impacts the coordination number $N_c$ and the angle distributions. We start with the results for $\rho = 2.28\ \text{g/cm}^3$, as shown in Fig. 4(a). We find that $N_c$ (left panel) exhibits two different behaviors as a function of the shear rate. For $\gamma^* < 0.01$, the coordination number plot as a function of distance is similar to that observed at rest, with an inflection around $r = 2.8\ \text{\AA}$ associated with the two sharp peaks found for $g(r)$ for the LDL form. This is confirmed by the value obtained for the first coordination shell ($Nc = 4.3$ for $\gamma^* = 0.0001$), which is consistent with that found at rest. As shown in Fig. 4(a), increasing the reduced shear rate beyond 0.01 changes the shape of the coordination number plot and, in turn, greatly reduces the amount of tetrahedral order in the fluid under shear as shown on the right panel of Fig. 4(a). Indeed, the maximum for the angle distribution decreases sharply with the shear rate, showing that fewer and fewer atoms have first four neighbors. Furthermore, the maximum for the distribution shifts toward the lower values at high shear rates and the distribution becomes tilted away from the distribution expected for a tetrahedral environment. The results therefore confirm that, provided that the reduced shear rate is below 0.01, a steady-state of a liquid with the structural hallmarks of the LDL form can be stabilized using shear. Turning to the results for $\rho = 2.44\ \text{g/cm}^3$ in Fig. 4(b), we find that the coordination number and angle distribution for shear rates below 0.01 are consistent with those found at rest. For instance, $N_c$ is found to be equal to 4.83 for a shear rate of $1 \times 10^{-4}$, in excellent agreement with the value obtained at rest. Similarly, as shown on the right panel of Fig. 4(b), the maximum for the angle distribution when $\gamma^* = 1 \times 10^{-4}$ is 0.11, in line with the value of 0.11 found at rest. We also observe that shear rates beyond 0.01 wipe away these features, as shown by the steady decrease in the maximum for the angle distribution with increasing shear. Overall, the results show that, for shear rates below 0.01, we have succeeded in obtaining in the steady-state a liquid with the structural characteristics of the HDL form and that both the steady-states of the two metastable forms of liquid Si have been stabilized under shear.

As discussed in Fig. 2(b), there is a linear relation between the two components of the potential energy that remains valid in both of the LDL and HDL forms at rest. We compare in Fig. 5(a) the linear plot obtained at rest to the $\langle u_2 \rangle$ vs $\langle u_3 \rangle$ plots obtained for different shear rates at $2.28\ \text{g/cm}^3$ and $2.44\ \text{g/cm}^3$. We observe that the results obtained for the lowest shear rates fall onto the $\langle u_2 \rangle$ vs $\langle u_3 \rangle$ line obtained at rest, further establishing that shear rates below 0.01 do not alter the nature of the LDL and HDL forms both from an energetic standpoint [Fig. 5(a)] and from a structural standpoint (Fig. 4). The energy plots for larger shear rates give some insight into the dramatic changes that take place at higher shear rates for both densities. As shear rate increases, the 2-body vs 3-body relation departs more and more from the linear relation observed at rest, a trend that is confirmed by the structural changes experienced by the fluid at high shear rates as shown by the pair correlation functions obtained at high shear rates [Fig. 5(b)]. While the $g(r)$ observed under low shear for $2.28\ \text{g/cm}^3$ and $2.44\ \text{g/cm}^3$ are in

$\rho = 2.28\ \text{g/cm}^3$
$\rho = 2.44\ \text{g/cm}^3$

![](./images/812582923600396288_13.jpg)

FIG. 6. Probability of finding a neighboring Si atom in the (x, y) plane within a slab of a width of $\sigma$ along the z axis for $\rho = 2.28\ \text{g/cm}^3$ (left panel) and $\rho = 2.44\ \text{g/cm}^3$ (right panel). For each panel, the top graph corresponds to the lowest shear rate studied ($1 \times 10^{-4}$) and the bottom graph to the highest shear rate (1).

very good agreement with their counterparts at rest for the LDL and HDL forms [Fig. 1(a)], the $g(r)$ under high shear are very similar for both densities, with a single well-defined peak and little structural detail beyond. This confirms that applying too high a shear rate destabilizes the formation of tetrahedral order for all densities and prevents the system from exhibiting the two types of liquid forms obtained at rest. In other words, there is an upper limit to the applied shear (here identified to be 0.01) that can be used to stabilize the LDL and HDL.

Another way to assess the loss of organization or, equivalently, of information at high shear can be made through the evaluation of the $S_2$ entropy. Figure 5(b) shows a comparison of how $S_2$ varies with the liquid density for a shear rate of 0.001 and a shear rate of 1. We observe that, at $\gamma^* = 0.001$ and for all densities, the liquid is more organized and has a lower $S_2$ than at high shear rate. This is in line with the less structured $g(r)$ shown in Fig. 5(a) for the larger shear rates. Furthermore, for a shear rate of 0.001, $S_2$ increases with density. This can be attributed to the gradual loss of organization that takes place as density increases as a result of the decrease in tetrahedral order. On the other hand, $S_2$ is almost constant over the entire density range for $\gamma^* = 1$. This stems from the very similar $g(r)$ obtained for all densities at high shear rates.

To understand better the effect of shear on the liquid structure, we plot in Fig. 6 a probability map of the presence of a neighboring atom in the (x, y) plane within a slab of a width of $\sigma$ along the z axis. At low shear rates, two dark circular regions appear clearly for both densities, corresponding to the first two peaks observed in the pair correlation function. The contrast between the first two dark disks is much sharper at low density, as a result of the strong short-range tetrahedral order that takes place in the LDL form than in the HDL form. This characterizes the in-plane structure of the liquids subjected to a low shear rate and confirms the LDL/HDL nature of the steady-state generated under these conditions. On the other hand, the plots are very different at a high shear rate, with a single dark ellipse observed for all densities. This ellipse corresponds to the single peak exhibited by $g(r)$ at high shear. Furthermore, the ellipse clearly highlights the compression axis (diagonal that goes from the top left corner to the bottom right corner), which shows the increased contact, and this decreased distance between two Si atoms along that diagonal (this effect is due to the greater streaming velocity of, e.g., an atom coming from the top left corner with respect to the central atom). Similarly, the opposite diagonal shows the elongation axis (bottom left corner to top right corner), with a greater distance between two neighboring atoms along that axis.

## IV. CONCLUSIONS

In this work, we use NEMD methods to study the response of metastable liquids of silicon, when subjected to shear. We show that, for sufficiently low shear rates, we achieve the formation, in the steady-state, of liquids that have similar structural, energetic, and entropic signatures to the metastable liquids identified at rest as the low-density liquid (LDL) and high-density liquid (HDL) forms. In particular, we establish that, at $T = 1090$ K, the LDL features are seen in Si under shear for densities below $2.4\ \text{g/cm}^3$ and for reduced shear rates below 0.01, while the HDL features are recovered for densities greater than $2.4\ \text{g/cm}^3$ and for reduced shear rates below 0.01. The competition between shear and tetrahedral

ordering is also unraveled via the determination of the variations of the tetrahedral order parameter $q_t$ and of the two-body entropy $S_2$ as a function of the applied shear, leading to a cross-validation of the range of shear rates for which the two liquid polymorphs can be obtained. The results point to the efficiency and reliability of using shear as a means to stabilize metastable liquids under out-of-equilibrium conditions. Most notably, these nonequilibrium liquids often exhibit dramatically different properties. Indeed, the LDL of Si is semimetallic with a pseudogap, while the HDL of Si is metallic with no bandgap. Being able to control the liquid properties via shear is an intriguing prospect, both for Si and for the increasing range of atomic and molecular fluids, including water, which are polymorphic.

## ACKNOWLEDGMENTS
Partial funding for this research was provided by the National Science Foundation through Award No. CHE-1955403. This work used the Extreme Science and Engineering Discovery Environment (XSEDE), $^{82}$ which is supported by the National Science Foundation (Grant No. ACI-1548562) and used the Open Science Grid through Grant No. TG-CHE200063.

## DATA AVAILABILITY
The data that support the findings of this study are available from the corresponding author upon reasonable request.

## REFERENCES
$^{1}$P. H. Poole, T. Grande, C. A. Angell, and P. F. McMillan, *Science* **275**, 322 (1997).
$^{2}$S. Harrington, R. Zhang, P. H. Poole, F. Sciortino, and H. E. Stanley, *Phys. Rev. Lett.* **78**, 2409 (1997).
$^{3}$O. Mishima and H. E. Stanley, *Nature* **392**, 164 (1998).
$^{4}$K. Koga, H. Tanaka, and X. C. Zeng, *Nature* **408**, 564 (2000).
$^{5}$G. Franzese, G. Malescio, A. Skibinsky, S. V. Buldyrev, and H. E. Stanley, *Nature* **409**, 692 (2001).
$^{6}$R. Kurita and H. Tanaka, *Science* **306**, 845 (2004).
$^{7}$C. J. Roberts, A. Z. Panagiotopoulos, and P. G. Debenedetti, *Phys. Rev. Lett.* **77**, 4386 (1996).
$^{8}$Y. Katayama, T. Mizutani, W. Utsumi, O. Shimomura, M. Yamakata, and K.-i. Funakoshi, *Nature* **403**, 170 (2000).
$^{9}$M. Togaya, *Phys. Rev. Lett.* **79**, 2474 (1997).
$^{10}$J. N. Glosli and F. H. Ree, *Phys. Rev. Lett.* **82**, 4659 (1999).
$^{11}$S. Sastry and C. A. Angell, *Nat. Mater.* **2**, 739 (2003).
$^{12}$K. Zhang, H. Li, and Y. Y. Jiang, *Phys. Chem. Chem. Phys.* **16**, 18023 (2014).
$^{13}$N. Jakse and A. Pasturel, *Phys. Rev. Lett.* **99**, 205702 (2007).
$^{14}$M. Beye, F. Sorgenfrei, W. F. Schlotter, W. Wurth, and A. Föhlisch, *Proc. Natl. Acad. Sci. U. S. A.* **107**, 16772 (2010).
$^{15}$O. Mishima, *Phys. Rev. Lett.* **85**, 334 (2000).
$^{16}$A. K. Soper and M. A. Ricci, *Phys. Rev. Lett.* **84**, 2881 (2000).
$^{17}$P. H. Poole, F. Sciortino, U. Essmann, and H. E. Stanley, *Nature* **360**, 324 (1992).
$^{18}$O. Mishima and H. E. Stanley, *Nature* **396**, 329 (1998).
$^{19}$J. L. F. Abascal and C. Vega, *J. Chem. Phys.* **133**, 234502 (2010).
$^{20}$Y. Liu, J. C. Palmer, A. Z. Panagiotopoulos, and P. G. Debenedetti, *J. Chem. Phys.* **137**, 214505 (2012).
$^{21}$J. C. Palmer, F. Martelli, Y. Liu, R. Car, A. Z. Panagiotopoulos, and P. G. Debenedetti, *Nature* **510**, 385 (2014).

$^{22}$R. S. Singh, J. W. Biddle, P. G. Debenedetti, and M. A. Anisimov, *J. Chem. Phys.* **144**, 144504 (2016).
$^{23}$J. C. Palmer, R. Car, and P. G. Debenedetti, *Faraday Discuss.* **167**, 77 (2013).
$^{24}$J. C. Palmer, P. H. Poole, F. Sciortino, and P. G. Debenedetti, *Chem. Rev.* **118**, 9129 (2018).
$^{25}$D. T. Limmer and D. Chandler, *J. Chem. Phys.* **135**, 134503 (2011).
$^{26}$D. T. Limmer and D. Chandler, *J. Chem. Phys.* **138**, 214504 (2013).
$^{27}$J. C. Palmer, A. Haji-Akbari, R. S. Singh, F. Martelli, R. Car, A. Z. Panagiotopoulos, and P. G. Debenedetti, *J. Chem. Phys.* **148**, 137101 (2018).
$^{28}$R. Kurita and H. Tanaka, *J. Phys.: Condens. Matter* **17**, L293 (2005).
$^{29}$H. Tanaka, R. Kurita, and H. Mataki, *Phys. Rev. Lett.* **92**, 025701 (2004).
$^{30}$H. Tanaka, *Phys. Rev. E* **62**, 6968 (2000).
$^{31}$M. Huš and T. Urbic, *Phys. Rev. E* **90**, 062306 (2014).
$^{32}$C. Desgranges and J. Delhommelle, *J. Chem. Phys.* **149**, 111101 (2018).
$^{33}$K.-i. Murata and H. Tanaka, *Nat. Commun.* **4**, 2844 (2013).
$^{34}$P. Beaucage and N. Mousseau, *J. Phys.: Condens. Matter* **17**, 2269 (2005).
$^{35}$P. Beaucage and N. Mousseau, *Phys. Rev. B* **71**, 094102 (2005).
$^{36}$F. H. Stillinger and T. A. Weber, *Phys. Rev. B* **31**, 5262 (1985).
$^{37}$X. Mei and J. Eapen, *Phys. Rev. B* **87**, 134206 (2013).
$^{38}$P. G. Debenedetti, *Metastable Liquids: Concepts and Principles* (Princeton University Press, 1996).
$^{39}$C. Desgranges and J. Delhommelle, *J. Am. Chem. Soc.* **133**, 2872 (2011).
$^{40}$S. Butler and P. Harrowell, *Nature* **415**, 1008 (2002).
$^{41}$J. Delhommelle, *Phys. Rev. B* **69**, 144117 (2004).
$^{42}$M. Ramsay and P. Harrowell, *Phys. Rev. E* **93**, 042608 (2016).
$^{43}$S. R. Williams and D. J. Evans, *J. Chem. Phys.* **132**, 184105 (2010).
$^{44}$S. Abraham and P. Harrowell, *J. Chem. Phys.* **137**, 014506 (2012).
$^{45}$C. Desgranges and J. Delhommelle, *Phys. Rev. B* **78**, 184202 (2008).
$^{46}$D. Evans and G. Morriss, *Nonequilibrium Statistical Mechanics of Liquids* (Cambridge University Press, Cambridge, 2008).
$^{47}$C. Desgranges and J. Delhommelle, *J. Chem. Phys.* **128**, 084506 (2008).
$^{48}$G. P. Morriss, *Phys. Rev. A* **39**, 4811 (1989).
$^{49}$D. J. Evans, E. Cohen, D. J. Searles, and F. Bonetto, *J. Stat. Phys.* **101**, 17 (2000).
$^{50}$B. D. Todd and P. J. Daivis, *Mol. Simul.* **33**, 189 (2007).
$^{51}$J. P. Ewen, D. M. Heyes, and D. Dini, *Friction* **6**, 349 (2018).
$^{52}$G. Zhao, Y. Yu, J. Yan, M. Ding, X. Zhao, and H. Wang, *Phys. Rev. B* **93**, 140203 (2016).
$^{53}$S. Sarman, D. J. Evans, and A. Baranyai, *Physica A* **208**, 191 (1994).
$^{54}$C. P. Dettmann and G. P. Morriss, *Phys. Rev. E* **54**, 2495 (1996).
$^{55}$K. P. Travis, P. J. Daivis, and D. J. Evans, *J. Chem. Phys.* **103**, 10638 (1995).
$^{56}$K. Bagchi, S. Balasubramanian, C. J. Mundy, and M. L. Klein, *J. Chem. Phys.* **105**, 11183 (1996).
$^{57}$J. Delhommelle and D. J. Evans, *J. Chem. Phys.* **115**, 43 (2001).
$^{58}$L. Lue, O. G. Jepps, J. Delhommelle, and D. J. Evans, *Mol. Phys.* **100**, 2387 (2002).
$^{59}$J. Delhommelle and D. J. Evans, *J. Chem. Phys.* **117**, 6016 (2002).
$^{60}$C. Braga and K. P. Travis, *J. Chem. Phys.* **123**, 134101 (2005).
$^{61}$A. A. Samoletov, C. P. Dettmann, and M. A. J. Chaplain, *J. Chem. Phys.* **132**, 246101 (2010).
$^{62}$J. Delhommelle, J. Petravic, and D. J. Evans, *Phys. Rev. E* **68**, 031201 (2003).
$^{63}$F. Zhang, D. J. Searles, D. J. Evans, J. S. den Toom Hansen, and D. J. Isbister, *J. Chem. Phys.* **111**, 18 (1999).
$^{64}$D. J. Evans and G. P. Morriss, *Phys. Rev. A* **38**, 4142 (1988).
$^{65}$C. Desgranges and J. Delhommelle, *Phys. Rev. E* **77**, 027701 (2008).
$^{66}$R. Hartkamp, S. Bernardi, and B. D. Todd, *J. Chem. Phys.* **136**, 064105 (2012).
$^{67}$P. J. Steinhardt, D. R. Nelson, and M. Ronchetti, *Phys. Rev. B* **28**, 784 (1983).

---

J. Chem. Phys. **153**, 054502 (2020); doi: 10.1063/5.0015417
Published under license by AIP Publishing

153, 054502-9

$^{68}$P. R. Ten Wolde, M. J. Ruiz-Montero, and D. Frenkel, *Phys. Rev. Lett.* **75**, 2714 (1995).

$^{69}$P.-L. Chau and A. J. Hardwick, *Mol. Phys.* **93**, 511 (1998).

$^{70}$J. R. Errington and P. G. Debenedetti, *Nature* **409**, 318 (2001).

$^{71}$G. Zhao, Y. J. Yu, and X. M. Tan, *J. Chem. Phys.* **143**, 054508 (2015).

$^{72}$L. Hui, *Phys. Rev. B* **68**, 024210 (2003).

$^{73}$H. Tanaka, *Eur. Phys. J. E* **35**, 113 (2012).

$^{74}$C. Desgranges and J. Delhommelle, *J. Chem. Phys.* **145**, 204112 (2016).

$^{75}$C. Desgranges and J. Delhommelle, *J. Chem. Phys.* **145**, 234505 (2016).

$^{76}$C. Desgranges and J. Delhommelle, *J. Chem. Phys.* **146**, 184104 (2017).

$^{77}$P. M. Piaggi, O. Valsson, and M. Parrinello, *Phys. Rev. Lett.* **119**, 015701 (2017).

$^{78}$C. Desgranges and J. Delhommelle, *Phys. Rev. E* **98**, 063307 (2018).

$^{79}$M. Zu, A. Bupathy, D. Frenkel, and S. Sastry, *J. Stat. Mech.: Theory Exp.* **2020**, 023204.

$^{80}$S. Martiniani, P. M. Chaikin, and D. Levine, *Phys. Rev. X* **9**, 011031 (2019).

$^{81}$V. Jadhao and M. O. Robbins, *Proc. Natl. Acad. Sci. U. S. A.* **114**, 7952 (2017).

$^{82}$J. Towns, T. Cockerill, M. Dahan, I. Foster, K. Gaither, A. Grimshaw, V. Hazlewood, S. Lathrop, D. Lifka, G. D. Peterson *et al.*, *Comput. Sci. Eng.* **16**, 62 (2014).

J. Chem. Phys. **153**, 054502 (2020); doi: 10.1063/5.0015417

Published under license by AIP Publishing

153, 054502-10