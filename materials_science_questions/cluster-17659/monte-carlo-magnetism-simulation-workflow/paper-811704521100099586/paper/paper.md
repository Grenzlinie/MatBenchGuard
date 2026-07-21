![](./images/811704521100099586_1.jpg)

Available online at www.sciencedirect.com

![](./images/811704521100099586_2.jpg)

Physics Procedia 9 (2010) 54-57

# Physics
## Procedia

www.elsevier.com/locate/procedia

# 12th International Conference on Magnetic Fluids

## Monte Carlo model for the dynamic magnetization of microspheres

### P.V. Melenev$^{a,b,*}$, R. Perzynski$^{b}$, Yu.L. Raikher$^{a}$, V.V. Rusakov$^{a}$

$^{a}$ Institute of Continuous Media Mechanics, Ural Branch of RAS, 1 Korolyov street, 614013, Perm, Russia
$^{b}$ Laboratoire PECSA, Batiment F, Université Pierre et Marie Curie, 4, place Jussieu, 75252, Paris Cedex 05, France

## Abstract
Monte Carlo method with a variable number of calculation steps is used for simulations of the magnetization dynamics in a microsphere consisting of a non-magnetic core coated with a layer of magnetic nanograins. Namely, the dynamic magnetic hysteresis under an AC field in such a core-shell microsphere is considered for the cases of non-interacting particles and with allowance for the interparticle dipole-dipole interaction. The time portions corresponding to one calculation step are estimated from comparison of the Monte Carlo-Metropolis results and a numerically-exact solution of the kinetic equation.

© 2010 Published by Elsevier Ltd

**Keywords:** soft magnetic matter; magnetic microspheres; dynamic magnetic hysteresis; hyperthermia

## 1. Introduction
Self- or guided organization of magnetic nanoparticles in multi-particle entities, being a ubiquitous nuisance in preparation of perfect magnetic fluids, becomes a goal in a number of applications where enhanced local concentrations are necessary. This objective in its 3D and 2D variants is realized in the form of magnetic vesicles [1], micro-aggregates [2], and microspheres [3–6] of various types. The methods of synthesis of magnetic microspheres (MMS’s) are by now well developed yielding the objects of diverse material content with the diameters from hundreds of nanometers [4] to tens of microns [3]. We remark that the references above are merely examples since the pertinent literature is indeed huge.

The enhanced local density of particles is important, for example, for hyperthermia applications, as the redistribution of the magnetic phase changes drastically the conditions of heat exchange at the mesoscopic scale. Obviously, employment of MMS’s together or instead of individual nanoparticles as the microgenerators, which transform the power of an AC magnetic field into heat, widens greatly the abilities of the magnetodynamic hyperthermia techniques. Even not counting other applications, this alone proves that nanodesign of microspheres is

* Corresponding author. Tel.: +7-342-237-8323; fax: +7-342-237-8487.
E-mail address: melenev@icmm.ru

1875-3892 © 2010 Published by Elsevier Ltd
doi:10.1016/j.phpro.2010.11.014

an important line of work in physico-chemistry of ultradisperse magnetics.

Given highly developed modern methods of instrumental visualization, the morphology of the obtained MMS's could be studied quite accurately, rendering not only the shapes of individual objects but also the details of their surface structure. Meanwhile, the methods of magnetic characterization of MMS's, being of crucial importance for optimization of the induction heating, have far lower resolution. In fact, with conventional techniques (including SQUIDs) only large assemblies comprising many thousands of MMS's could be measured. In this situation, computer modeling of the magnetic properties of MMS's takes the role of a high-resolution tool delivering the necessary info on magnetic susceptibility, coercive force, magnetization, etc. Moreover, the hyperthermia use requires these characteristics not as static parameters but as functions of the strength and frequency of the applied field.

### 2. Model and method
A single microsphere typically bears from tens to tens of thousands nanoparticles. Even if the latter are spatially fixed, so that the set of variables comprises only the orientation angles of the particle magnetic moments, one indeed deals with a statistical ensemble. To describe the behavior of such a system, we employ the Monte Carlo method with Metropolis algorithm. When applied in a conventional form, this procedure renders the free energy minimum and enables one to find the ground state and the equilibrium magnetic characteristics of an MMS [7,8].

The Monte Carlo method has, however, a very attractive modification that extends it to kinetics. Namely, the number of Monte Carlo steps is interpreted as "calculation" time, so that under appropriate ensemble averaging the set of states passed by the system is assumed to resemble its real time-dependent behavior, see [9], for example. The crucial point of this approach is the quantification of the calculation time in the real time units [10]. Hereby we consider a non-equilibrium magnetization of an MMS assuming direct proportionality between the number $N$ of Monte Carlo steps and the time $t$.

The model system is a non-magnetic microsphere resting at a finite temperature $T$ in a solid environment. The microsphere surface is covered with a dilute monolayer of identical uniaxially anisotropic single-domain particles. The particle centers of mass and easy axes are distributed at random, the only restriction is that overlapping of the particles is forbidden. To characterize the magnetic state of such an MMS three dimensionless parameters are used:

$$
\xi=\mu H / k T, \quad \sigma=E_{A} / k T, \quad \lambda=\mu^{2} /\left(k T a^{3}\right), \quad(1)
$$

where $\mu$ is the particle magnetic moment, $E_{A}$ its anisotropy energy, and $a$ the mean interparticle distance at the MMS surface. In these units, the maximal quasistatic (Stoner-Wohlfarth) coercive force of the particle equals $\xi_{c}=2 \sigma$.

The simulation is done as follows. At each step, the magnetic moment of each particle is rotated from its former direction by an angle $\delta$ chosen at random from the interval $[-\Delta, \Delta]$. The energy of the ensemble in the new state is calculated and the acceptance probability for $\delta$ is found with the standard Metropolis procedure.
In Ref. 10, to establish the relation between $N$ and $t$, the authors, first, evaluated the mean square angular displacement $\overline{\delta^{2}}(\Delta)$ of the particle magnetic moment resulting from one Monte Carlo step, and then identified it with the displacement attained in result of the magnetic moment rotary diffusion: $\overline{\delta^{2}}=2 D t$. The corresponding diffusion coefficient

$$
D=1 / 2 \tau_{D}, \quad \tau_{D}=\mu\left(1+\alpha^{2}\right) / 2 \alpha \gamma k T=\tau_{0} \sigma \quad(2)
$$

follows from the fluctuation-dissipation theorem applied to a linearized Landau-Lifshitz-Gilbert equation; here $\tau_{D}$ is the rotary diffusion time, $\gamma$ the gyromagnetic ratio, while $\alpha$ and $\tau_{0}$ are the precession damping parameter and precession damping time.

Thus obtained ratio $\overline{\Delta t}=\overline{\delta^{2}} / D$ is claimed to be the duration of one Monte Carlo step in the real time scale. It is essential that the angle perturbation $\Delta$ must be small enough to ensure $\overline{\delta^{2}}<<1$ and to justify neglecting the influence of the external and anisotropy fields. Therefore, the approximation [10] is by definition valid only for the systems with sufficiently low energy barriers $(\sigma \leq 1)$ and subjected to weak fields $(\xi \leq 1)$.

In the majority of practically interesting situations one needs to deal with $\sigma$ and/or $\xi$, which are substantially

greater than unity. To get the results in a plausible calculation time, rather large angle perturbations $\Delta$ are to be used, so that $\delta^{2} \sim 1$ becomes a probable enough occasion. Going that far beyond the hypothesis [10], it becomes necessary to have an $N$-to-$t$ rescaling law appropriate for the case. To find such, we take a periodic process and juxtapose the Monte Carlo and real kinetic results "globally", i.e., with respect to the full period.

Following this idea, we consider the dynamic magnetic hysteresis induced in an MMS by a linearly polarized AC field of the amplitude $\xi_{0}=\xi_{c}$. In the simulation, the oscillating field $\xi_{0} \cos \omega t$ is replaced by a stepwise regime consisting of $m$ stages differing in the field strength by a fixed value $\Delta \xi=2 \xi_{0} / m$. At each stage, the field is kept constant, and a number $n$ of Monte Carlo steps is performed.

### 3. Results and Discussion
As a benchmark process, we take the dynamic hysteresis loops obtained numerically [11] from the Brown's kinetic equation. In Fig. $1\left\langle\mu_{z}\right\rangle / \mu$ the normalized projection of the magnetic moment on the field direction is plotted. The Monte Carlo simulation is done at $\Delta=$ const for an MMS containing $10^{3}$ nanoparticles with randomly distributed positions and easy axes directions. The only adjustment parameter is the number $n$ of steps per stage. Other essential parameters are given in Table 1 along with the obtained estimations of the real time portions (in units of $\tau_{0}$ ) corresponding to one calculation step.

![](./images/811704521100099586_3.jpg)

Fig. 1. Dynamic hysteresis loops of an MMS with non-interacting particles for the anisotropy parameter $\sigma=2$ (crosses and solid line), $\sigma=5$ (empty circles and dashed line) and $\sigma=15$ (solid circles and dotted line) in an AC field of frequency $\omega \tau_{0}=0.01$. Symbols represent MC simulations, lines show solutions [11] of the kinetic equation.

![](./images/811704521100099586_4.jpg)

Fig. 2. The effect of dipole-dipole interactions on the shape of the dynamic hysteresis loop in the field with frequency $\omega \tau_{0}=10^{-3}$ of an MMS with 100 (dots), 500 (empty circles) and 1000 (stars) particles; solid line shows the numerical solution of the kinetic equation for the system without interaction.

Table 1. For the results, presented in Fig.1: simulation
parameters and estimations of the time corresponding to one
calculation step with the attempt amplitude $\Delta=0.25$ .

<table>
<thead>
<tr>
<th></th>
<th>$\sigma=2$</th>
<th>$\sigma=5$</th>
<th>$\sigma=15$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$m$</td>
<td colspan="3">80</td>
</tr>
<tr>
<td>$n$</td>
<td>100</td>
<td>45</td>
<td>16</td>
</tr>
<tr>
<td>$\Delta t$</td>
<td>$0.08\tau_{0}$</td>
<td>$0.17\tau_{0}$</td>
<td>$0.49\tau_{0}$</td>
</tr>
</tbody>
</table>

An important advantage of any Monte Carlo model is that interparticle interactions are included there in a very easy way. Fig. 2 illustrates the effect of the magnetic dipole-dipole coupling on the simulated dynamic hysteresis loop of an MMS. As expected, the interaction widens the loops. The dipole-dipole parameter $\lambda$ is defined by Eq. (1). We consider an MMS of diameter 200 nm, where a filled-in monolayer would have contained about $2{\times}10^{3}$ nanoparticles of 8 nm size. The shown values of $\lambda$ correspond, respectively, to the particle numbers 100, 500 and 1000 thus presenting the cases of dilute as well as dense monolayers. The magnetic material parameters are taken for maghemite: $M_{s}=400$ G and $K=2{\times}10^{5}\ \mathrm{erg/cm^{3}}$; the temperature is 28 K.

### 4. Conclusions
1.  Monte-Carlo-Metropolis simulations of the magneto-dynamics of a microsphere bearing an ensemble of superparamagnetic nanoparticles are performed.
2.  The simulated dynamic hysteresis loops of a microsphere subjected to a strong AC field are obtained in good agreement with the same rendered by consistent kinetic calculations.
3.  A procedure relating the number of Monte Carlo steps to real time intervals is proposed and tested.
4.  An example is given of including the magnetic dipole-dipole interparticle interactions in the model.

### Acknowledgements
We acknowledge partial support from projects: RFBR 08-02-00802, RFBR-CNRS 09-02-91070 (PICS 4825), 02.740.11.0442 and AATP 2.1.1/4463 from Russian Ministry of Education and Science.

### Reference
[1] S. Lecommandoux, O. Sandre, F. Chécot, R. Perzynski, Progr. Solid State Chem. 34 (2006) 171.
[2] B. Frka-Petesic, J. Fresnais, J.F. Berret, V. Dupuis, R. Perzynski, O. Sandre, J. Magn. Magn. Mater. 321 (2009) 667.
[3] M. Kawashita, S. Domi, Y. Saito, M. Aoki, Y. Ebisawa, T. Kokubo, T. Saito, M. Takano, N. Araki, M. Hiraoka, J. Mater. Sci: Mater. Med. 19 (2008) 1897.
[4] H. Pua, F. Jiang, Z. Yang, Mater. Chem. Phys. 100 (2006) 10.
[5] A. Schlachter, M.E. Gruner, M. Spasova, M. Farle, P. Entel, Phase Transitions 78 (2005) 741.
[6] E. M. Claesson, A.P. Philipse, Langmuir 21 (2005) 9412.
[7] M. E. Gruner, P. Entel, J. Magn. Magn. Mater. 310 (2007) 2453.
[8] P. V. Melenev, V. V. Rusakov, Yu. L. Raikher, R. Perzynski, J. Magn. Magn. Mater. 321 (2009) 663.
[9] M. Ulrich, J. Garcia-Otero, J. Rivas, A. Bunde, Phys. Rev. Lett. 84 (2000) 167.
[10] U. Nowak, R. Chantrell, E. Kennedy, Phys. Rev. Lett. 84 (2000) 163.
[11] I. S. Poperechny, Yu. L. Raikher, V. I. Stepanov, Bull. Russian Acad. Sci.: Physics 74 (2010) 1443.