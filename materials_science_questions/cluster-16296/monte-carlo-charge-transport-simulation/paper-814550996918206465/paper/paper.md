# Size effects in multisubband quantum wire structures

S. Briggs and J. P. Leburton
Coordinated Sciences Laboratory and Department of Electrical and Computer Engineering,
University of Illinois at Urbana-Champaign, Urbana, Illinois 61801
(Received 7 December 1987; revised manuscript received 2 May 1988)

We present a Monte Carlo simulation of multisubband quasi-one-dimensional GaAs-Al$_{x}$Ga$_{1-x}$As structures. The simulation includes polar-optical-phonon and inelastic acoustic-phonon scattering and investigates the effect of changing confinement on electron velocity. Even at low longitudinal fields, for confinements in the range 50-230 Å, intersubband scattering has a profound effect on transport parameters. Under optimum conditions, differential mobility in excess of twice the bulk value at 300 K is obtained. Asymmetric geometry and high degree of confinement result in interesting differences from magnetotransport. In addition, resonance analogous to the magnetophonon effect occurs when the separation between lowest subbands is equal to the polar-optical-phonon energy.

## I. INTRODUCTION

In recent years there has been increasing interest in the investigation of quasi-one-dimensional (1D) structures. Progress in epitaxial technologies combined with the emergence of new fine-line-patterning techniques have made the fabrication of artificial low-dimensional structures feasible in the near future. $^{1-7}$ From a fundamental viewpoint, the interest in 1D systems has been motivated by the fascinating consequences of the localization theory, which predicts that in weakly disordered structures no extended state exists and, consequently, the 1D conductivity goes to zero at low temperature. $^{8,9}$ At intermediate temperature and finite transverse confinement, however, the "particle-in-a-box" picture seems more realistic and the concept of a quasi-1D system is a natural extension of the ultraconfined two-dimensional (2D) electron gas. Sakaki suggested that semiconductor quantum wire structures could be the basis for very fast transport processes. $^{10}$ Because of the reduction of phase space, the number of available final states during the scattering process (only forward or backward scattering) is very limited and results in the enhancement of the 1D mobility with respect to the bulk value. Theoretical investigations of the electronic properties of semiconductor wire structures have recently been accomplished. $^{11-13}$ For III-V compounds, calculations of the most important scattering mechanisms, i.e., impurity, $^{10,14}$ acoustic, $^{15}$ and optical phonons, $^{16}$ show the importance of significant size effects which have been confirmed by Monte Carlo simulation. $^{17}$ In modulation-doping structures, ionized-impurity scattering is vanishingly small, which suggests 1D mobility above $1\times 10^{6}\ \text{cm}^{2}/\text{V s}.^{18}$

However, because of the high level of quantization, most of the transport models assume the extreme quantum limit (EQL) and neglect the influence of multiple subbands (one-subband models). $^{17,19}$ This approximation is precarious when the spacing between subbands is comparable to $kT$, as recently discussed by Das Sarma and Xie for low temperature in Si, $^{20}$ or when hot-electron effects induce intersubband scattering. Although these processes are analogous to longitudinal magnetotransport phenomena, $^{21,22}$ they occur with a variety of features which are specific to artificial 1D systems. For instance, the two transverse confining potentials are, in general, independent; this provides a situation completely different from the harmonic-oscillator-like spectrum of energy levels resulting from the cylindrical symmetry of the magnetic field. The different character of the two types of wave functions and the unequally spaced energy spectrum of the artificial 1D structures significantly influences the intersubband transitions. Furthermore, energy-level spacing of the order of the optical-phonon energy or the thermal energy at room temperature can, in principle, be achieved with artificial confinement; this anticipates resonance conditions superior to magnetotransport. Therefore, in order to assess realistically the transport properties of quantum wires, the development of a multisubband transport model is desirable.

The paper presents a Monte Carlo simulation of a multisubband quasi-1D GaAs-Al$_{x}$Ga$_{1-x}$As structure. Because of the small electron effective mass, quantization effects are more pronounced than in Si. Our purpose is to study the effect of varying confinement on the transport properties of the 1D system. We specifically focus on lattice scattering and analyze the influence of intersubband transitions on the transport properties. In the first approximation, we limit our simulation to the $\Gamma$ valley in GaAs and neglect high-energy processes such as intervalley scattering and real-space transfer. In addition, we neglect nonparabolicity corrections in the energy dispersion relation. Our model involves up to seven subbands, which allows a realistic simulation of confinement conditions in the range 50-230 Å. As the exact position of electronic states is not of primary importance for this work, elementary confining-potential profiles have been assumed. This assumption does not limit the validity of our model, as the real transport features may merely be shifted but not altered with respect to our simple electronic model.

## II. MODEL

Our model consists of a GaAs-AlₓGa₁₋ₓAs quantum well (QW) with a perpendicular gate electrode and a triangular electrostatic potential. At present, we assume a geometry similar to the V-groove field-effect-transistor (FET) structure proposed by Sakaki¹⁰ [Fig. 1(a)]. This device configuration may not be suited for high-speed transport due to interface states between the insulator and the active region resulting from processing which may degrade the mobility. However, the V-groove wire characterized by a quantum well in the y direction and a triangular potential in the z direction offers, in principle, the largest degree of confinement which can be controlled by external transverse electric fields (gate fields) $F_z$. In addition, the quantizations resulting from the square well and the triangular potential are rather different and result in various interesting features in the transport characteristics. The model is flexible enough to also simulate a multiwire gate FET structure of the type proposed by Warren and Antoniadis.²³,²⁴ In the present simulation all electrons remain in the $\Gamma$ valley and all subbands are parabolic. We assume that electrons will transfer to three-dimensional (3D) states (primarily by intervalley scattering or real-space transfer²⁵) before they reach 400 meV above the well bottom. The program currently has no routine for these processes, which limits the maximum electron energy that we can model. If an electron reaches an energy of 400 meV, we stop the simulation of its path and choose a new electron to replace it. We are thus limited to longitudinal fields ($F_x$) of 1 kV/cm or less and typically 500 V/cm to avoid electron runaway at 300 K. At lower temperatures we can go to somewhat higher fields because of the lack of phonon absorption. We have run simulations at 300 and 77 K with well widths $L_y$ in the range 250–50 Å. Wider wells require too many levels for an accurate simulation; however, this is not a serious constraint, as there are few electrons at the higher energies anyway. To save memory in the code, the lowest energy we consider is 100 meV above the bottom of the well, which sets a lower limit on the range of confinement conditions we can model. Our transverse electric fields $F_z$ range from an upper limit of 200 down to 20 kV/cm and are subject to the same restrictions as those on well widths.

For the y direction we calculate wave functions in the infinite-square-well approximation. The z wave functions are computed using a variational approach, with exponentially damped polynomials as the trial wave functions. We compute the first three y and z wave functions and combine them to obtain nine wave functions. Then, the total wave functions $\Psi$ are given by

$$
\begin{aligned}
\Psi_{i, j}=&\left(\frac{2}{L_{y}}\right)^{1 / 2} \sin \left(\frac{i \pi y}{L_{y}}\right) e^{-\alpha_{j} z} \sum_{k=1}^{j} c_{k, j} z^{k}, \\
& i=1,2,3, \quad j=1,2,3 \quad(1)
\end{aligned}
$$

where $\alpha_j$ and $c_{k,j}$ are determined by a variational calculation. The corresponding energies [Fig. 1(b)] are functions of the longitudinal electron k vector and are given by

![](./images/814550996918206465_1.jpg)

FIG. 1. (a) Schematic representation of a FET 1D quantum wire [after Sakaki (Ref. 10)]. (b) A representation of the confining potentials and two-electron energy levels and wave functions in the wire structure.

$$
E_{i, j}(k)=\frac{\hbar^{2} k^{2}}{2 m^{*}}+E_{i}+E_{j}, \quad i=1,2,3, \quad j=1,2,3 \quad(2 a)
$$

with $E_i$, the square-well energy, calculated from

$$
E_{i}=\frac{(\hbar \pi i)^{2}}{2 m^{*} L_{y}^{2}}, \quad i=1,2,3. \quad(2 b)
$$

Although $E_j$, the triangular potential energy, is obtained from a variational calculation, a useful approximation is²⁶

$$
E_{j}=\left(\frac{\hbar^{2}}{2 m^{*}}\right)^{1 / 3}\left(\frac{3}{2} \pi q F_{z}\right)^{2 / 3}\left(j-\frac{1}{4}\right)^{2 / 3}, \quad j=1,2,3. \quad(2 c)
$$

These approximations are good if the energy level lies deep in the well. The higher y levels should be spaced more closely as they approach the top of the QW, and the z levels more closely as screening flattens out the triangular potential. The $y=2, z=3$ and $y=3, z=3$ states are omitted because of memory constraints in the Monte Carlo code. For most confinement conditions of interest, these two levels are above the edge of the GaAs-AlₓGa₁₋ₓAs barrier and can be neglected. Although the lowest-energy level is clearly $E_{1,1}$, the ordering of the higher subbands depends on the confinement conditions. To avoid confusion, the subbands will be numbered with a single subband $v$, which will range in order of increas-

ing energy from 1 for the lowest subband to 7 for the highest subband. The $y$ and $z$ quantum numbers will, in general, not be used.

Currently, we consider only polar-optical-phonon (POP) and inelastic acoustic-phonon scattering. The 1D transition probabilities from an electron state $k_i$ in initial subband $v$ to a state $k_f$ in final subband $\mu$ are calculated according to Fermi's golden rule as

$$
W_{v, \mu}\left(k_{i}, k_{f}\right)=\frac{2 \pi}{\hbar} \delta_{k_{i}-k_{f} \pm q_{x}} \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} d q_{y} d q_{z}\left|M_{3 \mathrm{D}, v, \mu}\left(q_{x}, q_{y}, q_{z}\right)\right|^{2}\left(N_{q}+\frac{1}{2} \pm \frac{1}{2}\right) \delta\left(E_{\mu}\left(k_{f}\right)-E_{v}\left(k_{i}\right) \pm \hbar \omega_{q}\right), \quad \text { (3) }
$$

where $q_x$ is the longitudinal- and $q_y, q_z$ the transverse-phonon wave vectors, respectively. $N_q$ is the phonon occupation number with the $\pm$ corresponding to phonon emission or absorption. The double integral over $q_y$ and $q_z$ represents the calculation of the 1D matrix elements $M_{1 \mathrm{D}, v, \mu}(q_x)$ from the normal 3D matrix elements. Here we consider only bulk- (i.e., 3D) phonon modes and neglect 1D and surface modes. This does not introduce significant error as long as the confinement is not excessively high, i.e., less than $50 \mathring{A}$. The POP dispersion relation is assumed to be a constant, which makes $N_q$ and the energy-conservation $\delta$ function independent of $q$; therefore they can be factored out of the double integral. However, the nonconstant dispersion relation for acoustic phonons makes computation of the integral considerably more complex. The numerical integration routine has $q_x$ as an input parameter, which we vary to obtain 1D matrix elements. For acoustic phonons we evaluate the integral for $q_x$ in the range $7 \times 10^{4}<q_{x}<1.5 \times 10^{7}$ $\mathrm{cm}^{-1}$. The acoustic-phonon-transition probabilities are essentially independent of $q_x$ for smaller values, while $1.5 \times 10^{7} \mathrm{~cm}^{-1}$ is the largest possible momentum exchange. For POP transitions the integral is evaluated for $1 \times 10^{0}<q_{x}<1 \times 10^{7} \mathrm{~cm}^{-1}$.

The $\delta_k$ term in Eq. (3) represents conservation of longitudinal momentum, with the $\pm$ sign corresponding to phonon absorption or emission, respectively, and is used to select a value for $q_x$ and the corresponding matrix element. Scattering rates are computed by integrating the transition probabilities over the final electron $k$ states.

The total scattering rate for POP's or acoustic phonons from the initial state $k_i$ in subband $v$ is then given by

$$
\begin{aligned}
\lambda_{v}\left(k_{i}\right)= & \sum_{\mu=1}^{7} \int d k_{f} \frac{2 \pi}{\hbar}\left|M_{1 \mathrm{D}, v, \mu}\left(q_{x}\right)\right|^{2} \\
& \times \delta\left(k_{i}-k_{f} \pm q_{x}\right) \frac{m}{\hbar^{2}} \frac{1}{k_{f}},
\end{aligned}
$$

where we have transformed the energy-conservation $\delta$ function into a wave-vector-conservation $\delta$ function. For each 1D subband the wave-vector-conservation $\delta$ function reduces the integral to a sum over the four possible final states corresponding to forward or backward emission or absorption.

A broadening of the phonon energy, $\hbar / \tau_{\text {POP }}$, was used to smooth out the divergence in the scattering rate due to the final density of states. The physical justification for this broadening is that electrons encounter a broadened final density of states as they are scattered by phonons distributed within a finite energy range. This approximation should be distinguished from the explicit broadening in the density of states as considered by Das Sarma and Xie. $^{20}$ Because of its long tail, a Lorentzian-broadening factor allows for unrealistic phonon energies; this is especially noticeable at low temperatures. To avoid this unrealistic distribution, a Gaussian profile was used to drastically reduce the number of POP's with energy substantially different from $36 \mathrm{meV}$. In the first approximation this replaces the $1 / k_f$ factor in Eq. (4) by its convolution with a Gaussian distribution:

$$
\frac{1}{k_{f}} \leftarrow \frac{1}{\left(2 m^{*}\right)^{1 / 2}} \frac{\tau_{\mathrm{POP}}}{\sqrt{2 \pi}} \int_{-\infty}^{+\infty} \exp \left[-\frac{\left(E^{\prime}-\hbar \omega_{\mathrm{LO}}\right)^{2}}{2\left(\hbar / \tau_{\mathrm{POP}}\right)^{2}}\right] \frac{1}{\left[E^{\prime}+E_{v}(k=0)-E_{v}\left(k_{f}\right)\right]^{1 / 2}} d E^{\prime}.
$$

A similar broadening factor was also used for acoustic-phonon scattering.

We consider energies from 100 to $400 \mathrm{meV}$ above the bottom of the well. This energy range is divided into 400 intervals of uniform size to compute the scattering rates. For each energy interval in each subband, we consider forward and backward emission and absorption for both POP's and acoustic phonons to each possible final subband. This gives us $56(2 \times 2 \times 2 \times 7)$ possible independent scattering mechanisms for each initial state. This number is then multiplied by the number of initial subbands (seven) and the number of points in the energy mesh (400) to obtain the total number of rates stored in the code. This large number of scattering rates is the primary limitation on the maximum number of subbands in the code since the storage required is proportional to the square of the number of subbands. These scattering rates are saved in files and used as input to the Monte Carlo code. The rates show a large number of peaks; each peak is proportional to the density of final states and corresponds to an emission or absorption to the bottom of a subband [Fig. 2(a)]. The large single peaks are due to POP scattering,

![](./images/814550996918206465_2.jpg)

FIG. 2. (a) Total (POP and acoustic phonon) scattering rates for a quantum wire with $L_y=135$ $\text{\AA}$ and $F_z=120$ kV/cm at 300 K. Peaks correspond to an emission or absorption to the bottom of a subband. Large peaks represent POP transitions; small double peaks are due to acoustic phonons. For clarify, only the first three subbands are shown, with the heaviest line representing the lowest subband and the lightest representing the second subband. (b) Electron-distribution function for the same quantum wire.

the small peaks in pairs are acoustic phonon absorption and emission pairs to subband bottoms. These peaks make the velocity and distribution functions [Fig. 2(b)] sensitive to the energy separation between subbands, particularly between the first and second subbands. Below the POP emission threshold, rates are somewhat smaller than in bulk, while at high energies the large number of subbands enhances the rates with respect to the bulk value. The rates drop above 344 meV because we no longer allow for POP absorption beyond that point.

### III. MONTE CARLO CODE

We run a steady-state single-particle Monte Carlo code. An electron is placed at an arbitrary position in the bottom subband and undergoes $6\times 10^3$ scattering events to eliminate any effect of the initial conditions before we begin collecting statistics on it. Although the velocity converges after less than $4\times 10^4$ scattering events, we simulate $4\times 10^5$ (not including the $6\times 10^3$ needed to achieve steady state) events to obtain better convergence on the distribution functions. If an electron goes above our maximum energy (assumed to have scattered to a 3D state), it is lost to the simulation and a new electron is injected in the bottom subband. While the energy range for computing scattering rates is split up into 400 intervals, the Monte Carlo code has a resolution of $\delta E=0.075$ meV, which corresponds to 4000 intervals on the same range. We compute $k(E)$ at the start of the program for each interval and save it in a table for later use in evaluating free-flight times.

Because of the large number of peaks in the rates, normal methods for computing free-flight times are inefficient. Using constant or piecewise-constant scattering rates with self-scattering would have introduced a very large percentage of self-scattering events. An iterative gamma method$^{27}$ was tried, but the sharpness of the peaks meant that a large number of iterations were needed to find an appropriate gamma. Instead, a direct integration method was used. For a given subband $\nu$, if $r$ is a uniformly distributed random number on [0,1], then
$$
-\ln r=\int_{0}^{t}\lambda_{\nu}(k_{\nu}(t'))dt', \tag{6}
$$
where $t$ is the time of the free flight, $k_{\nu}(t)$ is the momentum as a function of time in subband $\nu$, and $\lambda_{\nu}(k_{\nu})$ is the scattering rate as a function of momentum for that subband. The program approximates the integral as a sum and moves the electron in uniform energy steps of size $\delta E$ from an initial energy $E_i$ until a final energy $E_f$ is found such that
$$
-\ln r=\sum_{E=E_i}^{E_f}\lambda_{\nu}(k_{\nu}(E))\Delta t(E), \tag{7a}
$$
with
$$
\Delta t(E)=\frac{\hbar}{eF_x}\Delta k_{\nu}(E) \tag{7b}
$$
and
$$
\Delta k_{\nu}(E)=|k_{\nu}(E\pm\delta E)-k_{\nu}(E)|, \tag{7c}
$$
the $\pm$ depending on whether the electron is accelerating or decelerating. In 3D simulations it is virtually impossible to store $k(E)$ in tabular form because of the large number of possible $k$ values. In 1D systems there are only two scalar $k_{\nu}$ values for each energy and each $\nu$ (tabulated earlier by the program) and, hence, $\Delta k_{\nu}$ is essentially a look-up function which avoids the time-consuming square-root computation required to determine $k_{\nu}(E)$. Moreover, in three dimensions, $\Delta t$ is a complicated function of $k$, involving squares and square-root computations, which typically prohibits direct-integration algorithms in Monte Carlo codes. For 1D systems, however, direct integration compares favorably with other methods.

The electron state is sampled after every free flight to obtain the before-scattering distribution $n_{b,\nu}(k)$ for the

$v$th subband. The correct distribution $n_{\nu}(k)$ is obtained from$^{28}$
$$
n_{\nu}(k)=C_{\nu} \frac{n_{b, \nu}(k)}{\lambda_{\nu}(k)}, \tag{8}
$$
where $C_{\nu}$ is a normalizing constant required to preserve the relative electron population in each subband. This distribution is saved and used to calculate all the quantities of interest.

## IV. RESULTS

In general, velocities in quasi-1D systems are higher than in bulk (3D) GaAs, despite the fact that scattering rates exhibit large singularities and background values on the average comparable to bulk rates. We attribute this increase to the reduction in phase space of the 1D system. Because of the lack of transverse scattering and the $1/q$ dependence of the electron-POP interaction, the scattering is more strongly forward peaked than in three dimensions. Although acoustic phonons were included in this simulation, they do not play an important role and simply tend to reduce the velocities by about $10\%$.

Figure 3 summarizes the effects of various confinement conditions on the velocity. The degree of confinement is represented by the energy of the first subband relative to the bottom of the well. Although this is a simplification and ignores the fact that confinement (and velocity) is a function of two variables $(L_y$ and $F_z)$, it demonstrates the primary effects on velocity. From a general standpoint, when the structure is in the EQL (i.e., when only the lowest subband is occupied), increasing confinement reduces the velocity. This is in agreement with the size effects predicted by several authors. $^{16,17}$ In this case the overlap integrals (form factors) in the matrix elements approach unity and enhance the scattering rates. However, this also occurs under less restricted conditions below the EQL when increasing confinement does not affect the separation between the first and second subbands, as can be seen from curve $a$ in Fig. 3, where $F_z$ is varied from 100 to 200 kV/cm while holding $L_y$ at $200\ \mathring{\text{A}}$. For these conditions, the first-excited subband is the $y=2, z=1$ subband, and since $L_y$ remains constant the separation between the bottom and first-excited subbands remains 42 meV. As confinement increases, the velocity at $F_x=500$ V/cm decreases from $6.11\times 10^6$ to $5.63\times 10^6$ cm/s.

At low confinement, upper subbands play a significant role because more final states (more final subbands) are available for scattering and velocities are lower than the EQL values. Consequently, increasing confinement towards the EQL increases velocity as intersubband scattering is suppressed. In the low-energy portion of curve $b$, as the bottom subband moves from 128 to 138 meV ($L_y$ is varied from 165 to $135\ \mathring{\text{A}}$ while holding $F_z$ fixed at 120 kV/cm), the separation between the lowest subband and the first-excited subband is increased from 62 to 93 meV. This increases the fraction of carriers in the lowest subband from $80\%$ to $92\%$ (for $F_x=500$ V/cm) and enhances the velocity from $6.89\times 10^6$ to $8.08\times 10^6$ cm/s.

These two mechanisms—increasing overlap integrals and decreasing influence of upper subbands—explain the general trends as confinement is varied. For instance, under conditions resulting in the first-excited state being the $y=2, z=1$ state, increasing $F_z$ does not change the separation between the ground-state and first-excited subbands; consequently, velocity drops as the overlap integrals increase. However, if $L_y$ is decreased, the separation increases and results in velocity increase as long as the first-excited state remains the $y=2, z=1$ state, even though the overlap integrals approach unity. This is in contradiction with other 1D results, where only one subband is considered. $^{17}$ If $L_y$ is reduced sufficiently, the first-excited state will become the $y=1, z=2$ state instead of the $y=2, z=1$ state; further reductions cause the velocity to decrease as the overlap integrals increase without reducing the influence of scattering to the second subband. The last four points on curve $b$ of Fig. 3 show this effect as $L_y$ is lowered from 135 to $105\ \mathring{\text{A}}$ and the velocity decreases to $7.42\times 10^6$ cm/s. The peak in velocity (near 138 meV on curve $b$ in Fig. 3) is a tradeoff between increasing overlap integrals and approaching the EQL. When there is a crossover between the first-excited $y$ state and the first-excited $z$ state, increasing one confinement parameter increases the overlap integrals without reducing the influence of intersubband scattering (the other excited state does not move relative to the ground state and the separation remains the same). On the other hand, decreasing one confinement parameter decreases the overlap integrals, but only at the expense of moving away from the EQL (the corresponding excited state drops relative to the bottom state). This tradeoff condition is achieved for $L_y=135\ \mathring{\text{A}}$ and $F_z=120$ kV/cm. The peak has a first-excited state at 93 meV relative to the ground state and $92\%$ of the carriers are in the bottom subband for $F_z=500$ V/cm.

![](./images/814550996918206465_3.jpg)

FIG. 3. Variation of velocity with confinement for $F_x=500$ V/cm and $T=300$ K. Confinement is expressed as the position of the bottom subband relative to the well bottom. In curves $a$ ($\bigcirc$) and $c$ ($\square$), $F_z$ is varied while $L_y$ remains constant, while in curve $b$ ($	riangle$) $L_y$ is varied and $F_z$ is constant. Curve $a$ shows confinement increasing without affecting the separation between the bottom two subbands. In curves $b$ and $c$ the separation between the bottom two subbands does change as a function of confinement.

It is clear from the above discussion why the velocity

in curve $a$ is lower than in curves $b$ or $c$. While the latter curves represent a tradeoff between the conflicting effects of overlap integrals and intersubband scattering, the former curve has both high overlap integrals due to high confinement in the $z$ direction and high intersubband scattering due to low confinement in the $y$ direction.

While these two mechanisms explain the general trends in velocity as confinement is varied, there are several other important effects to consider. The first is due to the asymmetry between the $y$ confinement and the $z$ confinement. Since we assume an infinite square well, the $y$ wave functions do not spread out for higher-energy levels like the $z$ wave functions do. This tail in the $z$ wave functions lowers the overlap integrals in the scattering rates and tends to enhance the mobility in subbands with $z$ index greater than 1 with respect to subbands with $y$ index greater than 1. Hence, systems with the second subband corresponding to $y=1, z=2$ tend to have higher mobilities than structures with the second subband corresponding to $y=2, z=1$ due to the higher mobility in the second subband. In addition, the $y$ energy levels increase as $i^2$ [Eq. (2b)], while the $z$ levels are roughly proportional to $j^{2/3}$ [Eq. (2c)]. Curve $c$ in Fig. 3 shows the same trends as curve $b$, but in this case $F_{z}$ is varied from 80 to 160 kV/cm while $L_{y}$ is held fixed at $135\ \mathring{A}$. Initially, the second subband is the $y=1, z=2$ state and as $F_{z}$ exceeds 120 kV/cm the second subband becomes the $y=2, z=1$ state. Although the variation of bottom subband energies in curve $c$ is greater than in curve $b$, the corresponding velocity variation is smaller, for two reasons. First, the separation between the first and second subbands is less sensitive to confinement (from 72 to 93 meV versus 62 to 93 meV in curve $b$) because of the sublinear dependence of the energy on the $z$ quantum number $j$. In addition, at low $F_{z}$ the second subband is a $z=2$ state with weak intersubband scattering even when the separation between subbands is small.

The velocity-field relation for the confinement condition giving the highest velocity ($L_{y}=135\ \mathring{A}$, $F_{z}=120$ kV/cm is shown in Fig. 4(a), along with the equivalent relation for bulk GaAs. The velocity at $F_{z}=500$ V/cm corresponds to a mobility of $16\ 160\ \mathrm{cm}^{2}/\mathrm{V}\,\mathrm{s}$, which is over twice the bulk value of $8000\ \mathrm{cm}^{2}/\mathrm{V}\,\mathrm{s}$. An important effect is the dependence of the differential mobility on the field. At low fields it is over twice the bulk value, but converges toward the bulk value at high fields. We attribute this effect to intersubband scattering (breakdown of the EQL) at high fields. The inset of Fig. 4 shows the average electron energy in units of $kT$ as a function of $F_{x}$. For low fields the electron energy is roughly equal to $kT$ and most of the electrons are near the bottom of the first subband. At higher fields hot electrons become significant, with higher scattering rates due to the presence of other subbands (i.e., they are not in the EQL), which reduces their differential mobility. The velocity-field curve for the same confinement conditions at 77 K is shown in Fig. 4(b). Again, at low fields differential mobility is higher in the 1D system than in the bulk, while at high fields the velocities approach the same value.

![](./images/814550996918206465_4.jpg)

FIG. 4. Velocity-field relation for highest-velocity confinement condition ($L_{y}=135\ \mathring{A}$ and $F_{z}=120$ kV/cm) compared to bulk values [after Haase (Ref. 29)] at (a) 300 K and (b) 77 K. The inset in (a) shows the average electron energy in units of $kT$ as a function of the longitudinal field.

Finally, when the separation between first and second subbands is near $\hbar\omega_{\mathrm{POP}}$ a resonance condition can occur with the electron jumping back and forth between the first and second subbands. This can be seen clearly in the distribution functions near and at resonance. In Fig. 5(a) the separation between the first two levels is 28 meV and the structure is below the resonance condition. (The sharp narrow peaks in the distribution functions are artifacts of the method used, corresponding to peaks in the scattering rates). The first-subband population falls off slightly at 122 meV and more dramatically at 138 meV. 122 meV is the onset of POP absorption to the third subband, while 138 meV is the onset of emission to the first subband. The distribution function of the second subband at a given energy is not significantly different from that of the first subband. 60% of the electrons are in the first subband, with 30% in the second subband, and the remainder primarily in the third subband. In Fig. 5(c) the separation is 44 meV and the system is above resonance. 71% of the electrons are in the first subband, 24% in the second, and 5% in the third. In Fig. 5(b) the separation is 36 meV and the two subbands are in resonance. The first-subband population shows marked decreases at the onset of emission to both the first and second subbands, while the second subband shows a decrease at the onset of emission to the second subband. More importantly, the second-subband population is al-

![](./images/814550996918206465_5.jpg)

FIG. 5. Distribution functions for $F_x=500$ V/cm and 300 K near the POP resonance condition. The heaviest line is for the second subband and the lightest for the third subband. (a) System below resonance. (b) System at resonance. (c) System above resonance. For clarity, only the lowest three subbands are shown.

most 3 times that of the first-subband population for the same energy and almost as great as the first-subband population at the bottom of the subband. 55% of the electrons are in the first subband and 38% are in the second subband, with the remaining 7% being primarily in the third subband. We observe a weak dependence of the velocity on confinement at this point, which may be analogous to the magnetophonon effect.^{21,22} This resonance effect may also appear in 2D systems, but not so dramatically, since the density of states is constant instead of singular. As an example of the flexibility in the structure due to the asymmetry between $y$ and $z$ directions, in Fig. 5(b) the bottom three subbands are the $y=1, z=1,2,3$ states, and not only is the second subband in resonance with the first, but it is also very near resonance with the third subband. For the equivalent case with the lowest three subbands being the $z=1, y=1,2,3$ states, when the first two subbands are in resonance ($F_z=150$ kV/cm and $L_y=215$ Å), the second and third subbands are separated by 61 meV.

## V. CONCLUSIONS

We have presented a multisubband Monte Carlo model of quantum wire systems including POP and acoustic-phonon scattering mechanisms. The transport parameters are not a simple function of the confinement conditions and result primarily from the respective influence of two factors: the magnitude of the wave-function-overlap integral in the transition probability and the relative influence of the upper (mainly second) subbands. The asymmetry between $y$ and $z$ states is significant in determining the relative importance of the above factors. Under optimum conditions, mobilities near twice the bulk value at room temperature are anticipated. Resonances similar to the magnetophonon effect with enhanced second-subband populations occur when the subband separation is $\hbar\omega_{\text{POP}}$.

The ability to achieve, in principle, energy-level spacing comparable to $kT$ at room temperature makes artificial 1D structures well suited for comparison to magnetically confined systems. Quantum wires present additional important features which differ from longitudinal magnetotransport. The absence of azimuthal degeneracy and the flexibility in varying independently the $y$ and $z$ confinement provide a useful means of controlling externally the transport parameters. In the FET configuration, negative-differential transconductance can be obtained by simply changing the gate voltage to modify the subband spacing. Similarly, transitions from one to two dimensions could be investigated by gradually turning off the external field. Finally, owing to the finite well depth, negative-differential resistance though real-space transfer, or intervalley scattering, is expected to occur under strong longitudinal fields.

## ACKNOWLEDGMENTS

We are indebted to Dan Jovanovic for technical assistance. This work was supported by the U.S. National Science Foundation under Grant No. NSF-CDR-85-22666 and the Joint Services Electronics Program. Part of the computation was performed using the resources of the National Center for Supercomputing Applications (NCSA) of the University of Illinois.

¹P. Petroff, A. Gossard, R. Logan, and W. Wiegmann, Appl. Phys. Lett. 41, 635 (1982).

²T. J. Thornton, M. Pepper, H. Ahmed, D. Andrews, and G. J. Davies, Phys. Rev. Lett. 56, 1198 (1986).

³K. Kash, A. Scherer, J. Worlock, H. Craighead, and M. Tamargo, Appl. Phys. Lett. 49, 1043 (1986).

⁴H. Temkin, G. Dolan, M. Panish, and S. Chu, Appl. Phys. Lett. 50, 413 (1987).

⁵P. Petroff, J. Cibert, A. Gossard, G. Dolan, and C. Tu, J. Vac. Sci. Technol. 5, 1204 (1987).

⁶K. Ishibashi, K. Nagata, K. Gamo, S. Namba, S. Ishida, K. Murase, M. Kawabe, and Y. Aoyagi, Solid State Commun. 61, 385 (1987).

⁷T. Hiramoto, K. Hirakawa, Y. Iye, and T. Ikoma, Appl. Phys. Lett. 51, 1620 (1987).

⁸D. Thouless, Phys. Rev. Lett. 39, 1167 (1977).

⁹N. Giordano, W. Gilson, and D. Prober, Phys. Rev. Lett. 43, 725 (1979).

¹⁰H. Sakaki, Jpn. J. Appl. Phys. 19, L735 (1980).

¹¹S. Laux and F. Stern, Appl. Phys. Lett. 49, 91 (1986).

¹²K. Wong, M. Jaros, and J. Hagon, J. Vac. Sci. Technol. 5, 1198 (1987).

¹³S. Das Sarma and Wu-yan Lai, Phys. Rev. B 32, 1401 (1985).

¹⁴J. Lee and H. Spector, J. Appl. Phys. 54, 3921 (1983).

¹⁵V. Arora, Phys. Rev. B 23, 5611 (1981).

¹⁶J. P. Leburton, J. Appl. Phys. 56, 2850 (1984). [In this paper, the 1D absorption rate in Eq. (16b) should be corrected to include forward scattering corresponding to the $q_+$ value in Eq. (14b).]

¹⁷A. Ghosal, D. Chattopadhyay, and A. Bhattacharyya, J. Appl. Phys. 59, 2511 (1986).

¹⁸G. Fishman, Phys. Rev. B 34, 2394 (1986).

¹⁹P. Yuh and K. Wang, Appl. Phys. Lett. 49, 1738 (1986).

²⁰S. Das Sarma and X. Xie, Phys. Rev. B 35, 9875 (1987).

²¹R. Peterson, in *Transport Phenomena*, Vol. 10 of *Semiconductors and Semimetals*, edited by R. K. Willardson (Academic, New York, 1975), p. 221.

²²R. Stradling and R. Wood, J. Phys. C 1, 1711 (1968).

²³A. Warren, D. Antoniadis, H. Smith, and J. Melngailis, IEEE Electron. Dev. Lett. EDL-6, 294 (1985).

²⁴A. Warren, D. Antoniadis, and H. Smith, Phys. Rev. Lett. 56, 1858 (1986).

²⁵K. Hess, H. Morkoç, H. Shichijo, and B. Streetman, Appl. Phys. Lett. 35, 469 (1979).

²⁶F. Stern, CRC Crit. Rev. Solid-State Sci. 499 (1974).

²⁷R. Yorston, J. Comput. Phys. 64, 177 (1986).

²⁸C. Jacobini and L. Reggiani, Rev. Mod. Phys. 55, 645 (1983).

²⁹M. Haase, V. Robbins, N. Tabatabaie, and G. Stillman, J. Appl. Phys. 57, 2295 (1985).

![](./images/814550996918206465_6.jpg)

FIG. 1. (a) Schematic representation of a FET 1D quantum wire [after Sakaki (Ref. 10)]. (b) A representation of the confining potentials and two-electron energy levels and wave functions in the wire structure.