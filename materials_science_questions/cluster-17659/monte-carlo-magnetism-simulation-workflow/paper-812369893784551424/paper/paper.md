![](./images/812369893784551424_1.jpg)

Available online at www.sciencedirect.com

![](./images/812369893784551424_2.jpg)

Journal of Magnetism and Magnetic Materials 272-276 (2004) 674-675

![](./images/812369893784551424_3.jpg)

www.elsevier.com/locate/jmmm

# Temperature dependence of switching curve for spatially oscillating field in antiferromagnetic Ising model

M.S. Magdoń-Maksymowicz$^{\mathrm{a},*}$, P. Gronek$^{\mathrm{b}}$, A.Z. Maksymowicz$^{\mathrm{b}}$, A. Dydejczyk$^{\mathrm{b}}$

$^{\mathrm{a}}$ Department of Mathematical Statistics, Agricultural University, Mickiewicza 21, Kraków 31-120, Poland
$^{\mathrm{b}}$ Department of Physics and Nuclear Techniques, AGH, Mickiewicza 30, Kraków 30-059, Poland

## Abstract

The switching magnetization process under influence of a magnetic field $(+h,-h)$ applied to the two nearest-neighbors sublattices of Ising spins with antiferromagnetic coupling are studied. Monte Carlo simulations of the switching curve $h(t)$ against temperature $t$ is presented. The switching takes place through an uniform coherent rotation below a critical temperature $t_{1}$. Above $t_{1}$, nucleation of bubble domains takes place and the growth of the domains corresponds to a flat portion of the $h(t)$ dependence till temperature $t_{2}$. For $t>t_{2}$ both mechanisms of local spin flips and domain wall motions are present, so monotone decrease of $h(t)$ is observed.

© 2003 Elsevier B.V. All rights reserved.

PACS: 75.60.Jk; 75.40.Mg

Keywords: Magnetization reversal; Hysteresis; Numerical simulations

For a ferromagnet there are two spin “up” and spin “down” twin configurations at zero temperature, and the system goes to one of them. On applied magnetic field $H$ in the direction opposite to the direction of the spins, this configuration becomes metastable. The system jumps to the stable state at the switching field $H$ at which magnetization reversal takes place. For antiferromagnetic coupling the situation is similar, yet we need to apply a nonuniform field $(+H$ and $-H)$ on neighboring sites. Analytical results for the switching curve $H(T)$ may be obtained when, for example, an over-simplified molecular field approximation (MFA) is applied. In this paper we concentrate on calculations of the antiferromagnetic Ising model studied by means of the Monte Carlo simulation with the standard cyclic boundary conditions.

Two-dimensional $N\times N=1000\times 1000$ lattice of spins, coupled by negative exchange integral energy $J<0$ between nearest neighbours, was considered. We use reduced temperature $t=T/T_{\mathrm{c}}$ normalized to the critical temperature $T_{\mathrm{c}}$ given by $T_{\mathrm{c}}=-J$ for the MFA and $T_{\mathrm{c}}=-0.567296326\cdot J$ for the exact result. Anti-ferromagnetic initial spin configuration was assumed with all spins “down” on the first sublattice and all spins “up” on the other sublattice. After some 1000 or so iteration steps we are close to the thermal equilibrium. Then we apply opposite magnetic field $H>0$ on the first sublattice and $-H$ on the other. We observe the switching of the system from this metastable state into a stable solution when the spins are reversed at the critical field $H$. This normalized field $h=-H/4J$ depends on temperature $t$. ($-4J$ is the maximum required field to force spin flips.) While scanning $h$, we calculate the spin net magnetization and the spin-spin correlations to determine the critical field. We also observe the spin distribution on the lattice to investigate in detail the mechanism of the spins reversal.

The obtained $h(t)$ switching curve for the applied spatially oscillating field $(+h,-h)$ is shown in Fig. 1. The MFA results, not displayed on the figure, overestimate the fields $h$ and produces a smooth $h(t)$ function. The Monte Carlo simulation yields less regular plot with a flat part for $t_{1}<t<t_{2}$. This corresponds to specific

*Corresponding author. Tel.: + 48-12-62-43-80; fax: + 48-12-633-62-45.
E-mail address: rrmagdon@cyf-kr.edu.pl
(M.S. Magdoń-Maksymowicz).

0304-8853/$- see front matter © 2003 Elsevier B.V. All rights reserved.
doi:10.1016/j.jmmm.2003.12.677

![](./images/812369893784551424_4.jpg)

Fig. 1. Switching field $h=-H/4J$ against temperature $t=T/T_{\rm c}$ for $1000\times 1000$ lattice.

magnetization process due to propagation of a nucleated bubble domain wall across the sample. (A bubble domain is a closed area of all spins reversed with respect to the orientation of the spins in the ground state, before they were flipped—the smallest bubble is just one spin reversal which makes the nucleation centre for the bubble domain to grow.) For low-temperature range $0<t<t_{1}$, there are no nucleation centers. Then the uniform rotation mechanism is dominant, and all spins flip almost simultaneously. The Ising model predicts reduced magnetization $m=1-2x^{4}$ at equilibrium in the low-temperature limit, where $x=\exp(-0.5J/T)$. The one spin flipped on the $N\times N$ net corresponds to magnetization decrease $\Delta m=2/(N\times N)$. We assume a less demanding condition $\Delta m>1/(N\times N)$ for the nucleation center to appear. The average number of reversed spins is then $\frac{1}{2}$, and so it is more likely to find the nucleation center rather than the system still remaining in the ground state. From this, we get a rough estimate of the temperature $t_{1}$. One gets $1/t_{1}=1.1346\log(N)$. For $N=1000$ we get $t_{1}=0.13$. In simulations, the plateau region is seen for the temperature range from $t_{1}=0.09$ to $t_{2}=0.16$. Our analytical value $t_{1}=0.13$ is perhaps not too far from the simulation result. In experiment, $N$ is close to the thermodynamical limit $N\rightarrow\infty$ and so we only observe the $t_{1}=0$. The plateau above $t_{1}$ stems from the fact that the bubble nucleated domain, the one spin flipped, grows at this field $h=\frac{1}{2}$ with speed of about 1 lattice constant per iteration and overall magnetization reversal takes place. At higher temperatures we have more nucleation centres, yet same field $h=\frac{1}{2}$ completes the reversal. From experiment done by H. Kronmuller et al. [1] on coercivity versus temperature, one can clearly see the plateau as obtained in our simulations. This plateau, predicted at $h=1-2/Z$, may be read out from experimental data at positions $h$ corresponding to the coordination number $Z$ between 8 and 12 for both $\text{Fe}_{77}\text{Nd}_{15}\text{B}_{8}$ and $\text{Fe}_{77}\text{Pr}_{15}\text{B}_{8}$ samples. (To do this we extrapolated the experimental data down to $t=0$ temperature to evaluate the maximum of the switching field.) Above $t_{2}$, both reversal mechanisms by the wall movement and local spin flips due to the thermal excitation take place. In short, the overall results seem to be supported by experimental data of [1] (Fig. 2).

![](./images/812369893784551424_5.jpg)

Fig. 2. Plateau region of the switching field $h(t)$.

The work was partly supported by Grant of Agriculture University, Department of Mathematical Statistics and by University of Mining and Metallurgy, Faculty of Physics and Nuclear Techniques. Computer calculations were carried out at the Academic Computer Center CYFRONET-KRAKÓW.

### References

[1] H. Kronmuller, K.D. Durst, M. Sagawa, J. Magn. Magn. Mater. 74 (1988) 291–302.