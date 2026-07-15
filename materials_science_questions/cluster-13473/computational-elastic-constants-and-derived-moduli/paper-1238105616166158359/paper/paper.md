# Averaging Molecular Dynamics simulations to study the slow-strain rate behaviour of metals

Sarthok Kumar Baruahª, Sabyasachi Chatterjeeª, Amit Acharyaç, Gerald J. Wangᵇ

ªDepartment of Applied Mechanics, Indian Institute of Technology Delhi, Hauz Khas, New Delhi 110016, India
ᵇDepartment of Civil and Environmental Engineering, Carnegie Mellon University, Pittsburgh, PA 15213
ᶜDepartment of Civil and Environmental Engineering & Center for Nonlinear Analysis, Carnegie Mellon University, Pittsburgh, PA 15213

## Abstract
The application of molecular dynamics (MD) simulations to quasi-static loading is severely limited by the large separation between atomic vibration timescales and experimentally relevant deformation rates. In this work, we employ the Practical Time Averaging (PTA) framework to overcome this limitation and enable atomistic simulations of crystalline solids under quasi-static loading conditions. PTA exploits the intrinsic separation of timescales by defining slow variables as time-averaged observables of the fast atomistic dynamics and their evolution in the slow loading timescale, thereby avoiding explicit integration of the fast dynamics.

Using this approach, we simulate uniaxial deformation, in both tension and compression, of (4 to 20) nanometer sized cubic specimens of face-centered cubic Aluminum nanocrystals and applied strain rates approaching quasi-static conditions ($10^{-4}s^{-1}-10^{-3}s^{-1}$). We define slow variables as the averaged kinetic energy, potential energy and normal stress in the loading direction, and show their evolution in the slow time scale. The stress-strain curves show yield close to the theoretical yield stress for homogeneous nucleation, followed by successive load drops and rise, caused due to dislocation nucleation, motion and exit from free surfaces. The "smaller is harder" effect is evident from the stresss-strain response as well as from the variation of yield stress with the sample size. The serrations in the response are more pronounced for smaller samples. The effects of applied strain rate and initial temperature are studied. An interesting aspect of our study is that it is also able to show the evolution of intricate dislocation microstructures in the slow time scale, by tracking the (fast) time-averaged atomic positions. The PTA framework enables simulations at strain rates several orders of magnitude lower than those accessible to conventional MD, demonstrating significant speedup in computer time, while retaining full atomistic resolution.

**Keywords:** Molecular Dynamics, Time Averaging, Multiscale Modelling

---

## 1. Introduction
Molecular dynamics (MD) simulations have become a powerful tool in understanding material behavior. However, a key difficulty in using MD for engineering applications is due to the extremely large separation between the timescales of atomic vibrations (on the order of femtoseconds) and the timescales of applied loading (on the order of seconds). A long-standing limitation in the use of molecular dynamics (MD) simulation is that it can only be applied directly to processes that take place on very short timescales. Many important processes in chemistry, physics and materials science take place on time scales that cannot be reached by molecular dynamics, which is limited to nanoseconds (or a few microseconds for very small systems). This restricts MD to extremely high strain rates of $10^{8}s^{-1}$ to $10^{10}s^{-1}$.

Application of MD is therefore not feasible in many problems of practical interest such as materials under slow loading rates (such as quasi-static tension test), evolution of defects in materials such as voids and bubbles, twinning, phase-transformation, protein folding and many others. Radiation damage in structural materials used in nuclear reactors involves the evolution of an isolated collision cascade over picosecond (ps) time scales followed by long-term evolution of such defects which include both annihilation and aggregation. In order to effectively predict radiation-damage evolution, longer time-scale behavior of such defects must be simulated. Another potential application is investigating thin-film deposition and crystal growth where deposition events take place in the order of picoseconds but the time to next deposition is in the order of seconds. Most MD simulations employ deposition rates which are $10^{8}-10^{11}$ orders of magnitude higher than experimental values. However, thermally activated

---

*Corresponding Author*
Email address: sabyasachi@am.iitd.ac.in (Sabyasachi Chatterjee)

atomic processes with rates as low as one per second can have significant effects on thin-film microstructures. The high atom deposition rate required for conventional MD simulations cannot realistically model such processes and thus, alternative methods such as PTA must be used. In the specific case of metal plasticity, dislocation motion is characterized by stick-and-slip motion where dislocations are stuck for long periods of time (with respect to MD time-scale) followed by sudden slip.

Several MD studies have been made on the effect of size and strain rate on the mechanical behavior of materials like Kabir et al. (2024); Chang et al. (2017); Yu et al. (2013); Wan et al. (2021); Komanduri et al. (2001); Vogl et al. (2021); Uchic et al. (2004); Van Vliet et al. (2003). In almost all the above studies, simulating material behavior at much slower strain rates still remains a significant challenge. Thus, traditional MD methods become computationally infeasible at such slow rates because of the unrealistically large number of time steps required to reach the characteristically large observed deformations.

Numerous techniques have been developed to address the challenge of accessing long timescales in MD simulations, which we briefly review here. A popular class of methods – including hyperdynamics Voter (1997), metadynamics Laio and Parrinello (2002), and Gaussian accelerated MD Miao et al. (2015) – broadly involves modifying the energy landscape to accelerate exploration of phase space. Another broad class of methods – including replica exchange MD Sugita and Okamoto (1999) and temperature-accelerated dynamics So/rensen and Voter (2000); Zamora et al. (2016) – achieves this accelerated exploration by performing simulations at temperatures higher than the temperature of interest. A large number of approaches fall under the umbrella of pathway-focused methods. Such methods focus on sampling along specific reaction coordinates, with less or no effort invested in sampling in directions orthogonal to the chosen ones (see, e.g., reviews in Bolhuis and Swenson (2021); Mohr et al. (2024)). Coarse-graining spatial degrees of freedom is yet another common approach to access long timescales, covering an enormous number of methods (see, e.g., reviews in Shi et al. (2023); Noid et al. (2024)). The method discussed herein shares the most conceptual similarity with existing techniques that explicitly (or implicitly) leverage the separation of timescales between fast and slow dynamics, most notably Mori-Zwanzig-based methods (Izvekov and Voth (2006); Hijón et al. (2010); Mielke et al. (2025)), methods based on adiabatic elimination of fast dynamics (Berezhkovskii and Szabo (2011)), or mathematical homogenization for Hamiltonian systems, see, e.g., (Bornemann and Schütte (1997); Bornemann (1998); Klar et al. (2021)).

Each existing method presents certain drawbacks, which the method discussed herein avoids, either altogether or at least in ways that differ from the existing method. The energy-landscape-modification and elevated-temperature methods all fundamentally alter transition rates between states (and typically require some knowledge of and/or assumptions about the underlying kinetics in order to correct for these altered transition rates). Pathway-focused methods typically require prior knowledge of and/or assumptions about productive reaction coordinates along which to sample. Current methods driven by separation of timescales mentioned in the previous paragraph typically require a) expensive computation of and/or assumptions about a memory kernel that links the fast and slow dynamics or b) an assumption of the fast dynamics in question settling on an equilibrium point in phase space for fixed slow variables (adiabatic elimination or the Tikhonov scheme (see, e.g., Artstein (2002); Chatterjee et al. (2018)), which is not satisfied by MD (especially NVE) systems or c) the satisfaction of delicate resonance conditions ((Bornemann, 1998, discussion of Takens chaos),Neishtadt (2019)). Spatial coarse-graining has a long history of successes and challenges; since these methods act on spatial degrees of freedom, most of these methods could likely be integrated with the approach developed herein in a relatively straightforward manner.

The separation of timescales of atomic vibrations in MD and applied slow loading leads to singularly perturbed forms of the evolution equations. In this context, the coarse-graining scheme named Practical Time Averaging (PTA), originating in Slemrod and Acharya (2012); Acharya and Sawant (2006) and given definitive form in Chatterjee et al. (2018), was developed to understand the behavior of nonlinear systems on a time scale much slower than that of the intrinsic dynamics. The technique deals with the averaging of singularly perturbed differential equations, which involve a small parameter representing the ratio between the fast and slow fundamental time periods involved and the goal of PTA is to develop a tool to model the limiting behavior as the parameter tends to zero. For small values of the parameter, the direct simulation of the underlying nonlinear dynamics becomes infeasible due to the restriction on the time-step. Hence, instead of evolving the fast dynamics, slow variables were introduced as averages of the state function of the fast dynamics. The scheme also provides the evolution of slow variables, which gives a measurement of the underlying intrinsic fast dynamics. In Chatterjee et al. (2018) a further improvement of the scheme is developed, describing a procedure to obtain the initial conditions of the fast trajectory of the state at a time in the future on the slow time scale, not accessible using a direct calculation with the fast dynamics. They also demonstrated the application of the scheme to problems that involve both conservative as well as dissipative microscopic dynamics such as slowly evolving fast oscillations, exponential decay, and even sharp jump (i.e., fast behavior) in the evolution of the slow variable.

Prior applications of PTA to model engineering problems include the work Tan et al. (2014), who applied it to two-dimensional lattice made of Nickel–Manganese undergoing detwinning and a three-dimensional atomic chain

made of face-centered cubic (FCC) Nickel under uniaxial tension. The macroscopic features such as space-time averaged strain/stress) are obtained from coarse dynamics, qualitatively consistent with generic observed behavior for the systems involved. Significant time savings compared to conventional MD was observed. In another work, Chatterjee et al. (2020) used PTA to time-average fast Dislocation Dynamics (DD) and use the resulting slow-variables to replace constitutive phenomenological assumptions in Mesoscale Field Dislocation Mechanics (MFDM) continuum model of plasticity Acharya and Roy (2006); Roy and Acharya (2005, 2006); Arora and Acharya (2020b,a). The mechanical response of macroscopic samples at slow loading rates up to moderately large strains was computed with significant savings in computing time compared to conventional DD.

The objective of the present work is to demonstrate the application of PTA to more complex and realistic engineering problems. The system we consider is a molecular dynamical system of FCC Aluminum crystal of few nanometers upto tens of nanometers in size, undergoing uniaxial tension and compression at quasi-static loading rates. We define *slow* variables of interest and evolve them on the slow time-scale of applied loading. We also show other details such as evolution of the atomic microstructure and dislocation configurations at quasi-static loading rates. Experimental studies of such details of evolution of microstructure at slow loading rates is challenging, which makes validation of these aspects in detail difficult. Our work may also be considered as posing some challenges for experiments in this sense.

This paper is organized as follows. In Section 2, we discuss the PTA numerical scheme and algorithm. In Section 3, we discuss the problem setup. In Section 4, we show the results of our work followed by conclusion in Section 5.

## 2. Methodology

In this section, we will discuss the PTA scheme and algorithm. A detailed discussion can be found in Chatterjee et al. (2018). Here, we provide a summary which includes the definition of the *slow* variable and its evolution equation. This is followed by the algorithm of its implementation.

### 2.1. Singularly perturbed differential equations

A particular class of ODE which involves a split into fast and slow dynamics, coupled to each other, is of the form

$$
egin{aligned}
rac{dx}{dt} &= rac{1}{\epsilon}F(x,l) \
rac{dl}{dt} &= L(x,l),
\end{aligned}
	ag{1}
$$

with $x \in \mathbb{R}^n$ and $l \in \mathbb{R}^m$. Here, $x$ corresponds to the fast variable and its evolution is governed by the fast dynamics. Denoting $\sigma = rac{t}{\epsilon}$ as time scale of the fast dynamics, the fast evolution equation becomes

$$
rac{dx}{d\sigma} = F(x,l).
	ag{2}
$$

On the other hand, $l$ corresponds to the load, which evolves in the slow time scale and can be considered to be fixed in the fast dynamics in Eq. (2). Such class of ODEs are called *singularly perturbed differential equations*. In the context of MD, we can think of $x$ as the position and velocities of atoms with characteristic time period of $T_f$ which is in the order of the time period of atomic vibrations (femtoseconds). $l$ is the slow applied loading rate, with time period $T_f$ (typically a few to 1000 seconds). The small real parameter $\epsilon > 0$, represents the ratio between fast and slow time periods, i.e. $\epsilon = rac{T_f}{T_s}$. In the case of MD under slow strain rates, it is of the order of $10^{-15}$ or even smaller, which shows the vast separation in time scales between fast and slow dynamics. This small parameter multiplies the highest order derivative in the governing equation, thus forming a *singular perturbation* of the rest of the terms in the equation. Often, the limit behavior as $\epsilon \to 0$ is well-recovered simply by obtaining the solution to the problem by setting $\epsilon = 0$. However, in many cases of practical relevance, as in MD, this is no longer true and obtaining the slow limit behavior requires more delicate analysis and the use of such understanding in robust and successful computation of the slow behavior of such systems. As already mentioned, the primary challenge in the direct computation of a singularly perturbed evolution is that when $\epsilon$ becomes very small, the time-step needs to reduce significantly as well, making the computations impractical. In such cases, instead of obtaining a full solution, a practical strategy is to define *slow* variables which give a measurement of the underlying dynamics. In the next section, we discuss the Practical Time Averaging (PTA) framework and algorithm, which precisely follows this idea.

### 2.2. Practical Time Averaging (PTA) - framework and algorithm

In Chatterjee et al. (2018), a class of slow variables called H-observables (where H stands for history) were defined as:
$$
\mathrm{v}_{m}(t)=\frac{1}{\Delta} \int_{t-\Delta}^{t} \int_{\mathbb{R}^{n}} m(x) \mu(s)(d x) d s,
\tag{3}
$$
where $m(x)$ is a state function of the fast dynamics, $\mu(s)$ is the invariant measure (also called Young measure) which gives the probability density function of the fast trajectory and $\Delta$ is an interval in the slow time scale. Thus, H-observables are averages over an interval in slow time of the moments of state functions with respect to the probability density function (Young measure) of the fast trajectory. Hence, such variables not only depend on the value of the measure at time $t$ but on the "history" of the measure in the interval $[t-\Delta, t]$.

Differentiation of Eq. (3) in time using Newton-Leibnitz rule gives the time-derivative of the slow variable in the form:
$$
\frac{d \mathrm{v}_{m}}{d t}(t)=\frac{1}{\Delta}\left(\int_{\mathbb{R}^{n}} m(x) \mu(t)(d x)-\int_{\mathbb{R}^{n}} m(x) \mu(t-\Delta)(d x)\right).
\tag{4}
$$

Given the initial conditions of the fast and slow variables i.e. $x(t_{0})$ and $l(t_{0})$, where $t_{0}=-\Delta$ is the initial time, we think of the calculations marching forward in slow time-scale in discrete steps (also called jumps) of size $h$ in the slow time scale, with total time as $T_{0}=n h$. Thus the variable $t$ below in description of our algorithm takes values of $0, h, 2h, ..., nh$. The interval $\Delta$ in the slow time-scale is a fraction of $h$ and its value is given in Table. 1. The goal is to determine the successive values of the slow variable $\mathrm{v}(t)$ in the slow time, which gives a measure of the underlying fast dynamics.

- **Step 1: Calculate the rate of change of slow variable**
  We denote $\int_{\mathbb{R}^{n}} m(x) \mu(t)(d x)$ as $R_{t}^{m}$ and $\int_{\mathbb{R}^{n}} m(x) \mu(t-\Delta)(d x)$ as $R_{t-\Delta}^{m}$. In practice, we do not compute the Young Measure and then take the moment of the state function with respect to it, but instead obtain it as running time averages of the state function till it converges. However, the latter definition using the running time average is computationally efficient and is therefore utilized in our work. We denote it as $R_{t}^{m}$, which is computed as
  $$
  R_{t}^{m}=\frac{1}{N_{t}} \sum_{r=1}^{N_{t}} m\left(x\left(\sigma_{r}\right), I_{t}\right),
  \tag{5}
  $$
  where the successive values of $x(\sigma_{r})$ are calculated by running the fast dynamics given by Eq. (2) while holding the load $I_{t}$ at slow time $t$ fixed. The initial conditions to run the fast dynamics is discussed in Step 4. Here, $N_{t}$ is the number of fine time steps required for $R_{t}^{m}$ to converge up to a specified tolerance. A discussion on the convergence criteria is provided in Appendix A. In this work, we have three state functions (as defined later in Eq. (21)), and the tolerance for checking the convergence of the running time averages for each of them is provided in Table 1.

  Substituting Eq. (5) to the RHS of Eq. (4), the time derivative of the slow variable is computed as:
  $$
  \frac{d \mathrm{v}_{m}}{d t}(t)=\frac{1}{\Delta}\left(R_{t}^{m}-R_{t-\Delta}^{m}\right)
  \tag{6}
  $$

- **Step 2: Find the value of slow variables**
  The predicted value of slow variable using PTA at $(t+h)$ is given using the extrapolation rule:
  $$
  \mathrm{v}_{m}(t+h)=\mathrm{v}_{m}(t)+\frac{d \mathrm{v}_{m}(t)}{d t} h
  \tag{7}
  $$
  where $\frac{d \mathrm{v}_{m}(t)}{d t}$ is obtained from Eq. (6).

- **Step 3: Accept the Measure**
  The value of the slow variable at $(t+h)$ is defined as
  $$
  \mathrm{v}_{d}^{m}(t+h):=\frac{1}{N^{\prime}} \sum_{r} m\left(x\left(\sigma_{r}\right)\right), \quad \text { where } \quad N^{\prime}=\frac{\Delta}{\epsilon \Delta \sigma},
  \tag{8}
  $$
  and successive values $x(\sigma_{r})$ are obtained by running the fast dynamics in Eq. (2), using a suitable initial condition as described in Step 4. Note that the number of steps $N'$ used to calculate the slow variable $\mathrm{v}(t+h)$

above is different from the number of steps $N_t$ to determine the $R_t^m$ using Eq. (5) (with $N' >> N_t$). This shows that both $\mathrm{v}(t+h)$ and $R_t^m$ are running time averages but are computed over different number of fast time steps. Moreover, $N'$ is fixed but $N_t$ depends on how fast the running time average converges at slow time $t$. In practice, it is not feasible to run the fast dynamics over the period $\Delta$ when $\epsilon$ becomes very small, since $N'$ becomes exceedingly large. Hence, we approximate it using Simpson's rule as

$$
\mathrm{v}_{d}^{m}(t+h) \approx \frac{1}{6}\left(R_{t+h-\Delta}^{m}+4 R_{t+h-\frac{\Delta}{2}}^{m}+R_{t+h}^{m}\right)
\tag{9}
$$

where $R_{t+h-\Delta}^{m}, R_{t+h-\frac{\Delta}{2}}^{m}$, and $R_{t+h}^{m}$ are the converged values of the running time averages (as defined in Eq. (5)) at the slow times given by their respective subscripts. The initial conditions to run the fast dynamics in order to obtain these averages are provided in Eq. (13) in Step 4.

The relative error between the values of the slow variable $\mathrm{v}(t+h)$ computed using Eq. (7) and Eq. (9) is denoted as $e_{t+h}^{\mathrm{v}}$ and given by

$$
e_{t+h}^{\mathrm{v}}=\left|\frac{\mathrm{v}_{m}(t+h)-\mathrm{v}_{d}^{m}(t+h)}{\mathrm{v}_{d}^{m}(t+h)}\right|.
\tag{10}
$$

Since the fast dynamics at play is not known to satisfy the ergodicity assumption for each fixed value of applied load, the invariant measures of the limit (as $\epsilon \to 0$) dynamics at any slow time depends on the initial condition used to generate the fast trajectory - this is also borne out by our practical experience. The relative error $e_{t+h}^{\mathrm{v}}$ does not address that component of the error. Addressing and quantifying that component of the error is challenging because it requires knowing the solution of the fast dynamics over impossibly large (fast) times.

We say there is a match in the value of the slow variable at $t+h$ if $e_{t+h}^{\mathrm{v}}<t o l_{\mathrm{v}}$, where $t o l_{\mathrm{v}}$ is a specified tolerance for slow variable $v$. Since we have 3 different slow variables in our work (as defined in the discussion following Eq. (21)), we have three tolerances corresponding to each of them, which are listed in Table (1).In that case, we accept the value of the slow variable predicted by PTA at $t+h$ as defined in Eq. (7) and move on to the next slow time.

If not, we check whether there is a jump in the measure at $t+h$. Since we do not compute the measure but instead obtain the moments of state functions with respect to it, a jump in such moments identifies a jump in the measure indirectly. Hence, we check if the following inequality holds:

$$
\left|\frac{e_{1}}{e_{2}}-1\right| \geq t o l_{j}, \quad \text { where } \quad e_{1}=\left|\frac{R_{t+h}^{m}-R_{t}^{m}}{R_{t}^{m}}\right|, \quad e_{2}=\left|\frac{R_{t}^{m}-R_{t-h}^{m}}{R_{t-h}^{m}}\right|.
\tag{11}
$$

The above inequality is satisfied when $R_{t+h}^{m}$ is significantly different from $R_{t}^{m}$ and $R_{t-h}^{m}$, which occurs when there is a jump in the measure at time $t+h$.

In Eq. (11), we use the assumption that the measure does not undergo a jump at time $t$. However, if a jump in the measure is already detected at time $t$, we detect if there is a jump in the measure at time $t+h$ by checking if $e_{1} \geq t o l_{j}$, where $e_{1}$ is given in Eq. (11).

If a jump in the measure is detected, $\mathrm{v}_{d}^{m}(t+h)$ defined in Eq. (8) is accepted as the value of the slow variable at $t+h$ and the prediction of the slow variable given by the extrapolation rule in Eq. (7) is discarded.

### Step 4: Obtain the fine initial conditions
Step 1 and Step 3 requires obtaining the values of $R^{m}$ at different slow times. To obtain $R_{t}^{m}$, we need to run MD with an initial guess of the fast variable, $x_{t}^{\text{guess}}$, which is chosen as a fine state at a fast time corresponding to $t_{prev}$ for which $R_{t_{prev}}^{m}$ was considered to have converged. We denote such a state as $x_{t_{prev}}^{conv}$. As mentioned in Eq. (5), it takes $N_{t_{prev}}$ fine time steps for $R_{t_{prev}}^{m}$ to converge. Hence, $x_{t_{prev}}^{conv}$ is equivalent to $x(\sigma_{N_{t_{prev}}})$.

Based on the above argument, the initial guess at slow times $t-\Delta$ and $t$, used to obtained $R_{t-\Delta}^{m}$ and $R_{t}^{m}$ respectively in Eq. (6) in Step 1 are obtained as:

$$
\begin{aligned}
x_{t-\Delta}^{\text{guess}} &= x_{t-h}^{conv} \\
x_{t}^{\text{guess}} &= x_{t-\frac{\Delta}{2}}^{conv}
\end{aligned}
\tag{12}
$$

Similarly, the initial guess used to obtained $R_{t+h-\Delta}^m$, $R_{t+h-\frac{\Delta}{2}}^m$ and $R_{t+h}^m$ in Eq. (9) in Step 3, are obtained as:

$$
\begin{aligned}
x_{t+h-\Delta}^{guess} & =x_{t}^{conv} \\
x_{t+h-\frac{\Delta}{2}}^{guess} & =x_{t+h-\Delta}^{conv} \\
x_{t+h}^{guess} & =x_{t+h-\frac{\Delta}{2}}^{conv}
\end{aligned} \tag{13}
$$

If the running time average obtained by running the fast dynamics with initial condition $x_{t}^{guess}$ does not converge even after running a reasonably large number of fast time steps, then we cannot obtain $R_{t}^m$ using that $x_{t}^{guess}$. In such cases, we have to try different values of $x_{t}^{guess}$ and repeat Steps 3 and 4.

While the protocol defined above appears to produce plausible results for the applications we are interested in, as shown later in Section 3, defining these guesses for generating the approximate measures at well-separated slow times is a fundamental problem. The challenge here is that the initial condition for generating the measure at any slow time has to be within the basin of attraction of the invariant measure(s) corresponding to the limit flow at that slow time. Estimating such a location in phase space with some plausibility from well-separated, in slow-time, spurts of fast computation, as employed by our scheme requires some special consideration. One line of reasoning was provided by the closest-point-projection approach as described in (Chatterjee et al., 2018, Step 3 and Step 5 of Section 9). There, the initial condition was obtained by taking the closest point projection of a point in the support of the invariant measure at a slow time with respect to the measure at a previous slow time. Then linearly extrapolating these points gave the initial condition for the fast trajectory at the next slow time (under the condition that the measure evolves slowly and does not undergo a jump in this interval of slow time). Applying that protocol here did not result in success, most likely due to the lack of a adapted metric w.r.t which the required projection can be executed in phase space. Based on the naive choices made, the guesses obtained for initial conditions seemed to have excessive kinetic energy, resulting in non-convergence of the $R^m$ values over the typical time intervals that were employed to perform the averages.

At a fundamental level, the plausibility of our obtained results (up to validation) does not rule out the fact that the measure that we work with, say at slow time $t$, is not an approximation of any of the invariant measures of the limit dynamics we are trying to probe. A full answer to this (very) difficult question of predicting the slow dynamics of a fast evolution *with guarantees* and furthermore, with computational efficiency, awaits further study. A natural idea in this regard would be to evolve the slow variables ($v_\mu{^\alpha}$, $v_\nu{^\alpha}$) defined in Sec. 2.3 below (i.e., the slow variables corresponding to the atomic positions and velocities of an MD asembly) and consider these at a discrete slow time, $t$, as the initial condition for the fine dynamics at time $t$ to generate the various $R_{t}^m$.

In the meanwhile, we proceed with our strategy laid out above which produces plausible outcomes.

### 2.3. Molecular Dynamics

In this work, the fast dynamics is the evolution of a molecular dynamical system consisting of a block of FCC Aluminum atoms, as discussed later in Section 2.4.1. We have performed MD simulations with the software Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) to study the tensile and compressive behaviors of metals under slow strain rates using embedded-atom method (EAM). Specifically, we used the Mishin et al. (1999) aluminum potential. It is converted in LAMMPS format by C. A. Becker (2008). The total potential energy of the system is represented as

$$
U=\frac{1}{2} \sum_{\alpha} \sum_{\substack{\beta \\ \beta \neq \alpha}} V\left(r^{\alpha \beta}\right)+\sum_{\alpha} B\left(\rho^{\alpha}\right) \tag{14}
$$

Here, $V$ is the pair potential which is a function of the distance $r^{\alpha \beta}$ between atoms $\alpha$ and $\beta$ and $B$ is the embedding energy which is a function of the atomic electron density $\rho$. The latter is given by

$$
\rho^{\alpha}=\sum_{\substack{\beta \\ \beta \neq \alpha}} \rho\left(r^{\alpha \beta}\right)
$$

In MD the atoms are treated as classical Newtonian particles. Thus, the total force on particle $\alpha$ is expressed as

$$
\boldsymbol{F}^{\alpha}=m_{a} \boldsymbol{a}^{\alpha}=\boldsymbol{F}^{\text {ext,} \alpha}+\boldsymbol{F}^{\text {int,} \alpha} \tag{15}
$$

Here, $m_a$ is the mass of each atom (note the difference between this and the state function defined previously as $m(x)$ in Eq. (3)) and $a^\alpha$ is the acceleration of atom $\alpha$. $\boldsymbol{F}^{\text{ext},\alpha}$ represents the external force acting on the atom due to external fields and atoms outside the system, while $\boldsymbol{F}^{\text{int},\alpha}$ represents the internal force arising from interactions with other atoms within the system. The internal force on atom $\alpha$ can be expressed as

$$
\boldsymbol{F}^{\text{int},\alpha} = \sum_{\substack{\beta \\ \beta \neq \alpha}} \boldsymbol{F}^{\alpha\beta} = -\frac{\partial}{\partial \boldsymbol{r}^\alpha} U
\tag{16}
$$

In the above the expression of potential energy ($U$) is substituted from Eq. (14). To evolve the fast dynamics of the sample LAMMPS uses the Velocity-Verlet (VV) algorithm LAMMPS Developers (2024a,b). Given, at fast time $\sigma$ the positions and velocities of the particles are $\boldsymbol{r}^\alpha(\sigma)$ and $\boldsymbol{v}^\alpha(\sigma)$, respectively. As discussed in Section 2.4, they form the state of the system. The steps of the algorithm are as follows:

- **Step 1: Calculate the velocity at fast time $\sigma + \frac{\Delta\sigma}{2}$**
  We calculate a half-step update to the velocities as

$$
\boldsymbol{v}^\alpha\left(\sigma + \frac{\Delta\sigma}{2}\right) = \boldsymbol{v}^\alpha(\sigma) + \frac{\boldsymbol{F}^\alpha(\boldsymbol{r}^\alpha(\sigma))}{m} \frac{\Delta\sigma}{2}
\tag{17}
$$

- **Step 2: Calculate the position at fast time $\sigma + \Delta\sigma$**
  We calculate a full-step update to the positions using the half-step update to the velocities as

$$
\boldsymbol{r}^\alpha(\sigma + \Delta\sigma) = \boldsymbol{r}^\alpha(\sigma) + \boldsymbol{v}^\alpha\left(\sigma + \frac{\Delta\sigma}{2}\right)\Delta\sigma
\tag{18}
$$

- **Step 3: Calculate the velocity at fast time $\sigma + \Delta\sigma$**
  Finally, we calculate one additional half-step update to the velocities as

$$
\boldsymbol{v}^\alpha(\sigma + \Delta\sigma) = \boldsymbol{v}^\alpha\left(\sigma + \frac{\Delta\sigma}{2}\right) + \frac{\boldsymbol{F}^\alpha(\boldsymbol{r}^\alpha(\sigma + \Delta\sigma))}{m} \frac{\Delta\sigma}{2}
\tag{19}
$$

### 2.4. Application of PTA to Molecular Dynamics

In this section, we discuss the application of PTA to a specific problem in which the fast dynamics is given by Molecular Dynamics, as discussed the previous section. This requires the identification of the load and fast variable, the state functions and the slow variable, which we discuss next.

#### 2.4.1. Problem Setup

A simulation box of constant volume is defined within which a sample of Aluminum with FCC lattice structure, with lattice parameter $a$ is created. The dimensions of the box are $B_x$, $B_y$ and $B_z$ (whose values are specified in Table 1) while that of the sample are $L_x$, $L_y$ and $L_z$, respectively, as shown in Fig. 1. In this work, we have used cubic samples, hence $L_x = L_y = L_z = L_s$, where $L_s$ is the size of the cubic sample, which ranges from $4\ nm$ to $30\ nm$, as specified in Table 1. Since the dimensions of the simulation box are much larger than those of the sample, they need not be changed during the deformation of the sample. Hence, the system is evolved using NVE ensemble (where V is the simulation box volume) with EAM potential as defined in Eq. (14). The global coordinate axes $x$, $y$, and $z$ are aligned along the lattice directions [100], [010], and [001] respectively of the sample. The MD box is subjected to fixed boundary condition in all directions. As shown in Fig. 2, we define the left boundary atoms of the sample as the set of atoms which belong to the left boundary region $\partial B_l = \{(x,y,z) \in \mathbb{R}^3 : 0 \leq x \leq a, 0 \leq y \leq L_y, 0 \leq z \leq L_z\}$. Similarly, the right boundary atoms of the sample are defined as the set of atoms which belong to the right boundary region $\partial B_r = \{(x,y,z) \in \mathbb{R}^3 : (L_x - a) \leq x \leq L_x, 0 \leq y \leq L_y, 0 \leq z \leq L_z\}$.

The state of the system comprises the set of atomic positions and velocities and is denoted as

$$
\begin{aligned}
s = \{\boldsymbol{r}^\alpha, \boldsymbol{v}^\alpha\} &= \left(\boldsymbol{r}^1, \boldsymbol{r}^2, ...., \boldsymbol{r}^n, \boldsymbol{v}^1, \boldsymbol{v}^2, ...\boldsymbol{v}^n\right) \\
&= \left(x^1, y^1, z^1, ..., x^n, y^n, z^n, v_x^1, v_y^1, v_z^1, ...v_x^n, v_y^n, v_z^n\right),
\end{aligned}
\tag{20}
$$

where the system consists of $n$ atoms and $\boldsymbol{r}^\alpha$ and $\boldsymbol{v}^\alpha$ are the position and velocity of atom $\alpha$. Thus, the state $s$ is a vector of size $6n$, where $n$ is the number of atoms in the system. The state $s$ evolves on the fast time scale $\sigma$, hence it is denoted as $s(\sigma)$. This serves as the fast variable in our work, similar to $x(\sigma)$ in Section 2.1 and 2.2. The load $l(t)$ corresponds to the applied displacement on the system under quasi-static loading rate. A detailed discussion on the boundary conditions is provided next.

![](./images/1238105616166158359_1.jpg)

Figure 1: MD Box and Sample.

![](./images/1238105616166158359_2.jpg)

Figure 2: Boundary conditions (BCs) applied on the sample corresponding to uniaxial tension/compression in the
$x$ direction. To obtain the converged running time average $R_{t}^{m}$ at slow time $t$, MD is run with the left boundary
atoms $\partial B_{l}$ fixed at zero displacement while the right boundary atoms $\partial B_{r}$ are fixed at $u_{x}(t)=\varepsilon(t)L_{s}=\dot{\varepsilon}tL_{s}$ while
$u_{y}=u_{z}=0$, where $\dot{\varepsilon}$ is the applied strain rate and $t$ is the slow time.

### 2.4.2. Boundary conditions

In this section, we discuss the boundary conditions applied to the sample at different stages of the simulation.
Fig. 2 shows the boundary conditions applied to the sample. The left and right boundary atoms, $\partial B_{l}$ and $\partial B_{r}$,
and the corresponding constraints on the atomic positions, velocities, and forces are indicated. First, we generate
the initial state $s(-\Delta)$. The initial positions of the atoms are the lattice positions; velocities are initialized from a
Maxwell-Boltzmann distribution corresponding to the temperatures $T_{0}$. During this step, the left boundary atoms

are fixed at their reference lattice positions by setting $\boldsymbol{v}^\alpha(\sigma) = \mathbf{0}$, $\boldsymbol{F}^\alpha(\sigma) = \mathbf{0}$. Note that this is the standard procedure to fix atoms in LAMMPS, unlike in mechanics, where we cannot simultaneously specify both velocity and force. However, setting $\boldsymbol{v}^\alpha(\sigma) = \mathbf{0}$, $\boldsymbol{F}^\alpha(\sigma) = \mathbf{0}$ in Eq. (17)-(19) ensures that the position $\boldsymbol{r}^\alpha(\sigma)$ for atom $\alpha$ which belongs to the left boundary $\partial B_l$ remains unchanged during the Velocity-Verlet update in MD. (some comment that this actually implements the mechanics correctly should be added - Jerry/Sabyasachi) while the right boundary atoms are allowed to move freely in the $x$ direction until the resultant reaction force on the right boundary atoms in the $x$ direction, $R_x(\sigma)$, vanishes. The sample thus undergoes thermal relaxation to achieve an initial stress-free state.

After thermal relaxation, the simulation proceeds by a combination of two steps. Mechanical loading is applied to the sample corresponding to the applied strain rate and the slow time. After the load is applied, the right boundary atoms are fixed at that displacement, and the running time average of the state functions is calculated. The steps we followed are summarized below:

1. We first displace the right boundary atoms to $u_x(t-\Delta) = \dot{\epsilon}(t-\Delta)L_s$ and then fix them at that position (by setting $\boldsymbol{v}^\alpha(\sigma) = \mathbf{0}$, $\boldsymbol{F}^\alpha(\sigma) = \mathbf{0}$, similar to the procedure used to fix the left boundary atoms as discussed above). At time $t-\Delta$, we run MD simulations until $R_{t-\Delta}^m$ converges, following Eq. (5).

2. We then displace the right boundary atoms by $u_x(t-\frac{\Delta}{2}) - u_x(t-\Delta) = \dot{\epsilon}\frac{\Delta}{2}L_s$ and fix them at that position. At time $t-\frac{\Delta}{2}$, we run MD simulations until $R_{t-\frac{\Delta}{2}}^m$ converges, following Eq. (5).

3. We then displace the right boundary atoms by $u_x(t) - u_x(t-\frac{\Delta}{2}) = \dot{\epsilon}\frac{\Delta}{2}L_s$ and fix them at that position. At time $t$, we run MD simulations until $R_t^m$ converges, following Eq. (5).

4. We calculate the rate of change of the slow variable using Eq. (6), and obtain the extrapolated value $v^m(t+h)$ using the extrapolation rule in Eq. (7). Finally, we displace the right boundary atoms by $u_x(t+h-\Delta)-u_x(t) = \dot{\epsilon}(h-\Delta)L_s$.

5. We similarly fix the right boundary atoms at that position corresponding to $t+h-\Delta$, $t+h-\frac{\Delta}{2}$, and $t+h$. Using the initial guess for the state as defined in Eq. (13), we run MD until convergence to calculate $R_{t+h-\Delta}^m$, $R_{t+h-\frac{\Delta}{2}}^m$, and $R_{t+h}^m$, respectively, following Eq. (5).

6. We then compare the value of the slow variable $v_d^m(t+h)$ calculated using Eq. (9) with the extrapolated value of the slow variable at slow time $t+h$. We accept the measure if the two values are close to each other, up to a specified tolerance, using Eq. (11).

7. If the values of the slow variables are different, we check if there is a jump in the measure using Eq. 11. If there is a jump in the measure, we discard v obtained using the extrapolation rule in Eq. (7) and set the value of the slow variable as the value $v_d^m$ obtained using Eq. (9).

8. We then proceed to the next slow time $t+h$, where $h$ is the jump-size in slow time, and repeat the above steps.

### 2.4.3. State functions and slow variables

The state functions (denoted as $m$ in the discussion following Eq. (3)) that we choose in our work are the instantaneous kinetic energy $K(\sigma)$, potential energy $U(\sigma)$ and normal stress (obtained as resultant reaction force divided by the cross-sectional area) in the $x$ direction, $T_x(\sigma)$, which are defined as

$$
K(\sigma) = \frac{1}{2} \sum_{\alpha=1}^n m_\alpha \boldsymbol{v}^\alpha(\sigma) \cdot \boldsymbol{v}^\alpha(\sigma)
$$

$$
U(\sigma) = \frac{1}{2} \sum_{\alpha=1}^n \sum_{\substack{\beta \\ \beta \neq \alpha}} V(r^{\alpha\beta}(\sigma)) + \sum_{\alpha} B(\rho^\alpha(\sigma)) \tag{21}
$$

$$
T_x(\sigma) = \frac{\boldsymbol{R}(\sigma) \cdot \hat{\boldsymbol{e}}_x}{A_0} = \frac{\left(- \sum_{\alpha \in \partial B_r} \boldsymbol{F}^{int,\alpha}(\sigma)\right) \cdot \hat{\boldsymbol{e}}_x}{L_s^2}.
$$

The forms of the potential energy of the system $U(\sigma)$ and the internal force $\boldsymbol{F}^{int,\alpha}(\sigma)$ on atom $\alpha$ have been discussed previously in Eq. (14) and Eq. (16) respectively. The right boundary region $\partial B_r$ is defined in Section 2.4.1. Note that the state functions depend on the state $s(\sigma)$ as defined above in Eq. (20) through the set of atomic positions $\boldsymbol{r}^\alpha$ and atomic velocities $\boldsymbol{v}^\alpha$.

The slow variables (denoted as $\mathrm{v}_m$ in Eq. (3)) corresponding to the state functions defined in Eq. (21) in this work are $\mathrm{v}_K(t)$, $\mathrm{v}_U(t)$ and $\mathrm{v}_{T_x}(t)$. For simplicity, hereafter we denote them with overhead bars as $\overline{K}$, $\overline{U}$ and $\overline{T}_x$ and refer to them as averaged kinetic energy, averaged potential energy and averaged normal stress respectively.

In addition to the slow variables defined above, we also track the average atomic positions of each atom in the system to visualize the evolution of the microstructure at different slow times $t$. The averaged position of atom $\alpha$ is calculated as

$$
\vec{r}^{\alpha}(t)=\frac{1}{N_{t}} \sum_{i} \boldsymbol{r}^{\alpha}\left(\sigma_{i}\right),
\tag{22}
$$

where $N_{t}$ is defined in the discussion following Eq. (5). Note that $\vec{r}^{\alpha}(t)$ is not evolved as a slow variable (and neither is it the same as $\mathrm{v}_{\mu^{\alpha}}$) but is only meant for the purpose of visualization of a measure of a type of averaged atomic positions and dislocation microstructure in slow time.

## 3. Results

Table 1: *Simulation parameters.*

<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Description</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$a$</td>
      <td>Lattice parameter of aluminum</td>
      <td>$4.05$ Å</td>
    </tr>
    <tr>
      <td>$\Delta\sigma$</td>
      <td>MD timestep</td>
      <td>1 femtosecond</td>
    </tr>
    <tr>
      <td>$B_x \times B_y \times B_z$</td>
      <td>Dimension of box</td>
      <td>$202.5\ nm \times 90\ nm \times 90\ nm$</td>
    </tr>
    <tr>
      <td>$L_s$</td>
      <td>Size of cubic sample</td>
      <td>$4$ to $30\ nm$</td>
    </tr>
    <tr>
      <td>$\Delta$</td>
      <td>Time interval in Eq. (3)</td>
      <td>$h/5$</td>
    </tr>
    <tr>
      <td>$N_{\text{max}}$</td>
      <td>Maximum MD runs to check for convergence</td>
      <td>$50 \times 10^3$</td>
    </tr>
    <tr>
      <td>$tol_m$</td>
      <td>Tolerance for convergence check in Eq. (A.2)</td>
      <td>$5\%(\overline{U},\overline{K},\overline{R_x})$</td>
    </tr>
    <tr>
      <td>$tol_j$</td>
      <td>Tolerance for jump check in Eq. (11)</td>
      <td>$1\%(\overline{U}),8\%(\overline{K}),5\%(\overline{R_x})$</td>
    </tr>
    <tr>
      <td>$tol_v$</td>
      <td>Tolerance for acceptance of measure in Eq. (24)</td>
      <td>$5\%(\overline{U}),1\%(\overline{K}),1\%(\overline{R_x})$</td>
    </tr>
  </tbody>
</table>

### 3.1. Uniaxial tension test

In this section, we discuss the results for uniaxial tension simulations performed on samples of sizes 4, 8, 20, 25 and $30\ nm$. The boundary conditions are described in Figure 2 and we have used the applied strain rate of $10^{-3}\ s^{-1}$.

- **Evolution of averaged kinetic energy, averaged potential energy, and averaged normal stress:** The evolution of the slow variables - averaged potential energy $\overline{U}$, averaged kinetic energy $\overline{K}$ and averaged normal stress $\overline{T}_x$ along with the relative errors between these quantities and the corresponding values obtained from the measure, $\overline{U}_d$, $\overline{K}_d$, and $\overline{T}_{d_x}$, for the 8 nm sample are shown in Fig. 3, 4, and 5, respectively. We observed that the relative error for all the slow variables are within $5\%$ at all strains.

The increase in potential and kinetic energy due to application of mechanical load is visible. This is expected as energy is supplied to the system which leads to bond stretching (increase of potential energy) and increased lattice vibrations (increase of kinetic energy). The stress strain curve has an elastic part up to around $5\%$ strain at which point dislocation nucleation and motion occurs. The resulting lattice waves lead to a sudden increase in kinetic energy. It also causes slip and plastic deformation and hence the stress-strain curve drops suddenly. Thus, dislocation nucleation events have a distinct signature in our simulations on slow time scales when the invariant measures jump, which is further reflected as jumps in the slow variables. Once dislocations exit the free-surface, the stress rises again due to dislocation starvation, followed by subsequent drop. These serrations are a characteristic feature of uniaxial tension and compression of samples of sizes ranging from a few nanometers to tens of nanometers (the sample sizes in this work range from $4\ nm$ to $30\ nm$).

The yield stress of around 5 GPa is reasonable since we are starting from a defect-free sample and homogeneous nucleation of dislocations is expected. The theoretical shear stress for the same is $G/10=2.5\ GPa$ (where $G=25\ GPa$ is the shear modulus of Aluminum) Frenkel (1926). The shear stress multiplied with the Schmid Factor $\sqrt{6}$ (for $\{111\}<110>$ slip systems in FCC crystal under uniaxial tension) gives around $6\ GPa$, which is close to our model prediction.

However, the primary contribution and key novelty of our approach is that the stress-strain curve shown till a strain of $20\ \%$ is obtained with applied strain rate of $10^{-3}/s$, which is almost 10 orders of magnitude smaller than the conventional rates applied in MD simulations. This is important for studying the mechanical response of samples at quasi-static loading rates using MD. To the best of our knowledge, MD simulations using such small rates and up to high strains have not been conducted yet.

Another significant improvement is that the size effect that we observe does not involve calibration of any fitting parameter and instead is an emergent behaviour that is caused by the underlying microstructure evolution on the scale of applied loading at quasistatic loadng rates.

![](./images/1238105616166158359_3.jpg)

Figure 3: Evolution of averaged potential energy ($\overline{U}$) and its relative error ($e^{\overline{U}}$) with strain ($\epsilon_x$) for 8 nm sample in uniaxial tension. $L_s$ in the y-axis denotes the size of the sample.

![](./images/1238105616166158359_4.jpg)

Figure 4: Evolution of averaged kinetic energy ($\overline{K}$) and its relative error ($e^{\overline{K}}$) with strain ($\epsilon_x$) for 8 nm sample in uniaxial tension.

- **Effect of sample size on the stress–strain curve:** To ensure statistical reliability, five simulations results with different initial atomic velocity distributions are performed for both 8 nm and 20 nm blocks. For each block size, the mean of these simulation results is used to analyze the size effect. The corresponding stress–strain curves are shown in Figure 6. Under the same loading conditions, the 8 nm block exhibits a higher stress response than the 20 nm block, indicating a pronounced size effect. Size effect in micron to submicron sized samples has been widely reported in micropillar compression tests and torsion tests of nanowires Uchic et al. (2004) It is caused by the limited availability of dislocation sources in smaller samples, which also require higher stress to nucleate. Secondly, the strain gradients in smaller samples are higher, which leads to the generation of Geometrically Necessary Dislocations (GNDs) to maintain lattice compatibility. GNDs are a source of hardening in metals. The size effect observed in our simulations agrees qualitatively with the experimental results of Uchic et al. (2004), discussed later in Section 3.5.

- **Effect of size on standard deviation of mean stress:** We carry out five simulations with different initial atomic velocity distributions for both 8 nm and 20 nm blocks. At a certain strain value, the mean and standard deviation of stress across those simulations are then calculated for both sizes. In Figure 7, we show the variation of the standard deviation of stress for different sizes. It can be observed that the smaller 8 nm block shows a higher standard deviation compared to the larger 20 nm block. To quantify this, we

![](./images/1238105616166158359_5.jpg)

Figure 5: Evolution of averaged normal stress $(\overline{T}_x)$ and its relative error $(e^{\overline{T}_x})$ with strain $(\epsilon_x)$ for 8 nm sample in uniaxial tension.

![](./images/1238105616166158359_6.jpg)

Figure 6: Evolution of averaged normal stress $(\overline{T}_x)$ with strain $(\epsilon_x)$ for different sample sizes under uniaxial tension.

calculate the mean of the standard deviation. The values are 0.3549 GPa and 0.2188 GPa for the 8 nm and 20 nm sizes, respectively. After yielding, the shaded regions corresponding to the 8 nm and 20 nm sizes appear to overlap. The higher standard deviation for smaller sample is reasonable. In smaller samples, fewer dislocations are nucleated and once nucleated, they exit the surface quickly, followed by a period of dislocation starvation, leading to pronounced serrations. However, in larger samples, higher number of dislocations are present at any given time (post-yielding), hence dislocation nucleation and exit events do not have such pronounced effect on the stress-strain curve.

- **Effect of size on the tensile properties of the sample:** We performed uniaxial tension tests on samples of various sizes $L_s = \{4, 8, 20, 25, 30\}$ nm to understand the effect of sample size on the mechanical properties of the material. We then fit a linear curve to the stress-strain data in the 0 to 1 % strain range and the slope of this fitted line is taken as the Young's modulus $(E)$. The yield strength $(\sigma_{ys})$ is taken as the value of the averaged normal stress $(\overline{T}_x)$ at which the first dislocation nucleation in slow time is observed. This is done by tracking the mean atomic positions of every atom calculated using Eq. (22). Figure 8a shows the elastic modulus plotted as a function of size. It is observed that the Young's modulus decreases significantly as the size increases. Similarly, Figure 8b shows the variation of yield strength with size, indicating a decreasing trend with increasing sample size.

The increase in Young's modulus with decreasing sample size is because of the increase in the surface to volume ratio. Surface atoms have higher stiffness compared to bulk atoms, which increases the Young's modulus. The decrease in yield strength with increasing sample size is because larger samples have more surface area, and hence higher number of potential sites for dislocation nucleation (which are usually parts of

![](./images/1238105616166158359_7.jpg)

Figure 7: Evolution of mean and standard deviation of $\overline{T}_x$ across different runs corresponding to different initial velocity distributions and for different sample sizes with strain $(\epsilon_x)$. The mean averaged stress $\mu(\overline{T}_x)$ is marked using the solid curve while the shaded envelope around it shows the range of $\mu(\overline{T}_x) \pm \sigma(\overline{T}_x)$, where $\sigma(\overline{T}_x)$ is the standard deviation of the averaged stress.

the sample with higher local stress concentration such as edges and corners), compared to smaller samples. Although done for very different sample sizes, the trends observed in our simulation results align with the experimental observations of Uchic et al. (2004), discussed later in Section 3.5.

![](./images/1238105616166158359_8.jpg)

(a) Variation of Young's modulus $(E)$ with sample size $(L_s)$.
(b) Variation of Yield strength $(\sigma_{ys})$ with sample size $(L_s^{-1/2})$.

Figure 8: Dependence of mechanical properties on sample size.

- **Effect of initial state of system on the stress-strain curve:** We carry out five simulations with different initial atomic velocity distributions at the same initial temperature of $T_0 = 300\ K$ for the $8\ nm$ and $20\ nm$ blocks, each. In Fig. 9, we have shown the variation of stress response for different initial states of the system. It is observed that although the initial temperature of the system remains the same, different ini- tial velocity distributions of atoms lead to variation in stress response. This is the primary reason for the stochasticity of the response observed in our simulations. As observed and discussed previously, a smaller sample size leads to harder responses and higher serrations in the stress-strain curve.

- **Effect of applied strain rate on stress-strain curve:** We perform uniaxial tension simulations on the 20 nm block under applied strain rates of $10^{-4}\ s^{-1}$ and $10^{-3}\ s^{-1}$. Figure 10 shows the variation of stress with the applied strain rate. It is observed that although the elastic slopes are nearly identical, the plastic deformation behavior, governed by dislocation nucleation and evolution, depends on the applied strain rate. In particular, the stress levels after yielding remain consistently above those at a lower strain rate.

At higher strain rates, the material has less time for dislocations to nucleate and move, so higher stresses are required to activate plastic deformation mechanisms. Conversely, at lower strain rates, dislocations have

![](./images/1238105616166158359_9.jpg)

Figure 9: Averaged normal stress ($\overline{T}_x$) with strain ($\epsilon_x$) with different initial atomic velocity and same temperature for different sample sizes under uniaxial tension.

more time to multiply and glide, leading to lower flow stresses. Plastic deformation involves overcoming energy barriers for dislocation nucleation and motion. Faster deformation (higher strain rate) means less time for thermal fluctuations to assist these processes, requiring larger applied stresses.

![](./images/1238105616166158359_10.jpg)

Figure 10: Evolution of averaged normal stress ($\overline{T}_x$) with strain ($\epsilon_x$) for 20 nm sample under uniaxial tension with different applied strain rates of $10^{-4}\ s^{-1}$ and $10^{-3}\ s^{-1}$.

- Effect of initial sample temperature on stress-strain curves:

We initialize the atomic velocities corresponding to different initial temperatures. For each initial temperature, we run 3 simulations from different initial velocity distribution corresponding to the same initial temperauture. The evolution of the mean kinetic energy and mean potential energy from the 3 simulations for each initial temperature are shown in Fig. 11a and Fig. 11b respectively. It is evident that there is a rise in both kinetic and potential energy with increasing initial temperature, at almost all strain values. The rise in kinetic energy is due to the increased initial kinetic energy supplied to the system at higher temperature. The rise in potential energy is because atoms vibrate at larger distance from their mean position due to increased kinetic energy. Fig. 12 shows the evolution of the stress (averaged over 3 simulations for each initial temperature) with strain. The initial yielding occurs at lower stress with increasing temperature as expected. Till about 7.5% strain, the stress-strain curves show a drop with increasing temperature. However, at higher strains, the serrations due to stochasticity of dislocation motion and exit, particularly for smaller samples, cause stress at the same strain to lower at some strains with lowering of the initial temperature. Hence the serrations dominate over the effect of increased atomic vibrations at higher strains.

- Evolution of the microstructure: Tracking the evolution of averaged atomic positions at different slow times allows us to visualize the evolution of the dislocation microstructure in slow time. The dislocation

![](./images/1238105616166158359_11.jpg)

![](./images/1238105616166158359_12.jpg)

Figure 11: Evolution of averaged kinetic ($\overline{K}$) and potential ($\overline{U}$) energy (each curve represents the mean over 3 different simulations for the same initial temperature) with strain for different initial temperatures for 8 nm sample in uniaxial tension.

![](./images/1238105616166158359_13.jpg)

Figure 12: Evolution of averaged normal stress ($\overline{T}_x$) (each curve represents the mean over 3 different simulations for the same initial temperature) with strain for different initial temperatures for 8 nm sample in uniaxial tension.

microstructure at different strains for a 20 nm sample are generated using Dislocation Analysis DXA in OVITO software Stukowski (2010), as shown in Fig. 13. We observe that dislocations nucleate for the first time at 6.5 % strain and the dislocation network evolves with applied strain. The networks consists of predominantly Shockley partials and Stair-rod dislocations. Dislocations exit the free surface and this leads to creation of slip steps, which can be seen particularly in Fig. 13c and Fig. 13d.

Fig. 14 show the mean atomic positions at 7 % strain. A defective zone of the crystal is zoomed in to show plastic deformation. Fig. 15 shows the atoms in colors which are categorized into FCC, HCP and other crystal structures (using DXA analysis in OVITO). Only FCC atoms are in their perfect lattice positions while the HCP and other atoms are out of their regular lattice positions, caused by plastic deformation due to dislocation motion.

### 3.2. Uniaxial compression test

Since compression tests are more common for micron sized samples, we have performed uniaxial compression tests on samples of sizes of 8 and 20 nm blocks to demonstrate the applicability of our method. We have used the applied strain rate of $(-10^{-3})~s^{-1}$.

- **Evolution of averaged kinetic energy, averaged potential energy and averaged normal stress**: The evolution of the slow variables - averaged potential energy $\overline{U}$, the averaged kinetic energy $\overline{K}$ and the averaged normal stress $\overline{T}_{xx}$ and the relative errors between them and the corresponding values of the measure $\overline{U}_d$, $\overline{K}_d$ and $\overline{T}_{d_{xx}}$ for 8 nm sample are shown in Fig. 16, 17 and 18 respectively. We observed that the relative error for the slow variables, averaged potential energy, averaged kinetic energy and averaged normal stress are within 1%, 8% and 5%, respectively at all strains. A discussion on the physical reasoning behind these observations is provided in Section 3.1.

![](./images/1238105616166158359_14.jpg)

(a) $6.5\%$ strain.

![](./images/1238105616166158359_15.jpg)

(b) $13\%$ strain.

![](./images/1238105616166158359_16.jpg)

(c) $13.5\%$ strain.

![](./images/1238105616166158359_17.jpg)

(d) $14.5\%$ strain.

Figure 13: Evolution of dislocation microstructure in slow time, under uniaxial tension at different strains for $20 nm$ sample. Different types of dislocations are indicated using the colors shown in the legend. The slip steps created by exiting dislocations can be observed clearly at higher strains.

- **Effect of sample size on the stress-strain curve:** To ensure statistical reliability, five and four simulations with different initial atomic velocity distributions are performed for the $8 nm$ and $20 nm$ blocks, respectively. For each sample size, the mean of the stress-strain curves are shown in Figure 19. Under the same applied loading rate, the $8 nm$ sample exhibits a higher stress response than the $20 nm$ sample, indicating a pronounced size effect. The discussion on the cause of size effect is provided in Section 3.1. However, we observe that the elastic slope in compression is not dependent on the sample size, unlike in the tension case presented earlier. The yield stress of around $4 GPa$ is also lower than than $5 GPa$ which is observed in uniaxial tension. The stress-strain response is also softer in compression compared to tension as upon comparison of Fig. 6 and Fig. 19. In general, a specimen is more stable in tension than compression because buckling (in slender specimens) and barrelling instabilities are avoided in the latter case. Although the sample sizes differ, the trends observed in our simulations are in qualitative agreement with the experimental observations of Uchic et al. (2004), as discussed later in Section 3.5.

- **Effect of size on standard deviation of mean stress:** We carry out four and three simulations with different initial atomic velocity distributions for the $8 nm$ and $20 nm$ blocks, respectively. At a certain strain value, the mean and standard deviation of stress across those simulations are then calculated for both sizes. In Figure 20, we show the variation of the standard deviation of stress for different sizes. It can be observed that the smaller $8 nm$ sample shows a higher standard deviation compared to the larger $20 nm$ block. To quantify this, we calculate the mean of the standard deviation. The values are $0.4285 GPa$ and $0.1087 GPa$ for the $8 nm$ and $20 nm$ sizes, respectively. A justification for this size effect is provided in Section 3.1.

![](./images/1238105616166158359_18.jpg)

Figure 14: Mean atomic positions at 7 % strain for 20 nm sample in uniaxial tension. A defective zone of the sample is zoomed in to show slip and plastic deformation.

![](./images/1238105616166158359_19.jpg)

Figure 15: Mean atomic position at 7 % strain for 20 nm sample in uniaxial tension. Atoms are colored as FCC, HCP or others. Only FCC atoms in green are at their regular lattice positions. Atoms which are not in their regular lattice positions such as the HCP atoms in red and other atoms in white result from slip caused by dislocation motion. A defective zone of the crystal is zoomed in to show the atoms which are out of their lattice positions.

- **Effect of the initial state of the system on the stress-strain curve:** We carry out four simulations with different initial atomic velocity distributions at same initial temperature of $T_0 = 300$ K for the 8 nm and 20 nm blocks, each. In Fig. 19 we have shown the variation of stress response for different initial state of the system. It is observed that although the initial temperature of the system remains the same, different initial velocity distributions of atoms lead to variation in stress response, similar to our observation in uniaxial tension case.

- **Evolution of the microstructure:** The dislocation microstructure at different strains, generated using Ovito as mentioned earlier, are shown in Fig. 22. We observe that dislocations nucleate for the first time at 3% strain and the dislocation network evolves with applied strain. The networks consists of predominantly Shockley partials along with some Hirth, Stair-rod and full (Perfect) dislocations.

Fig. 22 show the mean atomic positions at 5% strain. A defective zone of the crystal is zoomed in to show plastic deformation. Fig. 23 shows the mean positions of atoms for a 20 nm sample under uniaxial

![](./images/1238105616166158359_20.jpg)

Figure 16: Evolution of averaged potential energy ($\overline{U}$) and relative error ($\epsilon^{\overline{U}}$) with strain ($\epsilon_x$) for 8 nm sample under uniaxial compression. $L_s$ in the y-axis denotes the size of the sample.

![](./images/1238105616166158359_21.jpg)

Figure 17: Evolution of averaged kinetic energy ($\overline{K}$) and relative error ($\epsilon^{\overline{K}}$) with strain ($\epsilon_x$) for 8 nm sample under uniaxial compression.

![](./images/1238105616166158359_22.jpg)

Figure 18: Evolution of averaged normal stress ($\overline{T}_x$) and relative error ($\epsilon^{\overline{T}_x}$) with strain ($\epsilon_x$) for 8 nm sample under uniaxial compression.

compression at different values of strain. We observe that at sufficiently large strains ($\approx 11\%$ in this case), the sample changes its state and undergoes liquefaction, which is not observed in the case of uniaxial tension. Fig. 24 shows the atoms in colors which are categorized into FCC, HCP and other crystal structures (using

![](./images/1238105616166158359_23.jpg)

Figure 19: Evolution of averaged normal stress $(\overline{T}_{x})$ with strain $(\epsilon_{x})$ for different sample sizes under uniaxial compression.

![](./images/1238105616166158359_24.jpg)

Figure 20: Evolution of mean and standard deviation of $\overline{T}_{x}$ across different runs corresponding to different initial velocity distributions and for different sample sizes with strain $(\epsilon_{x})$. The mean averaged stress $\mu(\overline{T}_{x})$ is marked using the solid curve while the shaded envelope around it shows the range of $\mu(\overline{T}_{x}) \pm \sigma(\overline{T}_{x})$, where $\sigma(\overline{T}_{x})$ is the standard deviation of the averaged stress.

![](./images/1238105616166158359_25.jpg)

Figure 21: Averaged normal stress $(\overline{T}_{x})$ with strain $(\epsilon_{x})$ for different sample sizes with different initial atomic velocity and same temperature. Curves labeled 1–4 in brackets represent independent simulations for the same sample size but with different initial atomic velocity distributions. Blue curves correspond to the 8 nm sample, while red curves correspond to the 20 nm sample.

DXA analysis in OVITO). Only FCC atoms are in their perfect lattice positions while the HCP and other atoms are out of their regular lattice positions, similar to our observation for the tension case presented earlier.

![](./images/1238105616166158359_26.jpg)
(a) 3 % strain.

![](./images/1238105616166158359_27.jpg)
(b) 4 % strain.

![](./images/1238105616166158359_28.jpg)
(c) 5.5 % strain.

![](./images/1238105616166158359_29.jpg)
(d) 9 % strain.

Figure 22: Evolution of dislocation microstructure in slow time, at different strains for 20 nm sample under uniaxial compression. Different types of dislocations are indicated using the colors shown in the legend.

### 3.3. Speedup in compute time

The speedup $S$ in computer time between the pure MD and PTA calculations is calculated as follows. Let $T_f^{CPU}$ and $T_{PTA}^{CPU}$ be the compute time to reach strain $\epsilon_f$ and $\epsilon_{PTA}$ using pure MD and PTA, respectively. The speedup $S$ is defined as:

$$
S = \frac{\left( \frac{T_f^{CPU}}{\epsilon_f} \right)}{\left( \frac{T_{PTA}^{CPU}}{\epsilon_{PTA}} \right)}. \tag{23}
$$

We have run MD using PTA and pure MD on an $8\ nm$ sample. The compute time for pure MD ($T_f^{CPU}$) to reach a strain of $6 \times 10^{-11}\%$ strain at an applied strain rate of $10^{-3}\ s^{-1}$ is 43290 seconds. In comparison, it took

![](./images/1238105616166158359_30.jpg)

Figure 23: Mean atomic positions at 5 % and 11 % strain for 20 nm sample under uniaxial compression.

![](./images/1238105616166158359_31.jpg)

Figure 24: Mean atomic position at 5 % strain for 20 nm sample under uniaxial compression. Atoms are colored as FCC, HCP or others. Only FCC atoms in green are at their regular lattice positions. Atoms which are not in their lattice positions such as the HCP atoms in red and other atoms in white result from slip caused by dislocation motion. A defective zone of the crystal is zoomed in to show the atoms which are out of their lattice positions.

a compute time ($T_{PTA}^{CPU}$) of 3268 seconds for PTA calculations to reach slow time 0.5% strain at the same applied strain rate. The speed up $S$ in compute time between the the two methods, as defined in Eq. (23) comes out to be:

$$
S = \frac{\left( \frac{46290}{6 \times 10^{-11}} \right)}{\left( \frac{3268}{0.5} \right)} = 11.95 \times 10^8 .
$$

This shows that PTA is significantly faster than pure MD for the problem. Note that this is a very conservative estimate of the speedup since MD is run only till very small strain, while starting from a defect-free state. In this regime, the lattice structure is close to that of a perfect crystal and only mild lattice stretching is observed. At higher strains, the dynamics is much more computationally expensive due to generation and evolution of defects. This means the compute time for pure MD is expected to increase even more compared to PTA at higher strains.

This makes reaching large strains using pure MD alone practically impossible. However, the increase in compute time for PTA will not be significant since it involves only running short bursts of MD.

### 3.4. Verification with fine dynamics
In this section, we demonstrate a verification of the evolution of the slow variable $\mathrm{v}_m$ with PTA using Eq. (7) (which we denote as $\mathrm{v}_m^{PTA}$ in this section) by comparing it to the value of the slow variable $\mathrm{v}_d^{m,fine}$ using Eq. (8) obtained by running the fine dynamics for the entire slow time interval of the simulation (which we denote as $\mathrm{v}_d^{m,fine}$). Note that $\mathrm{v}_d^{m,fine}$ is different from $\mathrm{v}_d^m$ used in PTA to accept the measure in Step 3 of Section 2.2. The calculation of $\mathrm{v}_d^{m,fine}$ does not involve approximations such as the usage of Simpson's rule in Eq. (9) and, more importantly, the fine initial guesses as described in Step 4 of Section 2.2. Hence, the evolution of $\mathrm{v}_d^{m,fine}$ is the exact evolution of the slow variable in the slow time interval that is considered for this verification, corresponding to an MD trajectory. Since the applied strain rate is in the quasi-static regime, we can only reach a very small strain range using the fine dynamics. It is due to the difficulty associated with running MD over large strains that a direct verification with fine dynamics over large strains with PTA results is currently not possible. We consider an 8 nm sample and apply uniaxial tensile loading for this verification. We divide the discussion into two parts. In Section 3.4.1, we load the sample from a defect-free initial state, while in Section 3.4.2, we load the sample from a defective initial state. The defect-free initial state corresponds to the pre-yield regime, whereas the defective state corresponds to the post-yield regime. We then calculate the relative error between the two using the following:

$$
Error, \mathrm{v}(t)=\left|\frac{\mathrm{v}_m^{PTA}(t)-\mathrm{v}_d^{m,fine}(t)}{\mathrm{v}_d^{m,fine}(t)}\right|. \tag{24}
$$

The error as defined above includes the component of the error arising due to the fine initial conditions used to calculate $\mathrm{v}_m^{PTA}$ using PTA (as discussed in Step 4 of Section 2.2), since the fine initial condition used in the calculation of $\mathrm{v}_d^{m,fine}$ is exact as it is obtained by running the fine dynamics in the entire slow time interval.

#### 3.4.1. Defect-free initial-state
The evolution of the relative errors of the slow variables—namely, the averaged potential energy $\overline{U}^{PTA}$, the averaged kinetic energy $\overline{K}^{PTA}$, and the averaged normal stress $\overline{T}_x^{PTA}$—with respect to their corresponding fine-scale values $\overline{U}^{fine}$, $\overline{K}^{fine}$, and $\overline{T}_x^{fine}$, calculated using Eq. (24), for the 8 nm sample are summarized in Table 2. For the stress plot shown in Figure 5, we start from a state at 3.1 % strain, in the pre-yield regime, and load it under uniaxial tension. We observed that the relative error for the slow variables, averaged potential energy, averaged kinetic energy, and averaged normal stress, are within $5.87 \times 10^{-3}\ \%$, $0.78\ \%$, and $0.27\ \%$, respectively, at all points. This extremely small error indicates that the slow evolution with PTA using the guess for the fine initial conditions is in close agreement with that obtained by running the fine dynamics alone, for the strain range that we considered.

<table>
  <thead>
    <tr>
      <th>$MD\ steps (\times 10^7)$</th>
      <th>$Error, \overline{U}\ (\times 10^{-3})(\%)$</th>
      <th>$Error, \overline{K}\ (\%)$</th>
      <th>$Error, \overline{T}_x\ (\%)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>5.74</td>
      <td>0.77</td>
      <td>0.14</td>
    </tr>
    <tr>
      <td>1.0</td>
      <td>3.35</td>
      <td>0.44</td>
      <td>0.27</td>
    </tr>
    <tr>
      <td>1.5</td>
      <td>2.94</td>
      <td>0.39</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>2.0</td>
      <td>5.87</td>
      <td>0.78</td>
      <td>0.21</td>
    </tr>
  </tbody>
</table>

Table 2: Evolution of relative errors: $Error, \overline{U}$, $Error, \overline{K}$ and $Error, \overline{T}_x$ (in %) with MD steps for 8 nm sample in uniaxial tension, starting with a defect-free initial-state at 3.1 % strain.

#### 3.4.2. Defective initial-state
In this section, we evolve the same slow variables as discussed in Section 3.4.1, but we start the simulations with a defective state of the sample. For the stress plot shown in Figure 5, we start from a state at 8.1 % strain, in the post-yield regime, and load it under uniaxial tension. Here also we observed that the relative error for the slow variables, averaged potential energy, averaged kinetic energy, and averaged normal stress, are within $13.6{\times}10^{-3}\ \%$, $0.32\ \%$ and $0.74\ \%$, respectively, at all points, indicating that the slow evolution with PTA using the guess for the fine initial conditions is in close agreement with that obtained by running the fine dynamics alone, for the strain range that we considered. We have summarized them in Table 3

<table>
  <thead>
    <tr>
      <th>MD steps($\times 10^7$)</th>
      <th>$\text{Error}, \overline{U} (\times 10^{-3}) (\%)$</th>
      <th>$\text{Error}, \overline{K} (\%)$</th>
      <th>$\text{Error}, \overline{T}_x (\%)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>2.5</td>
      <td>0.19</td>
      <td>0.74</td>
    </tr>
    <tr>
      <td>1.0</td>
      <td>2.8</td>
      <td>0.21</td>
      <td>0.30</td>
    </tr>
    <tr>
      <td>1.5</td>
      <td>12.5</td>
      <td>0.32</td>
      <td>0.19</td>
    </tr>
    <tr>
      <td>2.0</td>
      <td>13.6</td>
      <td>0.23</td>
      <td>0.27</td>
    </tr>
  </tbody>
</table>

Table 3: Evolution of relative errors: $\text{Error}, \overline{U}$, $\text{Error}, \overline{K}$ and $\text{Error}, \overline{T}_x$ (in %) with MD steps for 8 nm sample in uniaxial tension, starting with a defective initial-state at 8.1 % strain.

### 3.5. Comparison with experimental results

In this section, we discuss the experimental results of Uchic et al. (2004) for comparison with our model predictions. They performed uniaxial compression tests on $Ni_3Al-Ta$ micropillars, which were fabricated directly on a bulk crystal using focused-ion beam (FIB) techniques. The samples were prepared in the size range of 0.5 to $20\ \mu\text{m}$ in diameter and tested using a conventional nanoindentation device equipped with a flat-punch indentation tip. They observed that the stress-strain curve become harder as the sample size decreases. We observe similar smaller is harder size effect in our simulation results, for both tension (in Fig. 6) and compression (in Fig. 19) cases. They also observed that increasing the diameter of the micropillars led to a decrease in flow stress. We observe similar inverse-relation between yield strength and sample size under uniaxial tension in Fig. 8b. The initial elastic slope of the stress-strain curve is not dependent on the sample size, which is consistent with our results for the uniaxial compression case in Fig. 19. One point to note is that the sample sizes considered in the experiments and in our simulations are around 2-3 orders of magnitude different. In the experimental work of Uchic et al. (2004), micron and submicron sized samples were tested while the samples used in our simulations are in the order of a few nanometers upto $20\ nm$. Thus, the dislocation nucleation mechanisms and the plastic deformation that follows in the two cases are different, which leads to much higher yield stress and harder response in our model predictions. Inspite of these differences, we still observed similar trends related to size effect in our results.

In order to compare the predictions with experiments conducted on larger samples which are relevant for engineering purposes, one possible approach is to fit the stress-strain data of samples (of size 0.1 micron or above, so that it can capture the operating dislocation mechanisms at those length scales) using our approach to a surrogate material model. This model can then serve as the constitutive model for upscaled Finite Element simulations, with sample sizes (possibly) orders of magnitude larger than that used in MD. However, there are challenges in coupling time-averaged data from microscopic models to macroscale plasticity models, owing to the vast separation in time-scales that govern the microscale and macroscale models. One such approach using time-averaged Discrete Dislocation Dynamics response serving as inputs to a mesoscale plasticity model (and the challenges therewith) is provided in our previous work Chatterjee et al. (2020); of relevance here is also the recent work Mielke et al. (2025). Although challenging, such coupled multiscale models have the potential of being truly predictive and microstructure sensitive.

### 4. Conclusion

Molecular dynamics (MD) simulations are performed to study the mechanical response of nanometer-sized single-crystal aluminum samples under uniaxial tension and compression at slow, realistic strain rates. Although our results cannot be directly validated with experiments, the predictions are in qualitative agreement. A summary of the predictions are listed below:

1. Serrations are observed in the stress-strain plots of the $8\ nm$ block under both uniaxial tension and compression. This behavior is due to the low surface-to-volume ratio of the $8\ nm$ block. In addition, an increase in internal potential energy is observed with increase in applied strain. This is because work is done on the sample during deformation. During instances where a drop in stress occurs, a sharp increase in kinetic energy is observed. This happens because dislocation nucleation and motion creates lattice waves. Moreover, dislocation nucleation correspond to very fast events which result in jumps even in an averaged quatity like the support of an invariant measures, which consequently result in jumps in the slow variables.

2. A significant size effect is observed in the tensile properties of the material. Both the yield strength and elastic modulus decrease as the sample size increases from $4\ nm$ and $30\ nm$. In this range, the yield strength dropped from $7.05\ GPa$ for $4\ nm$ sample to $2.62\ GPa$ for $30\ nm$ sample, while the elastic modulus decreased from $101.31\ GPa$ for $4\ nm$ sample to $68.39\ GPa$ for $30\ nm$ sample. As the sample size increases, the material

behavior transitions toward that of bulk aluminum, and the elastic modulus approaches values predicted by continuum models. The observed "smaller is stronger" behavior aligns with the experimental and modeling results in the literature for submicron sized samples.

3. The overall stress response beyond yielding is lower for the larger (20 nm) sample compared to the smaller (8 nm) sample. This occurs because, in smaller samples with a higher surface-to-volume ratio, dislocations can escape to the surface more easily, resulting in a higher stress response Moreover, the dislocation sources in smaller samples are limited and they activate at higher stresses, leading to harder response compared to larger samples. Prediction of mechanical behaviour and size effects of nanometer-sized samples at small strain-rates (at the scales employed in this work) is extremely challenging using existent approaches. Our method provides a viable alternative for conducting such studies.

Our approach is also a starting point for understanding behaviour of materials at a larger scale, where the mechanisms we observed may no longer be relevant. But our work in this paper is a test of methodol- ogy for the (smaller) scales that we have been able to explore. The algorithm used in our approach will remain unchanged even for larger samples. However, since the number of atoms will be much higher for such samples compared to the sizes we have considered, it will take significantly more computational re- sources (higher number of cores, efficient hardware architechture, increased wall-clock time) and optimized LAMMPS settings in order to do so.

4. The statistical variation in stress is smaller for the 20 nm block compared to the 8 nm block. The standard deviation of the stress-strain curve was 0.3549 GPa and 0.2188 GPa for the 8 nm and 20 nm samples un- der tension, and 0.4285 GPa and 0.1087 GPa under compression, respectively. This indicates that larger samples exhibit a smoother stress response compared to smaller samples.

5. Plastic deformation due to dislocation nucleation and evolution depends on the applied strain rate as ex- pected. The stress-strain curve corresponding to the higher strain rate remained consistently above that of the lower strain rate along the stress axis. This is because at higher strain rates, to reach the same strain the material has less time for dislocations to move, thereby leading to higher flow stress.

6. The simulations reveal the sensitivity of the system to its initial state of the system. Although the initial temperature of the sample is kept same, changing the initial atomic velocity distribution leads to variations in the stress-strain response, demonstrating the stochasticity in the response.

7. Our approach is able to predict the evolution of the microstructure of the sample in slow time by tracking the averaged position of every atom in the assembly. This allows us to identify the defective regions in the crystal with more plastic deformation.

8. We also observe the evolution of the dislocation microstructure at different strains in slow time and are also able to categorize them into different types, like Shockley partials, Stair-rod and full dislocations.

In order to validate the results with experiments, a possible approach is to fit the stress-strain data from micron- sized samples using our approach into a surrogate material model which will act as constitutive equation for upscaled FEM simulations on larger samples, as mentioned previously. However, such coupled, multiscale ap- proaches are challenging due to the significant separation in time-scales of the fast, microscopic dynamics and that of the mesoscale model under quasi-static strain rates. This will be a topic for future work.

Another future application of our method is in advanced structural materials like High Entropy Alloys, BCC refractory metal alloys and Mg Alloys, among others, for which traditional Crystal Plasticity Finite Element Method (CPFEM) has resulted in very limited success. The mechanics of dislocation and slip for such materials is complicated, which makes formulation of constitutive flow rules at slow strain rates very challenging. The mechanical response predicted using our approach does not involve phenomenological assumptions and is a direct outcome of the underlying microstructural evolution from time-averaged MD. Hence, it does not suffer from such limitations and may potentially prove to be useful for studying the plastic deformation of such materials. It may be used to predict response of new materials as a function of temperature, orientation and strain-rate from first principles and also for understanding complicated dislocation interactions in such materials at slow time scales. However, it is essential that the statistical/representative volume element (RVE) size used in MD to generate the surrogate material model must be of sufficient size (approximately 100nm or larger) in order to capture the dislocation microstructure evolution that occurs in the bulk of the material.

### CRediT authorship contribution statement

S.Baruah: Formal analysis, Investigation, Methodology, Validation, Visualization, Writing - original draft, Writing - review and editing; S.Chatterjee: Conceptualization, Investigation, Methodology, Project administra- tion, Resources, Supervision, Validation, Visualization, Writing - review and editing; A.Acharya: Conceptual- ization, Investigation, Methodology, Validation, Writing - review and editing; G.Wang: Investigation, Validation, Visualization, Software, Writing - review and editing. (AA and GW, please check and add anything if necessary.)

### Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Data Availability

Data will be made available on request.

### Acknowledgements

S.Baruah acknowledges the Institute Fellowship received from Indian Institute of Technology Delhi and the High Performance Computing facility at Indian Institute of Technology Delhi. S. Chatterjee acknowledges the New Faculty Seed Grant and Equipment Matching Grant received from Indian Institute of Technology Delhi, the financial support received from the Anusandhan National Research Foundation (ANRF, erstwhile SERB) via grant no. SRG/2022/001328 and the financial support received from the Department of Applied Mechanics at Indian Institute of Technology Delhi.

### Appendix A. Convergence criteria for the running time average of state function

We define $\hat{R}_s^m$ as the running time average of state function $m$ at slow time $s$, given as:

$$
\hat{R}_s^m(i) = \frac{1}{i} \sum_{i=1}^i m_i.
$$

The successive values of $m_i$ are obtained by running the fast dynamics with the initial conditions obtained from step 4. We denote $R_s^m$ as the converged value of $\hat{R}_s^m$, defined as:

$$
R_s^m = \frac{1}{N_s} \sum_{i=1}^{N_s} m_i, \tag{A.1}
$$

where $N_s$ denotes the number of fine steps required for $\hat{R}_s^m$ to converge upto a specified value of tolerance. The maximum value of $N_s$ is $N_{max}$ ($N_s < N_{max}$). We define the tolerance as

$$
e^m(i) = \left| \frac{\hat{R}_s^m(i) - \hat{R}_s^m(i - k)}{\hat{R}_s^m(i)} \right|. \tag{A.2}
$$

Here, $(i)$ and $(i - k)$ are step numbers in fast time. If $e^m(i) < tol_m$ we declare $R_s^m = \hat{R}_s^m(i)$ and $\hat{R}_s^m$ has converged at $N_s = i$. The values of $tol_m$ used for our simulation purposes are defined in Table. 1. In our problem, we have the state functions as $U(\sigma_i)$ and $R_x(\sigma_i)$. In the following figures, we have shown the plots of the state functions and their running time averages.

![](./images/1238105616166158359_32.jpg)
![](./images/1238105616166158359_33.jpg)

Figure A.25: Potential energy $(U)$ and its running time average $(\hat{R}_s^U)$.

![](./images/1238105616166158359_34.jpg)

Figure A.26: Reaction force $(R_x)$ and its running time average $(\hat{R}_s^{R_x})$.

## References

Acharya, A. and Roy, A. (2006). Size effects and idealized dislocation microstructure at small scales: Predictions of a phenomenological model of mesoscopic field dislocation mechanics: Part i. *Journal of the Mechanics and Physics of Solids*, 54(8):1687–1710.

Acharya, A. and Sawant, A. (2006). On a computational approach for the approximate dynamics of averaged variables in nonlinear ode systems: toward the derivation of constitutive laws of the rate type. *Journal of the Mechanics and Physics of Solids*, 54(10):2183–2213.

Arora, R. and Acharya, A. (2020a). Dislocation pattern formation in finite deformation crystal plasticity. *International Journal of Solids and Structures*, 184:114–135.

Arora, R. and Acharya, A. (2020b). A unification of finite deformation j2 von-mises plasticity and quantitative dislocation mechanics. *Journal of the Mechanics and Physics of Solids*, 143:104050.

Artstein, Z. (2002). On singularly perturbed ordinary differential equations with measure-valued limits. *Proceedings of Equadiff 10*, pages 15–26.

Berezhkovskii, A. and Szabo, A. (2011). Time scale separation leads to position-dependent diffusion along a slow coordinate. *The Journal of Chemical Physics*, 135(7).

Bolhuis, P. G. and Swenson, D. W. H. (2021). Transition path sampling as Markov Chain Monte Carlo of trajectories: Recent algorithms, software, applications, and future outlook. *Advanced Theory and Simulations*, 4(4).

Bornemann, F. (1998). *Homogenization in time of singularly perturbed mechanical systems*, volume Lecture Notes in Mathematics. Springer-Verlag Berlin Heidelberg.

Bornemann, F. A. and Schütte, C. (1997). Homogenization of Hamiltonian systems with a strong constraining potential. *Physica D: Nonlinear Phenomena*, 102(1-2):57–77.

Chang, L., Zhou, C.-Y., Wen, L.-L., Li, J., and He, X.-H. (2017). Molecular dynamics study of strain rate effects on tensile behavior of single crystal titanium nanowire. *Computational Materials Science*, 128:348–358.

Chatterjee, S., Acharya, A., and Artstein, Z. (2018). Computing singularly perturbed differential equations. *Journal of Computational Physics*, 354:417–446.

Chatterjee, S., Po, G., Zhang, X., Acharya, A., and Ghoniem, N. (2020). Plasticity without phenomenology: a first step. *Journal of the Mechanics and Physics of Solids*, 143:104059.

Frenkel, J. (1926). Zur theorie der elastizitätsgrenze und der festigkeit kristallinischer körper. *Zeitschrift für Physik*, 37(7):572–609.

Hijón, C., Español, P., Vanden-Eijnden, E., and Delgado-Buscalioni, R. (2010). Mori–zwanzig formalism as a practical computational tool. *Faraday Discuss.*, 144:301–322.

Izvekov, S. and Voth, G. A. (2006). Modeling real dynamics in the coarse-grained representation of condensed phase systems. *The Journal of Chemical Physics*, 125(15).

Kabir, H., Aghdam, M. M., Samandari, S. S., and Moeini, M. (2024). A molecular dynamics study on the size effects of $\text{Fe}_3\text{O}_4$ nanoparticles on the mechanical characteristics of polypyrrole/$\text{Fe}_3\text{O}_4$ nanocomposite. *Molecular Simulation*, 50(7-9):493–505.

Klar, M., Matthies, K., Reina, C., and Zimmer, J. (2021). Second-order fast–slow dynamics of non-ergodic hamil- tonian systems: Thermodynamic interpretation and simulation. *Physica D: Nonlinear Phenomena*, 428:133036.

Komanduri, R., Chandrasekaran, N., and Raff, L. (2001). Molecular dynamics (md) simulation of uniaxial tension of some single-crystal cubic metals at nanolevel. *International Journal of Mechanical Sciences*, 43(10):2237–2260.

Laio, A. and Parrinello, M. (2002). Escaping free-energy minima. *Proceedings of the National Academy of Sciences*, 99(20):12562–12566.

LAMMPS Developers (2024a). *LAMMPS Documentation: fix nve*. Sandia National Laboratories. Velocity-Verlet time integration.

LAMMPS Developers (2024b). *LAMMPS Documentation: run_style verlet*. Sandia National Laboratories. Ve- locity form of the Störmer–Verlet integrator.

Miao, Y., Feher, V. A., and McCammon, J. A. (2015). Gaussian accelerated molecular dynamics: Uncon- strained enhanced sampling and free energy calculation. *Journal of Chemical Theory and Computation*, 11(8):3584–3595.

Mielke, A., Peletier, M. A., and Zimmer, J. (2025). Deriving a generic system from a hamiltonian system: Mielke, peletier and zimmer. *Archive for Rational Mechanics and Analysis*, 249(5):62.

Mishin, Y., Farkas, D., Mehl, M. J., and Papaconstantopoulos, D. A. (1999). Interatomic potentials for monoatomic metals from experimental data and ab initio calculations. *Phys. Rev. B*, 59:3393–3407.

Mohr, B., van Heesch, T., Pérez de Alba Ortíz, A., and Vreede, J. (2024). Enhanced sampling strategies for molecular simulation of <scp>dna</scp>. *WIREs Computational Molecular Science*, 14(2).

Neishtadt, A. (2019). On mechanisms of destruction of adiabatic invariance in slow–fast hamiltonian systems. *Nonlinearity*, 32(11):R53–R76.

Noid, W., Szukalo, R. J., Kidder, K. M., and Lesniewski, M. C. (2024). Rigorous progress in coarse-graining. *Annual Review of Physical Chemistry*, 75(1):21–45.

Roy, A. and Acharya, A. (2005). Finite element approximation of field dislocation mechanics. *Journal of the Mechanics and Physics of Solids*, 53(1):143–170.

Roy, A. and Acharya, A. (2006). Size effects and idealized dislocation microstructure at small scales: Predictions of a phenomenological model of mesoscopic field dislocation mechanics: Part ii. *Journal of the Mechanics and Physics of Solids*, 54(8):1711–1743.

Shi, R., Qian, H., and Lu, Z. (2023). Coarse-grained molecular dynamics simulation of polymers: Structures and dynamics. *WIREs Computational Molecular Science*, 13(6).

Slemrod, M. and Acharya, A. (2012). Time-averaged coarse variables for multi-scale dynamics. *Quarterly of applied mathematics*, 70(4):793–803.

So/rensen, M. R. and Voter, A. F. (2000). Temperature-accelerated dynamics for simulation of infrequent events. *The Journal of Chemical Physics*, 112(21):9599–9606.

Stukowski, A. (2010). Visualization and analysis of atomistic simulation data with OVITO-the Open Visualization Tool. *Modelling and Simulation in Materials Science and Engineering*, 18(1):015012.

Sugita, Y. and Okamoto, Y. (1999). Replica-exchange molecular dynamics method for protein folding. *Chemical Physics Letters*, 314(1–2):141–151.

Tan, L., Acharya, A., and Dayal, K. (2014). Modeling of slow time-scale behavior of fast molecular dynamic systems. *Journal of the Mechanics and Physics of Solids*, 64:24–43.

Uchic, M. D., Dimiduk, D. M., Florando, J. N., and Nix, W. D. (2004). Sample dimensions influence strength and crystal plasticity. *Science*, 305(5686):986–989.

Van Vliet, K. J., Li, J., Zhu, T., Yip, S., and Suresh, S. (2003). Quantifying the early stages of plasticity through nanoscale experiments and simulations. *Physical Review B*, 67(10):104105.

Vogl, L. M., Schweizer, P., Richter, G., and Spiecker, E. (2021). Effect of size and shape on the elastic modulus of metal nanowires. *MRS Advances*, 6(27):665–673.

Voter, A. F. (1997). Hyperdynamics: Accelerated molecular dynamics of infrequent events. *Physical Review Letters*, 78(20):3908–3911.

Wan, W., Tang, C., Qiu, A., and Xiang, Y. (2021). The size effects of point defect on the mechanical properties of monocrystalline silicon: A molecular dynamics study. *Materials*, 14(11):3011.

Yu, H., Sun, C., Zhang, W., Lei, S., and Huang, Q. (2013). Study on size-dependent young's modulus of a silicon nanobeam by molecular dynamics simulation. *Journal of Nanomaterials*, 2013(1):319302.

Zamora, R. J., Uberuaga, B. P., Perez, D., and Voter, A. F. (2016). The modern temperature-accelerated dynamics approach. *Annual Review of Chemical and Biomolecular Engineering*, 7(1):87–110.