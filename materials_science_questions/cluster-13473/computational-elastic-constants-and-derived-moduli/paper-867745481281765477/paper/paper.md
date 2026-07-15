# Molecular Dynamics Simulation of Shear Moduli for Coulomb Crystals

C. J. Horowitz* and J. Hughto†
Department of Physics and Nuclear Theory Center, Indiana University, Bloomington, IN 47405
(Dated: October 22, 2021)

Torsional (shear) oscillations of neutron stars may have been observed in quasiperiodic oscillations of Magnetar Giant Flares. The frequencies of these modes depend on the shear modulus of neutron star crust. We calculate the shear modulus of Coulomb crystals from molecular dynamics simulations. We find that electron screening reduces the shear modulus by about 10% compared to previous Ogata et al. results. Our MD simulations can be extended to calculate the effects of impurities and or polycrystalline structures on the shear modulus.

PACS numbers: 62.20.de, 97.60.Jd, 52.27.Gr

Recently quasi-periodic oscillations (QPOs) have been observed in the tails of Magentar Giant Flares [1][2]. These flares are extremely energetic $\gamma$-ray bursts from very strongly magnetized neutron stars. The QPOs have been interpreted as shear oscillations of the crust [3],[4]. If this interpretation is correct, the QPO frequencies could provide detailed information on neutron stars and their crusts [5]. The frequencies of shear modes depend on shear moduli of neutron star crust which is a Coulomb solid. Ogata et al. [6] have calculated shear moduli using Monte Carlo simulations. In this paper we improve on the Ogata et al. results by presenting molecular dynamics simulations with much better statistics and we include the effects of electron screening.

Our results for shear moduli are preparation for later molecular dynamics calculations of the breaking strain of neutron star crust [7]. This breaking strain determines the maximum height of neutron star "mountains" before they collapse under their own weight. Mountains on rapidly rotating neutron stars may efficiently radiate gravitational waves [8]. These waves could limit the spin frequencies of accreting stars and may be detectable with large scale interferometers [9]. In addition the breaking strain may be important for crust breaking models of Magnetar Giant Flares [10].

In the crust of a neutron star electrons form a very degenerate relativistic gas. The ions are completely pressure ionized and have Coulomb interactions that are screened at large distances by the slightly polarizable electron gas. The interaction potential between two ions, $v(r)$, is assumed to be [11],
$$
v(r)=\frac{Z^{2} e^{2}}{r} \mathrm{e}^{-r / \lambda_{e}}, \tag{1}
$$
where the ions have chage $Z$, $r$ is the distance between them, and the electron screening length $\lambda_e$ is
$$
\lambda_{e}=\frac{\pi^{1 / 2}}{2 e\left(3 \pi^{2} n_{e}\right)^{1 / 3}} \tag{2}
$$
with $n_e$ the electron density. The total potential energy is $V_{tot}=\sum_{i<j} v(r_{i j})$. Charge neutrality ensures that $n_e=Zn$ where $n$ is the ion density. The ions are assumed to form a classical one component plasma (OCP) that can be characterized by the Coulomb parameter $\Gamma$,
$$
\Gamma=\frac{Z^{2} e^{2}}{a T}. \tag{3}
$$

This parameter is the ratio of a typical Coulomb to thermal energy and the ion sphere radius $a=[3/(4\pi n)]^{1/3}$ characterizes the separation between ions. The OCP is expected to freeze for $\Gamma\geq175$.

To calculate shear moduli, we follow the procedure of Ogata et al. [6]. The change in free energy with deformation $\delta F$ can be expressed in terms of elastic constants $c_{11}$, $c_{12}$ and $c_{44}$,
$$
\delta F=\frac{1}{2}\left(c_{11}-c_{12}\right) u_{i i}^{2}+c_{44} u_{i k} u_{k i} \quad(i \neq k), \tag{4}
$$
and $u_{ik}$ describes the strain.

Under a deformation, the coordinates $r_k$ of an ion get mapped to $r_i'$,
$$
r_{i}^{\prime}=\sum_{k=1}^{3}\left(\delta_{i k}+u_{i k}\right) r_{k}. \tag{5}
$$

We consider six deformations $D_i\ (i=1...6)$ that conserve the volume to order $\epsilon^2$.
$$
D_{1}: \quad u_{x x}=\epsilon+\frac{3}{4} \epsilon^{2}, \quad u_{y y}=u_{z z}=-\frac{\epsilon}{2} \tag{6}
$$

$$
D_{2}: \quad u_{y y}=\epsilon+\frac{3}{4} \epsilon^{2}, \quad u_{x x}=u_{z z}=-\frac{\epsilon}{2} \tag{7}
$$

$$
D_{3}: \quad u_{z z}=\epsilon+\frac{3}{4} \epsilon^{2}, \quad u_{x x}=u_{y y}=-\frac{\epsilon}{2} \tag{8}
$$

$$
D_{4}: \quad u_{x y}=u_{y x}=\frac{\epsilon}{2}, \quad u_{z z}=\frac{\epsilon^{2}}{4} \tag{9}
$$

$$
D_{5}: \quad u_{y z}=u_{z y}=\frac{\epsilon}{2}, \quad u_{x x}=\frac{\epsilon^{2}}{4} \tag{10}
$$

*Electronic address: horowit@indiana.edu
†Electronic address: jhughto@astro.indiana.edu

$$
D_{6}: \quad u_{z x}=u_{x z}=\frac{\epsilon}{2}, \quad u_{y y}=\frac{\epsilon^{2}}{4} \tag{11}
$$

For each deformation $D_{m}$ we calculate a corresponding expectation value $f_{m}(m=1...6)$,
$$
f_{m}=\frac{1}{V}\left\{\left\langle\frac{d^{2} V_{t o t}}{d \epsilon^{2}}\right\rangle-\frac{1}{T}\left[\left\langle\left(\frac{d V_{t o t}}{d \epsilon}\right)^{2}\right\rangle-\left\langle\frac{d V_{t o t}}{d \epsilon}\right\rangle^{2}\right]\right\}, \tag{12}
$$
where $V$ is the system volume. At zero temperature, this reduces to $f_{m}=(d^{2} V_{t o t} / d \epsilon^{2}) / V$.

For a body centered cubic crystal one has [6],
$$
f_{1}=f_{2}=f_{3}=3 b_{11}=3\left(c_{11}-c_{12}\right) \tag{13}
$$
and
$$
f_{4}=f_{5}=f_{6}=c_{44}. \tag{14}
$$

Here $c_{11}, c_{12}$, and $c_{44}$ are elastic constants. In practice we calculate all six $f_{m}$ independently and average to determine $b_{11}$ and $c_{44}$. The angle averaged shear modulus is [6],
$$
\mu_{\text {eff }}=\left(2 b_{11}+3 c_{44}\right) / 5. \tag{15}
$$

If neutron star crust involves many crystal domains of random orientation, then $\mu_{\text {eff }}$ is the appropriate elastic constant to determine the speed of shear waves.

The shear modulus is sensitive to the very long range tails of the interactions. To study this we cut off the potential at a large distance $R_{\text {cut }}$,
$$
v(r) \rightarrow v_{\mathrm{cut}}(r)=\left[v(r)-v\left(R_{\mathrm{cut}}\right)\right] \Theta\left(R_{\mathrm{cut}}-r\right). \tag{16}
$$

We have subtracted a constant so that $v_{\text {cut }}(r)$ is continuous at $r=R_{\text {cut }}$. In Fig. 1 we plot the elastic constants $b_{11}$ and $c_{44}$ versus $R_{\text {cut }}$ for a perfect bcc lattice at zero temperature. This figure was calculated assuming $Z=29.4$. We note that the ratio of $\lambda_{e}$ to $a$ is $\lambda_{e} / a=5.41 / Z^{1 / 3}$ independent of density. We see that one must go to very large $R_{\text {cut }}>12 \lambda_{e}$ to calculate both $b_{11}$ and $c_{44}$ accurately. For $R_{\text {cut }} \rightarrow \infty$ we have $\mu_{\text {eff }}=0.1108(n Z^{2} e^{2} / a)$. This is $8\%$ smaller than the value $\mu_{\text {eff }}=0.1194(n Z^{2} e^{2} / a)$ that Ogata et al. [6], calculate in the limit $\lambda_{e} \rightarrow \infty$. We conclude that electron screening , neglected in ref. [6], reduces $\mu_{\text {eff }}$ by about $10\%$.

We now describe our MD simulations at finite temperatures. For simplicity we work at a density $n=7.18 \times 10^{-5}$ $\mathrm{fm}^{-3}$ and $Z=29.4$. Our results can be scaled to other densities at a given value of $\Gamma$. Our results can also be approximately scaled to other values of $Z$, at fixed $\Gamma$. This is because, although the ratio $\lambda_{e} / a$ changes with $Z$, this change in screening has only a small effect on the shear modulus. We evolve the system with the velocity Verlet algorithm [13] using a time step $\delta t=25 \mathrm{fm} / \mathrm{c}$. Starting from $T=0$ and a perfect bcc lattice we increase the temperature to $T=0.1$ MeV and evolve the system for typically 100000 MD steps $(2.5 \times 10^{6} \mathrm{fm} / \mathrm{c})$ to reach thermal equilibrium. Next we evolve for a further

![](./images/867745481281765477_1.jpg)

FIG. 1: (Color on line) Elastic constants $3b_{11}$ and $c_{44}$ versus cutoff distance $R_{\text {cut }}$ for a perfect bcc lattice at zero temperature. The cutoff distance is in units of the electron screening length $\lambda_{e}$.

$250000$ MD steps $(6.25 \times 10^{6} \mathrm{fm} / \mathrm{c})$ storing configurations for later calculations of elastic constants. The temperature is then raised by of order $0.1$ MeV and the process repeated. We keep the system at a fixed temperature (approximately) by periodically rescaling the velocities. These MD simulations are done in an undistorted cubic box using periodic boundary conditions.

We calculate $f_{m}$ by averaging over 1000 configurations, each separated by 250 MD steps (6250 fm/c). To minimize finite size effects we calculate $V_{\text {tot }}$ by summing over all 27 nearest periodic images. Thus ion $i$ is assumed to interact not only with ion $j$ at its original position but also with 26 more images of $j$ where the x, y, and z coordinates are independently shifted by $0, +l$, or $-l$, with $l$ the box size. The derivatives in Eq. 12 are approximated using a five point numerical formula. We note that the MD trajectories have been calculated using periodic distances (involving only the single nearest periodic image of a given ion) to save time, while the derivatives have been calculated by summing over 27 images to minimize finite size effects.

Table I presents results for simulations using $N=3456$ ions and no cutoff $R_{\text {cut }}=\infty$. Statistical errors only are indicated in parentheses. We caution that $b_{11}$ may have significant errors from finite size and other systematic effects. Indeed Fig. 1 suggests that finite size effects could be large for this small system. However $b_{11}$ only makes a small contribution to $\mu_{\text {eff }}$. Therefore $\mu_{\text {eff }}$ in Table I may be more accurate. We fit the values of $\mu_{\text {eff }}$ in Table I with a simple analytic formula that is valid for all $\Gamma \geq 175$,
$$
\mu_{\mathrm{eff}} \approx\left(0.1106-\frac{28.7}{\Gamma^{1.3}}\right)\left(n \frac{Z^{2} e^{2}}{a}\right). \tag{17}
$$

<table>
<caption>TABLE I: Shear Moduli for MD simulations with $N = 3456$ ions.</caption>
<tbody><tr><th>$\Gamma$</th><td>$b_{11}$ ($nZ^2e^2/a$)</td><td>$c_{44}$ ($nZ^2e^2/a$)</td><td>$\mu_{\rm eff}$ ($nZ^2e^2/a$)</td></tr>
<tr><th>$\infty$</th><td>0.0220</td><td>0.1699</td><td>0.1107</td></tr>
<tr><th>834</th><td>0.0209(2)</td><td>0.1617(3)</td><td>0.1054(2)</td></tr>
<tr><th>417</th><td>0.0194(2)</td><td>0.1517(3)</td><td>0.0988(2)</td></tr>
<tr><th>278</th><td>0.0202(4)</td><td>0.1410(5)</td><td>0.0927(3)</td></tr>
<tr><th>200</th><td>0.0154(5)</td><td>0.1253(10)</td><td>0.0813(6)</td></tr>
<tr><th>175</th><td>0.0158(8)</td><td>0.1152(10)</td><td>0.0755(6)</td></tr>
</tbody></table>

<table>
<caption>TABLE II: Shear Moduli for MD simulations with $N = 9826$ ions using a cutoff $R_{\rm cut} = 13.9\lambda_e$.</caption>
<tbody><tr><th>$\Gamma$</th><td>$b_{11}$ ($nZ^2e^2/a$)</td><td>$c_{44}$ ($nZ^2e^2/a$)</td><td>$\mu_{\rm eff}$ ($nZ^2e^2/a$)</td></tr>
<tr><th>$\infty$</th><td>0.0212</td><td>0.1700</td><td>0.1105</td></tr>
<tr><th>834</th><td>0.0208(2)</td><td>0.1602(2)</td><td>0.1045(1)</td></tr>
<tr><th>200</th><td>0.0177(5)</td><td>0.1224(6)</td><td>0.0805(4)</td></tr>
</tbody></table>

This fit has an error $\leq 2\%$.

To study finite size effects we have performed additional simulations with larger systems. Table II presents results for simulations with $N = 9826$ ions using a cutoff $R_{\rm cut} = 13.9\lambda_e$. For this larger system and for finite $\Gamma$, $\mu_{\rm eff}$ is about $1\%$ smaller in Table II than in Table I. Therefore we estimate finite size effects in Table II to be of order $1\%$. Figure 2 plots these results for $\mu_{\rm eff}$ and in addition shows results for very small simulations with $N = 1024$ ions, where finite size effects are large. Finally, Fig. 2 also shows the Monte Carlo results of Ogata et al. [6]. These results are about $10\%$ larger than our results at large $\Gamma$ and have much larger statistical errors.

Ogata et al. neglect electron screening $\lambda_e \to \infty$. At zero temperature we have performed calculations for larger values of $\lambda_e$ and extrapolated to $\lambda_e \to \infty$. Note that we can not directly calculate for $\lambda_e = \infty$. Our extrapolated results are consistent with Ogata et al. Therefore we conclude that electron screening reduces $\mu_{\rm eff}$ by about $10\%$. The speed of shear waves is proportional to the square root of $\mu_{\rm eff}$. Therefore electron screening reduces the shear speed by about $5\%$. This will slightly lower the frequency of torsional oscillations of neutron star crusts.

In future work, we will study the impact of impurities on $\mu_{\rm eff}$ by explicitly including them in our MD simulations [12]. We expect impurities to lower the shear modulus because they reduce the uniformity of the crystal. We will also study the effect of polycrystalline structure on $\mu_{\rm eff}$ with larger scale MD simulations that include multiple crystal domains. These multiple domains could also lead to a lower effective shear modulus. Finally, we will calculate the breaking strain by slowly deforming the simulation volume and calculating the resulting stress. The breaking strain is important for the maximum height of mountains on neutron stars that could be important for gravitational wave radiation. In addition, the breaking strain is important for star "quakes" that may trigger Magnetar Giant Flares.

In conclusion, we have calculated the shear modulus of a Coulomb plasma using MD simulations. The shear modulus is important for the frequencies of torsional oscillations of neutron star crusts. Our results for the angle averaged shear modulus $\mu_{\rm eff}$ are, $\mu_{\rm eff} \approx (0.1106 - 28.7/\Gamma^{1.3})(nZ^2e^2/a)$. Here $n$ is the ion density, $Z$ the ion charge, and $a$ the ion sphere radius, $a = (3/4\pi n)^{1/3}$. This formula is accurate to about $2\%$ and valid for Coulomb parameter $\Gamma \geq 175$. Our results are about $10\%$ smaller than Ogata et al because we include electron screening.

![](./images/867745481281765477_2.jpg)

FIG. 2: (Color on line) Angle averaged shear modulus $\mu_{\rm eff}$ versus Coulomb parameter $\Gamma$ for MD simulations involving $N = 1024$, 3456, and 9826 ions. Also shown are Monte Carlo results from Ogata et al. [6] that omit electron screening.

We thank Don Berry, Kai Kadau, and Andrew Steiner for helpful discussions. This work was supported in part by DOE grant DE-FG02-87ER40365.

[1] G. Isreal et al., ApJ. 628 (2005) L53.
[2] Tod E. Strohmayer and Anna L. Watts, ApJ. 632 (2005) L111.
[3] T. Strohmayer, S. Ogata, H. Iyetomi, S. Ichimaru, and H. M. Van Horn, ApJ 375 (1991) 679.
[4] Anthony L. Piro, ApJ. 634 (2005) L153.
[5] Lars Samuelsson and Nils Andersson, Mon. Not. Roy. Astron. Soc. 374 (2007) 256.

[6] Shuji Ogata and Setsuo Ichimaru, Phys. Rev. A **42** (1990) 4867.

[7] C. J. Horowitz and K. Kadau, to be published.

[8] G. Ushomirsky, C. Cutler, and L. Bildsten, MNRAS **319** (2000) 902.

[9] A. L. Watts, B. Krishnan, L. Bildsten, and B. F. Schutz, MNRAS **389** (2008) 839.

[10] C. Thompson and R. C. Duncan, ApJ. **561** (2001) 980.

[11] A. L. Fetter and J. D. Walecka, Quantum Theory of Many Body Systems (McGraw-Hill, New York,1971), p. 175.

[12] C. J. Horowitz, D. K. Berry, and E. F. Brown, PRE **75** (2007) 066101.

[13] L. Verlet, Phys. Rev. **159**, 98 (1967). F. Erco- lessi, A Molecular Dynamics Primer, available from http://www.sissa.it/furio/ (1997).