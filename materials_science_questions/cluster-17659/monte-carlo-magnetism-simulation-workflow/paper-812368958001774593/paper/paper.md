Available online at www.sciencedirect.com

![](./images/812368958001774593_1.jpg)

![](./images/812368958001774593_2.jpg)

Journal of Magnetism and Magnetic Materials 272-276 (2004) 1302-1303

![](./images/812368958001774593_3.jpg)

www.elsevier.com/locate/jmmm

# Simulations of irreversibilities of the random-field Ising model order parameter

L.J. Shelton$^{\mathrm{a}}$, F. Ye$^{\mathrm{a}}$, W.C. Barber$^{\mathrm{b}}$, L. Zhou$^{\mathrm{c}}$, D.P. Belanger$^{\mathrm{a},*}$

$^{\mathrm{a}}$Department of Physics, University of California, Santa Cruz, CA 95064, USA
$^{\mathrm{b}}$Department of Radiology, University of California, San Francisco, CA 94080, USA
$^{\mathrm{c}}$T.H. Geballe Laboratory for Advanced Materials, Stanford University, Stanford, CA 94305, USA

## Abstract

Hysteresis observed in experiments below the random-field Ising transition, as realized in dilute antiferromagnets in applied magnetic fields, is characterized in Monte Carlo simulations.

© 2003 Elsevier B.V. All rights reserved.

PACS: 75.50.Lk; 64.60.–i

Keywords: Random-field Ising model; Monte Carlo simulations; Hysteresis

Neutron [1] and X-ray [2] scattering and birefringence [4] experiments in the random-field Ising model (RFIM) antiferromagnet $\mathrm{Fe}_{x}\mathrm{Zn}_{1-x}\mathrm{F}_{2}$, with $x=0.85$ in an applied field have shown critical behavior, measured to $|t|=|(T-T_{\mathrm{c}})/T_{\mathrm{c}}|<10^{-3}$ upon cooling in a field, raising the field and heating through the phase transition (ZFC). The order-parameter exponent $\beta$ can only be measured for $x>x_{v}$, where $x_{v}=0.76$ is the magnetic vacancy percolation threshold concentration [2]. The critical exponents obtained for $x=0.85$ and $H=10$ T, $\beta=0.16\pm0.02$ [2], the staggered susceptibility exponent $\gamma=\nu(2-\eta)=1.68\pm0.09$ [1], and the specific heat exponent $\alpha=0.00\pm0.02$ [4], satisfy the Rushbrooke scaling relation $2\beta+\alpha+\gamma=2$. Latent heat, a signature of a first-order transition, has never been observed in RFIM specific heat measurements [5]. Despite these evidences of the second-order nature of the transition, the specific heat and order parameter show striking hysteresis upon cooling through the transition in the applied field (FC). Hysteresis in the Bragg-scattering intensity (square of the order-parameter) has been observed [2] upon reversing the temperature in the ZFC procedure close to $T_{\mathrm{c}}$. Hence, the system exhibits obvious non-equilibrium behavior with temperature reversals, despite the scaling properties. Although hysteresis in the Bragg scattering has been observed previously [6] for $x=0.52<x_{v}$, $\beta$ could not be determined because of domain formation even upon ZFC below $T_{\mathrm{c}}$.

The present Monte Carlo (MC) simulations serve to complement the magnetic X-ray results for $x=0.85$, to verify that the behavior is intrinsic to the RFIM and to further characterize the hysteresis. The MC techniques are nearly those described earlier [7]. The lattice size is $2L\times L\times L$ with $L=128$, corresponding to $3.6\times10^{6}$ spins. Periodic boundary conditions are imposed. The dilute MC Ising Hamiltonian is

$$
H=J_{2}\sum_{\langle ij\rangle}\varepsilon_{i}\varepsilon_{j}S_{i}S_{j}-h\sum_{i}\varepsilon_{i}S_{i}, \tag{1}
$$

where $S_{i}=\pm2$ and $\varepsilon_{i}=1$ if site $i$ is occupied and zero if not, $J_{2}=3.17$ K and $h=8.73$ K. This approximates the experimental system. The MC value for $J_{2}$ is 0.60 times that of $\mathrm{FeF}_{2}$ so that $T_{\mathrm{c}}(0)$ corresponds roughly to the experiments. The value of $h$ is chosen to have roughly the same shift $T_{\mathrm{c}}(0)-T_{\mathrm{c}}(H)$ as a field $H=10$ T in the real system. The sample is cooled and heated in steps of 0.01 K while magnetic sites are randomly visited an average of $N$ times, where $200<N<15000$, and flipped according to the metropolis algorithm.

*Corresponding author. Tel.: +1-831-459-2871; fax: +1-831-459-3043.
E-mail address: dave@dave.ucsc.edu (D.P. Belanger).

0304-8853/$ - see front matter © 2003 Elsevier B.V. All rights reserved.
doi:10.1016/j.jmmm.2003.12.084

![](./images/812368958001774593_4.jpg)

Fig. 1. MC order-parameter curves for $N=200$. The upper curve is for $H=0$, the next lower one is ZFC at $H=10$ T and the lower dark curve is FC. The light curves, from top to bottom, are temperature reversals after ZFC at $T\approx$0.8, 0.6, 0.4, and 0.2 K below $T_{\rm c}$. The inset is an example of an X-ray scattering [3] reversal for $x=0.85$ and $H=10$ T. The upper curve is ZFC and the reversal is at 0.1 K below $T_{\rm c}$.

The observation of hysteresis in the MC simulations, shown in Figs. 1 and 2, demonstrates non-equilibrium behavior. This contrasts equilibrium MC and exact ground state calculations on small lattices which yield strikingly different critical exponents [8]. It may well be that the experimental phase transition is an intrinsically non-equilibrium one, even while a diverging correlation length governs the scaling behavior.

Work at UCSC supported by Department of Energy Grant No. DE-FG03-87ER45324. Work at Stanford was supported by the US Department of Energy under Contracts No. DE-FG03-99ER45773 and No. DE-AC03-76SF00515, by NSF Grants No. DMR-9985067 and No. DMR-9802737.

![](./images/812368958001774593_5.jpg)

Fig. 2. MC $N=1000$ hysteresis loops. The upper dark curve is ZFC and the lower dark curve is a reversal at 0.6 K below $T_{\rm c}$. The light curves are from heating after the reversal curve reached 64.7 and 64.2 K for the lower and upper curves, respectively.

### References
[1] F. Ye, et al., J. Magn. Magn. Mater., this issue, doi: 10.1016/j.jmmm.2003.12.081.
[2] F. Ye, et al., Phys. Rev. Lett. 89 (2002) 157202.
[3] F. Ye, L. Zhou, L.J. Shelton, S.A. Meyer, L. Lu, D.P. Belanger, M. Greven, unpublished.
[4] F. Ye, D.P. Belanger, unpublished.
[5] Z. Slanic, D.P. Belanger, J. Magn. Magn. Mater. 186 (1998) 65.
[6] D.P. Belanger, et al., Phys. Rev. B 54 (1996) 3420.
[7] W.C. Barber, D.P. Belanger, J. Magn. Magn. Mater. 226-230 (2001) 545.
[8] A.A. Middleton, D.S. Fisher, Phys. Rev. B 65 (2002) 134411;
A.K. Hartmann, A.P. Young, Phys. Rev. B 64 (2001) 214419.