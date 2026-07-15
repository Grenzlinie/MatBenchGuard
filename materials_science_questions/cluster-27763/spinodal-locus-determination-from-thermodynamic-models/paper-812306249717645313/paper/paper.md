# Nucleation near the Spinodal in Long-Range Ising Models

T. S. Ray $^{1,2}$ and W. Klein $^{1}$

Received June 2, 1990

Properties of metastable long-range Ising models (LRIMs) are studied for deep quenches near the mean-field spinodal with Monte Carlo simulations using Glauber dynamics. The theory of spinodal-assisted nucleation is found to agree well with the data. Nucleating droplets are shown to have the same structure as large clusters in random long-range bond percolation.

**KEY WORDS:** Nucleation; spinodal; metastability; mean-field; percolation; Ising model.

## 1. INTRODUCTION

The classical theory of nucleation is based on phenomenological models where it is generally assumed that nucleating droplets are local fluctuations of the stable phase. $^{(1)}$ The droplets are compact objects with a well-defined surface and volume. The results of classical nucleation theory are consistent with the behavior of many experimental systems and with simulations of metastable nearest-neighbor Ising models. $^{(1-4)}$ The work of Langer, $^{(5)}$ based on a quasiequilibrium treatment of the ferromagnetic metastable Ising model, provides more of a "first principles" justification for the assumptions of classical nucleation theory. It is shown that these assumptions hold near the condensation point for temperatures well below the critical value $T_{c}$.

Several years ago, this work was extended to long-range Ising models (LRIMs) with large values of the external field $H$ which put the system

\(^{1}\) Center for Polymer Studies and Department of Physics, Boston University, Boston, Massachusetts 02215.
\(^{2}\) HLRZ c/o Forschungszentrum Jülich, D-5170 Jülich 1, Federal Republic of Germany.

891
---
822/61/3-4-25
0022-4715/90/1100-0891\$06.00/0 (C) 1990 Plenum Publishing Corporation

near the spinodal. $^{(6,7)}$ In mean-field approximations, the spinodal is the sharp boundary dividing the metastable and unstable regimes. $^{(1)}$ Increasing the range of interaction between spins makes it possible to quench the system arbitrarily close to the spinodal. $^{(8)}$ Many features of the metastable state were found to be radically different. For example, the nucleating droplet was discovered to be a critical fluctuation whose linear size is given by the correlation length. The correlation length diverges at the spinodal in a manner analogous to the behavior at the critical point. Also, the struc- ture of the nucleating droplet is quite different than that assumed in classi- cal nucleation theory. Rather than a fluctuation of the stable phase, the spinodal-assisted nucleating droplet is ramified and fractal-like. Additional work showed that there is a smooth transition between the classical droplets of Langer and those near the spinodal. $^{(9)}$ This is expected since the same formalism underlies both results. We will refer to this new type of nucleation as spinodal-assisted nucleation.

Since the completion of the theoretical work, $^{(6-9)}$ there have been several reports of computer simulations which confirm many of the qualitative features of spinodal-assisted nucleation in LRIMs. Heer- mann et al. studied nucleation in 3-dimensional LRIMs using Glauber dynamics (model A). $^{(10)}$ Near the spinodal, the nucleating droplets were found to be ramified objects. Furthermore, the initial growth of the droplets was observed to take place throughout their interior as predicted by spinodal-assisted nucleation theory. This result is much different than the behavior of classical droplets, which initially grow on their surface.

Another result of Heermann et al. $^{(10)}$ concerned the behavior of the quasistatic susceptibility; i.e., the measured fluctuations in the bulk magnetization while the system remains metastable. A marked increase in this quantity was observed as the spinodal was approached. This is consis- tent with the theory, which predicts a divergence in the quasistatic suscep- tibility at the spinodal.

Simulations of 2-dimensional LRIMs using Creutz dynamics(model C) were reported by Monette et al. $^{(11)}$ In this work the qualitative features of the nucleating droplet observed by Heerman et al. were con- firmed, showing that these aspects of spinodal-assisted nucleation are independent of dynamics (i.e., quasiequilibrium). In addition, the radius of gyration of the nucleating droplets was seen to approach the calculated value of the correlation length, $\xi=R(\Delta T)^{-1 / 2}$ , as the system was initialized closer to the spinodal. Here $\Delta T=(T_{s}-T) / T_{s}$ , where $T_{s}$ is the temperature at the spinodal line, and $R$ is the range of interaction between spins.

As of this paper, the theory of spinodal-assisted nucleation is reasonably supported by the Monte Carlo simulation data. There are, however, two major issues which remain unresolved. First, although the

theory is based on a second-order singularity at the spinodal, no measurements of mean-field exponents have been reported from LRIM simulation data. Second, even though the nucleating droplets are proposed to be fractal objects, their fractal dimension and other scaling properties are not completely understood and have not been measured.

The present work addresses these two points. Section 2 contains a description of the computational methods and of the system used in the simulations. In Section 3 the nature of the quasistatic susceptibility divergence observed by Heermann et al. $^{(10)}$ is investigated. The behavior of metastable LRIMs appears to approach that of a Curie-Weiss (mean-field) system. The mean cluster size of the appropriate clusters of spins is also measured. Section 4 focuses on the properties of the nucleating droplets. Data for the correlation length exponent are shown and compared with spinodal-assisted nucleation theory. In addition, data for the mass of the nucleating droplets as a function of the external field are presented. The droplets appear to have a structure which obeys the same scaling properties as clusters the size of the connectedness length in long-range bond percolation. $^{(12)}$

## 2. METHODS AND BACKGROUND

The system used in the simulations is a long-range Ising model (LRIM) in two dimensions. Each spin interacts with all of its neighbors ferromagnetically and with equal strength. The coupling constant is $J=J_{0} / q$, where $q$ is the coordination number. The coupling constant is always positive, so that the system is ferromagnetic. The Hamiltonian for this system is

$$
\mathscr{H}=-J \sum_{i, j} s_{i} s_{j}-H \sum_{i} s_{i} \tag{2.1}
$$

Here the first sum is over all pairs of neighboring spins. The second term is due to the coupling of the spins to a constant external field $H$. The coordination number of the lattice is variable. In the limit where $q \rightarrow \infty$ we expect the system to exhibit mean-field behavior.

The set of spins which interact with a single spin $s_{i}$ is called the neighborhood of $s_{i}$. The neighborhood of $s_{i}$ is bounded by a square box whose sides are parallel to the $x$ and $y$ axes of the lattice. The length of the box is set to $2 R+1$, where $R$ is an integer called the range of interaction. The coordination number is related to $R$ through the equation

$$
q=(2 R+1)^{2}-1 \tag{2.2}
$$

For example, when $R=1$, each spin interacts with its nearest and next-
nearest neighbors and $q=8$ (since the system is in $d=2$).

Glauber dynamics (nonconserved order parameter) was used in the
LRIM simulations. The specific method chosen was the well-known
Glauber-Metropolis (or heat-bath) algorithm. $^{(13)}$ In this algorithm, the
probability to flip a spin $s_{i}$ is computed from the following expression:

$$
P_{\text {flip }}=\frac{\exp \left\{-\beta\left(J\left(\sum_{j} s_{j}\right) s_{i}+H s_{i}\right)\right\}}{\exp \left\{-\beta\left(J\left(\sum_{j} s_{j}\right) s_{i}+H s_{i}\right)\right\}+\exp \left\{+\beta\left(J\left(\sum_{j} s_{j}\right) s_{i}+H s_{i}\right)\right\}}
\tag{2.3}
$$

Here each sum $\sum_{j}$ is over all of the spins $s_{j}$ within the interaction range $R$
of $s_{i}$. A random number between zero and one is sampled from a uniform
distribution. If the random number is smaller than $P_{\text {flip }}$, the spin is flipped.
Otherwise the spin remains unchanged. The time is measured in Monte
Carlo steps per spin. One time step is equivalent to applying the above
process to every spin in the system. The order in which the spins are visited
is random. All systems had a linear size $L=150$. They were run on an
IBM 3090 at Boston University.

Initially the spins are configured so that they are antiparallel to the
external magnetic field. The temperature is then set to $\frac{4}{9} T_{c}$. The system is
allowed to evolve under the heat-bath dynamics. Typically, the evolution of
the metastable LRIM consists of three stages. First, the system relaxes to
quasistatic equilibrium. This usually takes only a few Monte Carlo steps.
Then the system remains metastable for an amount of time which depends
on the value of the nucleation barrier (i.e., the free energy necessary to form
a nucleating droplet in the metastable background). Finally, a nucleating
droplet forms and the system decays to equilibrium by means of the growth
of the droplet. If the external field is too large, the system will decay to
equilibrium without initially relaxing to a metastable state.

The structure of the nucleating droplet is of principal interest. The
long-range potential makes it nontrivial to define the nucleating droplet.
Fortunately, it is possible to identify the droplets by exploiting a mapping
between the metastable system and a correlated long-range bond percola-
tion problem. $^{(6)}$ The critical point in the percolation problem coincides
with the spinodal. Furthermore, the connectedness length scales with the
Ising correlation length. The percolation problem is defined as follows:
After every Monte Carlo step the up spins (i.e., those aligned with $H$) are
considered to be percolation sites. The sites which are neighbors in the
LRIM problem are connected by bonds with probability

$$
p=1-e^{-4 J \beta\left(1-\rho_{s}\right)}
\tag{2.4}
$$

Here $\rho_{s}$ is the density of spins aligned with the field at the spinodal line.

In the limit of large coordination number (i.e., small $J$), one can show from Eq. (2.4) and the fact that the density of sites scales $^{(1)}$ as $(\rho_{s}-\rho) \sim$ $(\Delta H)^{1 / 2}$ that

$$
\Delta p \sim(\Delta H)^{1 / 2} \quad(2.5)
$$

Here $\Delta p=\left(p_{c}-p\right) / p_{c}$, with $p_{c}$ being the critical probability for bond percolation when the density of sites is equal to $\rho_{s}$. Also, $\Delta H=\left(H_{s}-H\right) / H_{s}$, where $H_{s}$ is the value of the external field at the spinodal. This scaling relation links the singular behavior of percolation and Ising quantities.

Statistics are now gathered from the percolation clusters. One of the clusters should grow anomalously large as the simulation proceeds until it dominates the entire system. This cluster is identified as the nucleating droplet. Since the percolation connectedness length and the Ising correlation length are proportional to one another, the nucleating droplet should initially be a patch of sites in the percolation problem with a characteristic linear size equal to the connectedness length.

Although the percolation mapping gives a procedure for isolating the nucleating droplet, the time at which it forms is still not well defined. For example, the droplet could have appeared as a small cluster many time steps before it clearly dominated the system. This necessitates the use of an arbitrary criterion to determine the time of formation. This choice should not affect the scaling properties of the droplet as long as it is consistently applied to every simulation. In this work the particular criterion used is to trace the nucleating droplet back to the first Monte Carlo step in which it was the largest cluster in the system. All of the nucleating droplet's properties are measured at this time. This is roughly equivalent to the criterion used by Monette et al. $^{(11)}$

## 3. QUASISTATIC SUSCEPTIBILITY MEASUREMENTS

First some of the properties of the metastable LRIM will be investigated at small values of the external field $H$ where the metastable state has a long lifetime. The term "long lifetime" means that the simulation run lasts for at least 1500 Monte Carlo steps in the metastable state without decaying to equilibrium. Spinodal-assisted nucleation theory predicts that the lifetime is proportional to $e^{+\beta \Delta F}$, where $\Delta F$ is the nucleation barrier. The barrier is found to obey the following scaling law $^{(6)}$:

$$
\Delta F \sim R^{d}(\Delta H)^{3 / 2-d / 4} \quad(3.1)
$$

Here, $d$ is the dimension of space ( $d=2$ in the simulations). If $\beta \Delta F \gg 1$, the lifetime of the metastable state should be many Monte Carlo steps.

The anomalous behavior of Eq. (3.1) above $d=6$ is currently being investigated. $^{(14)}$

When the metastable system has a long lifetime, one can measure averaged bulk properties. These properties are averaged only over metastable configurations. As long as this restriction is imposed, the system will obey Boltzmann statistics, treating the metastable state as a point of local equilibrium. One of these bulk properties which is of interest is the quasi-static susceptibility $(\chi_{\mathrm{qs}})$. The quasistatic susceptibility is defined to be the averaged fluctuations in the magnetization while the system remains metastable:

$$
\chi_{\mathrm{qs}}=N\left(\left\langle m^{2}\right\rangle_{\mathrm{ms}}-\langle m\rangle_{\mathrm{ms}}^{2}\right)
\tag{3.2}
$$

Here $N$ is the total number of spins in the system and $m$ is the magnetization per spin. The brackets $\langle\cdot\rangle_{\mathrm{ms}}$ indicate an average over metastable configurations. It is necessary to distinguish the quasistatic susceptibility $\chi_{\mathrm{qs}}$ from the ordinary susceptibility $\chi$ (defined as the fluctuations over all configurations of the system). This makes $\chi$ insensitive to the metastable state, since the equilibrium configurations have a much greater weight than the metastable ones.

In the limit where the range of interaction $R$ goes to infinity, the mean-field approximation becomes exact. $^{(6)}$ The limiting behavior of $\chi_{\mathrm{qs}}$ as $R \rightarrow \infty$ can be determined by numerically evaluating the partition function for an Ising model with $N$ spins where all spins interact with one another. The system has a Hamiltonian identical to Eq. (1.1) in all respects except that now $q=N-1$. This is referred to as the Curie-Weiss model. $^{(15)}$ The limiting behavior of this model as $N \rightarrow \infty$ is expected to be the same as that of the LRIM when $R \rightarrow \infty$. The partition function for the Curie-Weiss model may be written as a sum over all possible values of the magnetization $M$:

$$
Z=\sum_{M} \frac{N!}{[(N-M) / 2]![(N+M) / 2]!} e^{+\beta\left(J M^{2}+H M\right)}
\tag{3.3}
$$

Here constant factors have been left out since they do not affect ensemble-averaged quantities. The quasistatic susceptibility may be numerically evaluated from the partition function by considering values of $M$ near the metastable state in accordance with Eq. (3.2) (it is found that $\chi_{\mathrm{qs}}$ is insensitive to the exact cutoff value of $M$). This has been done as a function of $\Delta H$ for $N=1 \times 10^{7}$. In Fig. $1, \chi_{\mathrm{qs}}$ for the Curie-Weiss model as a function of $\Delta H$ is indicated by the dots. The left-hand portion of the curve is

![](./images/812306249717645313_1.jpg)

Fig. 1. Quasistatic susceptibility versus $\Delta H$. Dots are evaluated from the partition function of a Curie-Weiss model. The LRIM data for $R=5,7,15$, and 25 are indicated by squares, crosses, circles, and plusses, respectively.

approaching a slope of $-1 / 2$. This is the correct asymptotic behavior of $\chi_{\mathrm{qs}}$ as predicted by mean-field theory $^{(1)}$:
$$
\chi_{\mathrm{qs}} \sim(\Delta H)^{-\gamma} \quad(3.4)
$$
where the value of $\gamma$ is calculated to be $1 / 2$.

The results from the LRIM simulations are displayed in the same plot. The quasistatic susceptibility $\chi_{\mathrm{qs}}$ is measured in accordance with Eq. (3.2). Each data point is measured from a simulation which lasted 1500 Monte Carlo steps per spin. For each interaction range $R$, nucleation is never observed near the condensation point $(H=0)$. When the system is deeply quenched at large values of $H$, nucleation occurs quickly enough to be easily observed in the simulations (usually within 40 Monte Carlo steps). The particular value of $\Delta H$ where this transition occurs depends upon $R$, as is expected from Eq. (3.1). Systems with large interaction ranges are found to remain metastable closer to the spinodal than those with smaller $R$. The curves end where the system decayed to equilibrium before the simulations finished running.

One can see from the plots the nature of the crossover in the metastable LRIM to mean-field behavior as $R \rightarrow \infty$. For a given $R$, the data follow the Curie-Weiss curve quite closely to the point where nucleating droplets form before the simulation ends. This supports the

notion that the spinodal is driving fluctuations in the system, which leads to an increasing $\chi_{\mathrm{qs}}$. In addition, it suggests that the data are accurate; i.e., 1500 Monte Carlo steps gives an adequate sampling of the distribution of configurations for a good measurement of $\chi_{\mathrm{qs}}$. It is apparent that if the range of interaction $R$ were increased enough, the scaling form of $\chi_{\mathrm{qs}}$ given by Eq. (3.2) would be observed.

It is interesting to note that for small $\Delta H$, the data taken from LRIMs with large $R$ have a slight upward twist which deviates from the Curie-Weiss plot. This behavior is thought to be due to the finite size of $R$ because the values of $\Delta H$ at which it occurs depends upon $R$ (all systems have the same size). In fact, this same effect can be seen in the numerical evaluation of the Curie-Weiss model with a finite number of spins if $\Delta H$ is small enough.

The mean cluster size of the corresponding percolation problem will now be considered to illustrate the relation between the Ising and percola- tion problems. Since the mean cluster size is the second moment of the cluster distribution, it is analogous to the quasistatic susceptibility in the Ising system. The mean cluster size $\langle s\rangle$ is defined in the usual manner:

$$
\langle s\rangle=\sum_{s} s^{2} n_{s} \quad (3.5)
$$

Here $s$ is the mass of a cluster and $n_{s}$ is the number of clusters with mass $s$ divided by the number of sites (i.e., the number of Ising spins parallel to the external field). The mean cluster size diverges at the critical value of the bond probability according to the scaling relation

$$
\langle s\rangle \sim(\Delta p)^{-\gamma_{p}} \quad (3.6)
$$

In the limit $R \rightarrow \infty$, the problem approaches mean-field percolation. Calculations show that $\gamma_{p}=1$. Using the relation between the Ising and percolation scaling, Eq. (2.5), gives

$$
\langle s\rangle \sim(\Delta H)^{-\gamma_{p} / 2} \quad (3.7)
$$

so that a log-log plot of $\langle s\rangle$ versus $\Delta H$ is predicted to yield an asymptotic slope which is equal to $-1 / 2$. Figure 2 is an example of this plot for several different values of $R$. Each data point was obtained from runs of 1500 Monte Carlo steps per spin. The dashed line drawn in the plot has a slope of $-1 / 2$. It appears that as the range of interaction increases, the mean cluster size plot is tending toward the line.

The upward twists which were observed in the $\chi_{\mathrm{qs}}$ data close to the point where nucleating droplets rapidly form are even more pronounced in

![](./images/812306249717645313_2.jpg)

Fig. 2. Mean cluster size of percolation clusters versus $\Delta H$ for LRIM systems with several values of $R$. Data for $R=5$, 7, 15, and 25 are indicated by squares, crosses, circles, and plusses. The dashed line has a slope $-1/2$, which is predicted by spinodal-assisted nucleation theory.

the mean cluster size plot. Again, these deviations are probably due to the finite size of the interaction range, since their location in the plot depends upon $R$.

## 4. PROPERTIES OF THE NUCLEATING DROPLET

One of the most important results of spinodal-assisted nucleation is that the nucleating droplet has a different structure than that assumed in the classical theory. Instead of a compact object made up of the stable phase, the droplet that forms near the spinodal is predicted to be a diffuse patch of correlated spins with a linear size equal to the correlation length. As the system is quenched closer to the spinodal, the correlation length diverges and the density of the nucleating droplet approaches that of the metastable background. The correlation length $\xi$ is found to scale with $\Delta H$ as $^{(6)}$

$$
\xi \sim R(\Delta H)^{-v} \tag{4.1}
$$

where $v$ is calculated to be $1/4$.

This relation can be checked quantitatively in the following manner: First, $\Delta H$ is lowered for a system with fixed $R$ until a nucleation event is

observed within 20-40 Monte Carlo steps for roughly half of the runs. The values of $\Delta H$ are slightly smaller than those where the $\chi_{\mathrm{qs}}$ plots in Fig. 1 end for each $R$. The nucleating droplet is identified using the percolation mapping described in Section 2. Then, the radius of gyration $R_{G}$ of the nucleating droplet is measured. This quantity is predicted by Eq. (4.1) to scale as the correlation length. The procedure used to identify the nucleating droplet is described in Section 2.

In Fig. 3, the radius of gyration for the nucleating droplet divided by $R$ is plotted against $\Delta H$. Each data point is an average over 12 nucleation events. Assuming that the radius of gyration scales as $\xi$, Eq. (4.1) gives

$$
R_{G} / R \sim(\Delta H)^{-v}
\tag{4.2}
$$

The asymptotic slope is close to the predicted value of $-v\ (-1/4)$ indicated by the dashed line.

The percolation mapping is defined so that the connectedness length is equal to the Ising correlation length. Since the nucleating droplet is iden- tified in the percolation problem as a cluster with linear size which scales as the connectedness length, it is expected to have a fractal structure. For large $R$, the exponents in the percolation problem approach mean-field values. The fractal dimension exponent $d_{f}$ is equal to 4 in mean-field percolation. The correct interpretation of this exponent for long-range bond percolation has been found in systems where the dimension of space

![](./images/812306249717645313_3.jpg)

Fig. 3. Radius of gyration of nucleating droplets divided by $R$ versus $\Delta H$. The dashed line has the predicted asymptotic slope, $-1 / 4$.

![](./images/812306249717645313_4.jpg)

Fig. 4. Mass of nucleating droplets versus $\Delta H$. The dashed line gives the predicted slope, -1.

is less than four. $^{(12)}$ The result is that $d_{f}$ describes the scaling between the mass of percolation clusters $M_{c}$ and their normalized radius of gyration:

$$
M_{c} \sim\left(R_{G} / R\right)^{d_{f}} \tag{4.3}
$$

On the other hand, the Hausdorff dimension of a given cluster $d_{H}$ is found to be the dimension of space. The Hausdorff dimension of a cluster is defined to be how the mass scales with a running length $l$:

$$
M \sim l^{d_{H}} \tag{4.4}
$$

In the case of the nucleating droplet, $R_{G}$ scales as the correlation length. The scaling form of the correlation length, Eq. (4.2), and Eq. (4.3) give the scaling relation for the mass of the nucleating droplet $M_{\mathrm{ND}}$:

$$
M_{\mathrm{ND}} \sim(\Delta H)^{-v d_{f}} \tag{4.5}
$$

Since $v=1 / 4$ and $d_{f}=4$, the exponent is predicted to be equal to -1. In Fig. 4 we have plotted the mass of nucleating droplets averaged over 12 simulations versus $\Delta H$. The points seem to approach the dashed line, which has a slope equal to -1.

## 5. CONCLUSION

This work has shown that singular properties of the spinodal radically affect the quasistatic bulk quantities in the metastable state as well as the phenomenon of nucleation. Near the spinodal, classical nucleation theory breaks down and must be modified. The data presented here seem to be consistent with the predictions of spinodal-assisted nucleation theory. $^{(6-9)}$

The structure of nucleating droplets near the spinodal appears to be the same as that of clusters in random long-range bond percolation. The droplets have a mass which scales as $\xi^{4}$ and a radius of gyration which scales as the correlation length $R_{G} \sim R(\Delta p)^{-1 / 2}$. These same scaling laws are obeyed by the LRBP clusters.

## ACKNOWLEDGMENTS

The authors wish to thank the following colleagues for many stimulat- ing and fruitful discussions: D. Ben-Abraham, D. Considine, F. Leyvraz, L. Monette, D. Stauffer, and P. Tamayo. In addition, they thank Informa- tion Technology for generous allocation of computer resources. This work was supported in part by a grant from the ONR.

## REFERENCES
1. J. Gunton and D. Droz, *Introduction to the Theory of Metastable and Unstable States* (Springer, Berlin, 1983).
2. D. Stauffer, A. Coniglio, and D. W. Heermann, *Phys. Rev. Lett.* 49:1299 (1982).
3. T. S. Ray and P. Tamayo, *J. Stat. Phys.*, in press.
4. T. S. Ray and J.-S. Wang, *Physica A*, in press.
5. J. Langer, *Ann. Phys.* (NY) 14:108 (1967).
6. W. Klein and C. Unger, *Phys. Rev. B* 28:455 (1983).
7. C. Unger and W. Klein, *Phys. Rev. B* 29:2698 (1984).
8. K. Binder, *Phys. Rev. B* 8:3423 (1973).
9. C. Unger and W. Klein, *Phys. Rev. B* 31:6127 (1985).
10. D. W. Heerman, W. Klein, and D. Stauffer, *Phys. Rev. Lett.* 49:1262 (1982).
11. L. Monette, W. Klein, M. Zuckermann, A. Khadir, and R. Harris, *Phys. Rev. B* 38:11607 (1988).
12. T. S. Ray and W. Klein, *J. Stat. Phys.* 53:773 (1988).
13. K. Binder, ed., *Monte Carlo Methods in Statistical Physics* (Springer-Verlag, 1979).
14. T. S. Ray, in preparation.
15. K. Huang, *Statistical Mechanics* (Wiley, 1963).

Communicated by D. Stauffer