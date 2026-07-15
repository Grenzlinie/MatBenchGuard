Faraday Discuss., 1997, 106, 93-104

# Simulation of adsorption and diffusion of hydrocarbons in zeolites

Berend Smit, $^{*, \dagger a}$ L. Daniël J. C. Loyens $\ddagger^{b}$ and Guy L. M. M. Verbist $\S^{c}$

$^{a}$ Department of Chemical Engineering, Universiteit van Amsterdam,
Nieuwe Achtergracht 166, 1018 WV Amsterdam, The Netherlands
$^{b}$ Shell International Exploration and Production B.V., Research and Technical Services,
Volmerlaan 8, 2288 GD Rijswijk, The Netherlands
$^{c}$ Shell International Oil Products B.V., P.O. Box 38000, 1030 BN Amsterdam,
The Netherlands

Molecular simulations are used to investigate the energetics and siting of linear and branched alkanes in the zeolite silicalite. The calculated heats of adsorption of the branched alkanes are in good agreement with the experi- mental data. The simulations show a striking difference between the behav- iour of linear and branched alkanes. The linear alkanes are relatively free to move in all channels of the zeolites. The branched alkanes are trapped with their CH group in the intersection of the zig-zag and straight channels of silicalite. This trapping of the branched alkanes suggests that diffusion of these molecules is an activated process; most of the time the molecule is located in the intersection but, occasionally, it hops from one intersection to another. The straight and zig-zag channels form a barrier for the diffusion. We present some preliminary calculations of this hopping rate, from which the diffusion coefficient can be calculated. These preliminary results are in reasonable agreement with experimental data.

## 1 Introduction

The catalytic conversion of molecules inside the pores of a zeolite can be seen schemati- cally as a three-step process; adsorption and diffusion of the reactants in the pores of the zeolites, catalytic conversion at the active site and, finally, diffusion and desorption of the products. Each of these steps contributes to the overall activity of a zeolite. To understand the shape selectivity of a given zeolite it is, therefore, important to have a detailed understanding of the sorption and diffusion of the molecules in the pores of a zeolite. Experimentally, it is difficult to obtain this type of information under reaction conditions and therefore computer simulations could be a possible alternative.

In principle, the conventional simulation techniques, such as molecular dynamics (MD) or the Monte Carlo (MC) method, can be used to obtain this type of information. However, in practice, it turns out that these techniques are limited to the sorption and diffusion of relatively small molecules. The diffusion of these small molecules or atoms is sufficiently high, such that within a reasonable amount of CPU time a representative part of the zeolite is sampled (for a review, see ref. 1). For hydrocarbons, this implies that

$\dagger$ E-mail: smit@chemeng.chem.uva.nl
$\ddagger$ E-mail: D.LOYENS@siep.shell.com
$\S$ E-mail: verbist1@siop.shell.nl

standard MD can be used efficiently to simulate the diffusion and sorption of methane, ethane and propane. $^{2,3}$ If we increase the number of carbon atoms the CPU time becomes too great. $^{4,5}$ To simulate the thermodynamic properties of long-chain alkanes, it is necessary to use alternative simulation techniques. For example, Smit and co-workers have used the configurational-bias Monte Carlo (CBMC) technique to compute the energetics and siting of linear alkanes in various zeolites. $^{6-9}$ Similar methods have been used by Maginn et al. $^{10}$ In this work we use the CBMC technique to simulate the behaviour of branched hydrocarbons. Branched hydrocarbons are of importance for catalytic dewaxing and alkane isomerisation.

We compare the sorption properties of linear and branched alkanes in silicalite. In particular, we show that the siting of the branched alkanes differs significantly from the siting of the linear alkanes. It is argued that this difference in siting has consequences for the diffusion mechanism of branched alkanes and we present some preliminary results for the diffusion coefficients of these molecules.

## 2 Model and computational details
We focus on alkanes with a single chain-end branch with the structure $(CH_{3})_{2}-CH-(CH_{2})_{n}CH_{3}$. The branched alkanes are described with a united-atom model, *i.e.* $CH_{3}$, $CH_{2}$ and $CH$ groups are considered as single interaction centres. We have used the model of Wang et al. $^{11}$ The pseudo-atoms in different molecules, or belonging to the same molecule, but separated by more than three bonds, interact with each other through a Lennard-Jones potential

$$
u_{ij}^{\mathrm{LJ}}=4\varepsilon_{ij}\left[\left(\frac{\sigma_{ij}}{r_{ij}}\right)^{12}-\left(\frac{\sigma_{ij}}{r_{ij}}\right)^{6}\right] \tag{1}
$$

where $r_{ij}$ is the distance between sites $i$ and $j$. The Lennard-Jones potentials were truncated at $9.626$ Å, and the usual tail corrections have been applied. $^{12}$ The Lennard-Jones parameters used are shown in Table 1. The pseudo-atoms in a given chain are assumed to be connected by rigid bonds ($d_{\mathrm{CC}}=1.53$ Å). Bond bending is modelled by a harmonic

<table>
<caption>Table 1 Parameters for the Lennard-Jones potential describing the interactions between pseudo-atoms of a branched alkane as developed by Wang et al. $^{11}$</caption>
<thead>
<tr>
<th>
</th>
<th>
$(\varepsilon/k_{\mathrm{B}})/\mathrm{K}$
</th>
<th>
$\sigma/\mathrm{\mathring{A}}$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
$\mathrm{CH}_{2}-\mathrm{CH}_{2}$
</td>
<td>
59.38
</td>
<td>
3.905
</td>
</tr>
<tr>
<td>
$\mathrm{CH}_{3}-\mathrm{CH}_{3}$
</td>
<td>
88.06
</td>
<td>
3.905
</td>
</tr>
<tr>
<td>
$\mathrm{CHb}_{3}-\mathrm{CHb}_{3}$
</td>
<td>
80.51
</td>
<td>
3.910
</td>
</tr>
<tr>
<td>
$\mathrm{CH}-\mathrm{CH}$
</td>
<td>
40.25
</td>
<td>
3.850
</td>
</tr>
<tr>
<td>
$\mathrm{CH}_{3}-\mathrm{CH}_{2}$
</td>
<td>
72.31
</td>
<td>
3.905
</td>
</tr>
<tr>
<td>
$\mathrm{CH}_{3}-\mathrm{CHb}_{3}$
</td>
<td>
84.20
</td>
<td>
3.9075
</td>
</tr>
<tr>
<td>
$\mathrm{CH}_{3}-\mathrm{CH}$
</td>
<td>
59.53
</td>
<td>
3.8775
</td>
</tr>
<tr>
<td>
$\mathrm{CH}_{2}-\mathrm{CHb}_{3}$
</td>
<td>
69.14
</td>
<td>
3.9075
</td>
</tr>
<tr>
<td>
$\mathrm{CH}_{2}-\mathrm{CH}$
</td>
<td>
48.89
</td>
<td>
3.8775
</td>
</tr>
</tbody>
</table>

A $\mathrm{CH}_{3}$ group connected to a $\mathrm{CH}$ group is denoted by $-\mathrm{CHb}_{3}$. This group is given a different set of interaction parameters. The interactions are truncated at $R_{\mathrm{c}}=9.626$ Å.

<table><thead><tr><td></td><td><b>$C_{0}$</b></td><td><b>$C_{1}$</b></td><td><b>$C_{2}$</b></td><td><b>$C_{3}$</b></td></tr></thead><tbody><tr><td><b>$CH_{3}-CH_{2}-CH-CHb_{3}$</b></td><td><b>373.0512</b></td><td><b>919.0441</b></td><td><b>268.1541</b></td><td><b>—1737.216</b></td></tr><tr><td><b>$CH_{2}-CH_{2}-CH-CHb_{3}$</b></td><td><b>373.0512</b></td><td><b>919.0441</b></td><td><b>268.1541</b></td><td><b>—1737.216</b></td></tr><tr><td><b>$CH_{2}-CH_{2}-CH_{2}-CH$</b></td><td><b>1009.728</b></td><td><b>2018.446</b></td><td><b>136.341</b></td><td><b>—3164.52</b></td></tr><tr><td><b>$CH_{3}-CH_{2}-CH_{2}-CH$</b></td><td><b>1009.728</b></td><td><b>2018.446</b></td><td><b>136.341</b></td><td><b>—3164.52</b></td></tr><tr><td><b>$CH_{2}-CH_{2}-CH_{2}-CH_{2}$</b></td><td><b>1009.728</b></td><td><b>2018.446</b></td><td><b>136.341</b></td><td><b>—3164.52</b></td></tr><tr><td><b>$CH_{3}-CH_{2}-CH_{2}-CH_{2}$</b></td><td><b>1009.728</b></td><td><b>2018.446</b></td><td><b>136.341</b></td><td><b>—3164.52</b></td></tr><tr><td><b>$CH_{3}-CH_{2}-CH_{2}-CH_{3}$</b></td><td><b>1009.728</b></td><td><b>2018.446</b></td><td><b>136.341</b></td><td><b>—3164.52</b></td></tr></tbody></table>

A $CH_{3}$ group connected to a $CH$ group is denoted by $CHb_{3}$. For a $CH$ group the total torsion potential is the sum of two contributions.

potential

$$
u_{\text{bending}}(\theta_{i})=(1/2)k_{\theta}(\theta_{i}-\theta_{\text{eq}})^{2} \tag{2}
$$

with $\theta_{\text{eq}}=112.4^{\circ}$ as the equilibrium angle and with a force constant equal to $k_{\theta}=63\,390.976$ K rad$^{-2}$. Changes in the torsional angles are controlled by:

$$
u_{\text{torsion}}(\phi_{i})=C_{0}+C_{1}\cos(\phi_{i})+C_{2}\cos^{2}(\phi_{i})+C_{3}\cos^{3}(\phi_{i})
$$

with parameters shown in Table 2.

In our calculations, we focus on all-silica zeolites. Following Kiselev and co-workers, $^{13}$ the zeolite lattice was assumed to be rigid. For alkane adsorption the energetics will be dominated by dispersive interactions. Since the Si atoms are much smaller than the O atoms, they make a very small contribution to the energetics and can be ignored in the calculations. In fact, the interactions of the guest molecules with the Si atoms are implic- itly accounted for in the effective potential for the interactions with the O atoms. The dispersive interactions of the O atoms of the zeolite with the host molecules are described with a Lennard-Jones potential, eqn. (1). The parameters used are shown in Table 3.

## 3 Energetics and siting
In Fig. 1 the calculated heats of adsorption as a function of the total number of carbon atoms, $N_{c}$ in silicalite are compared with experimental data of Calvalcante and Ruthven$^{14}$ and Eder. $^{15}$ The simulations show that the temperature dependence of the heat of adsorption is very small. Only for $C_{12}$ is a small decrease in the heat of adsorption observed. The agreement of the experimental data with the simulation results is surprisingly good.

In Fig. 2 the structure of silicalite is shown schematically. Silicalite has two types of channels, zig-zag and straight, that cross each other at the intersections. Fig. 3 compares

<table><thead><tr><td></td><td><b>$(ε/k_{B})/K$</b></td><td><b>σ/Å</b></td></tr></thead><tbody><tr><td><b>$O-CH_{3}$</b></td><td><b>87.5</b></td><td><b>3.64</b></td></tr><tr><td><b>$O-CHb_{3}$</b></td><td><b>87.5</b></td><td><b>3.64</b></td></tr><tr><td><b>$O-CH_{2}$</b></td><td><b>54.4</b></td><td><b>3.64</b></td></tr><tr><td><b>O—CH</b></td><td><b>51.3</b></td><td><b>3.64</b></td></tr></tbody></table>

The interactions are truncated at $R_{c}=13.8$ Å.

![](./images/812654434625519619_1.jpg)

Fig. 1 Heats of adsorption of the branched alkanes $(CH_{3})_{2}-CH-(CH_{2})_{N-4}(CH_{3})$ as a function of the total number of carbon atoms $N_{c}$ at various temperatures. The experimental data are from ref. 14 for $N_{c}=6$ at $T=398 ~K$ and from ref. 15 for $N_{c}=8$ at $T=372 ~K$.

the distribution of the CH group of the heat of 2-methylbutane with the distribution of the middle segment of pentane in the pores of silicalite at $T=498 ~K$ . It shows that the distribution of the linear alkanes is very different from the distribution of the branched alkanes. Whereas pentane has an equal probability of being in the straight channels, zig-zag channels or intersections, the branched alkanes have a strong preference to be with the head group in the intersections. These results are in very good agreement withthe MC integration results of June et al. $^{16}$

For the other branched alkanes we also a find a preference for the head group to be in the intersections. If the head group is localized in the intersection, the tail of the molecule can either be in the straight or zig-zag channels or when the molecule is suffi- ciently small, in the intersection. In Fig. 4 we compare the distribution of the tails of the branched alkanes over the various channels of silicalite with the distribution of the linear alkanes at $T=298 ~K$ . For the branched alkanes, a nearly identical distribution isfound at $T=398$ and $498 ~K$ . For the linear alkanes, the distribution is relatively simple;

![](./images/812654434625519619_2.jpg)

Fig. 2 Schematic drawing of the pore structure of silicalite, the straight channels are in the $y-z$  plane and the zig-zag channels in the $x-z$ plane. The channels cross at the intersection.

![](./images/812654434625519619_3.jpg)

Fig. 3 Distribution of alkanes in the channels of silicalite. The lines represent the zeolite lattice. At regular intervals a dot, representing the position of the CH pseudo-atom of the head group for 2-methylbutane or the $CH_2$ middle segment for pentane, is drawn. The density of the dots is a measure of the probability of finding a molecule in a particular section of the zeolite. The top figures give a projection along the straight channels ($z$-$x$ plane) and the bottom figures along the zig-zag channel ($x$-$y$ plane).

![](./images/812654434625519619_4.jpg)

Fig. 4 Distribution of the alkanes over the zig-zag and straight channels and intersections, as a function of $N_c$ at $T=298$ K. Left-hand figure is for linear and right-hand figure for branched alkanes.

the short alkanes are equally likely to reside in the straight or zig-zag channels, the long alkanes have a preference for the straight channels (see ref. 6 and 17 for more details). The siting of the branched alkanes is more complex. The small branched alkanes ($N_c =$ 5, 6) are nearly spherical and can 'rotate' freely in the intersection. For these molecules it is not very favourable to put their tail into one of the channels. In fact, for these small molecules it is difficult, because of the bulky head, to reach the entrance of the zig-zag channel, therefore they prefer the straight channel. If we increase the tail length, the molecules become too big to be completely in the intersection and they have to put their tail in one of the channels. For these molecules the tail is sufficiently long so that it can be in the zig-zag channel while the head remains in the middle of the intersection. For these tail lengths we observed, therefore, a nearly equal probability of being in the straight or zig-zag channel. A further increase in the tail length makes these tails longer than the period of the zig-zag channel. As for the linear alkanes, this is not a favourable configuration and therefore the long branched alkanes prefer the straight channels.

## 4 Diffusion

It is interesting to discuss the consequences of the results of the previous section for the diffusion of these molecules in the pores of the zeolite. Comparison of the siting of the linear and branched alkanes shows that the (short-chain) linear alkanes have a uniform distribution whereas the branched alkanes prefer to be at the intersection. This suggests that these linear alkanes can move 'freely' in the channels and therefore their diffusion coefficient can be obtained from MD simulations within a reasonable amount of CPU time. The branched alkanes, however, are pinned with their head group at the intersec- tions and have a very small probability of being in the channels connecting the intersec- tions. These straight and zig-zag channels, therefore, form a barrier to diffusion. If this barrier is much higher than $k_{\mathrm{B}} T$, the diffusion of such an alkane is an activated process; most of the time the molecule resides at an intersection but occasionally a molecule hops from one intersection to another.

If the diffusion of these branched alkanes is an activated process, we can use the simulation techniques developed by Bennett $^{18}$ and Chandler $^{19}$ to simulate rare events. $^{20}$ The basic idea behind these calculations is that the rate at which a barrier crossing proceeds is determined by the product of a static term, namely the probability of finding the system at the top of the barrier, and a dynamic term that describes the rate at which systems at the top of the barrier move to the other valley.

To compute the diffusion coefficients of a branched alkane in a zeolite we have to determine a favourable reaction coordinate for which we can compute the free energy. For diffu- sion, a natural reaction coordinate is the position of one of the atoms of the adsorbed molecules. For branched alkanes it is convenient to take the position of the CH group (i.e. the group for which the distribution is shown in Fig. 3). Let us assume the concen- tration of hydrocarbons is sufficiently low, such that the probability that two hydrocar- bons are in neighbouring intersections is very small. In this limit, the jumps from one intersection to another are independent.

In silicalite, a molecule can jump from one intersection to another *via* the straight channel or zig-zag channel (see Fig. 5). We have to calculate the jump rates for each of these paths. Because of the symmetry of the crystal, the two different paths *via* the straight channels (jumping up or down) and the paths *via* the zig-zag channels are equivalent. The calculation can therefore be limited to computing the jump rates *via* these two paths.

For the straight channel the reaction coordinate $q_{\mathrm{str}}(z)$ is defined as the projection of the head group on the line connecting two intersections *via* a straight channel. For the zig-zag channel the reaction coordinate is $q_{\mathrm{zz}}(x, y)$ defined as the projection of the

![](./images/812654434625519619_5.jpg)

Fig. 5 Schematic drawing of the silicalite pore structure. An alkane can jump from one intersection to another. The dotted lines show the paths via zig-zag channels and the solid lines those via straight channels.

head group of the line connecting two intersections via a zig-zag channel (see Fig. 6).
Both reaction coordinates are normalized in such a way that $q \in [0; 1]$.

In practice, the computation of a rate constant consists of two steps. The expression
of the rate constant is given by $^{20}$

$$
k_{\mathrm{A} \rightarrow \mathrm{B}}(t)=\frac{\left\langle\dot{q}(0) \delta\left[q^{*}-q(0)\right] \theta\left[q(t)-q^{*}\right]\right\rangle}{\left\langle\delta\left[q^{*}-q(0)\right]\right\rangle} \times \frac{\left\langle\delta\left(q^{*}-q\right)\right\rangle}{\left\langle\theta\left(q^{*}-q\right)\right\rangle} \tag{3}
$$

where A and B are neighbouring intersections, $q(t)$ is the reaction coordinate, $\theta(x)$ is the
Heavyside step-function, $\theta(x)=1$ for $x>0$ and $\theta(x)=0$ otherwise, and $q^{*}$ is the top of
the free energy barrier separating the states A and B.

![](./images/812654434625519619_6.jpg)

Fig. $6 q_{\text {str }}(y)$ is reaction coordinate along the straight channel, obtained by projecting the $y$ coordinate of the molecule on the line indicated. $q_{\mathrm{zz}}(x, z)$ is obtained by projection of the $x-z$ coordinate on the line indicated.

100
Adsorption and diffusion of hydrocarbons in zeolites

The first part on the left-hand side of eqn. (3) is a conditional average, namely the average of the product $\dot{q}(0)\theta[q(t)-q^{*}]$, given that the initial position of the reaction coordinate is $q(0)=q^{*}$. An assumption in transition-state theory is that all trajectories that start on top of the barrier with a positive velocity will end up in state B. If this assumption holds, we have

$$
\dot{q}(0)\theta[q(t)-q^{*}]\approx\frac{1}{2}|\dot{q}|=\sqrt{\left(\frac{k_{\mathrm{B}}T}{2\pi m}\right)} \tag{4}
$$

It is important to note that it is possible to test the validity of the above approximation and to compute this ensemble average exactly. This conditional average can be calcu- lated from MD simulations. In these simulations we start with an initial configuration taken from a Boltzmann distribution on top of the barrier. Such a distribution can be obtained from constrained MD or, if the constraint is sufficiently simple, from an MC simulation.

In this work, we focus on the calculation of the second term on the right-hand side of eqn. (3), *i.e.* $\langle\delta(q^{*}-q)\rangle/\langle\theta(q^{*}-q)\rangle$, the probability density of finding the system at the top of the barrier, divided by the probability that the system is on the reactant side of the barrier. This ratio, can be calculated from the free energy as a function of the order parameter. We can use the CBMC algorithm to compute this free energy as a function of the order parameter. Details of this calculation are given in the Appendix.

A typical result is presented in Fig. 7. The free energies of 2-methylhexane as a function of order parameter in the straight and zig-zag channels are calculated. This figure indicates that in the straight channel there are three barriers. The height of the first barrier $(q=0.29)$ is $ca.\ 14\ k_{\mathrm{B}}T$, which demonstrates that a jump over this barrier is indeed a rare event. In addition this figure shows two additional barriers at $q=0.5$ and $q=0.68$. Because of the symmetry of the crystal the barriers at $q=0.68$ and $q=0.29$ are of equal height. Within the accuracy of the calculation, the barrier at $q=0.5$ is also of the same height. For the zig-zag channel we observe four barriers, the highest barrier has a height of $18\ k_{\mathrm{B}}T$.

For both the zig-zag and straight channels, the middle barriers have a height of several $k_{\mathrm{B}}T$, therefore crossing of these barriers is also a rare event on the timescale of an MD simulation. Thus, the jump from one intersection to another consists of three consecutive jumps over the three barriers shown in Fig. 7 for the straight channel or over four barriers for the zig-zag channel.

![](./images/812654434625519619_7.jpg)

Fig. 7 Free energy of 2-methylhexane as a function of the position of the head group in the straight (left) and zig-zag (right) channels. For $q=0$ and 1 the head group is in the intersections. $T=398$ K.

If we assume that transition-state theory can be applied to this system, Fig. 7 is sufficient to compute the crossing rate. If we combine the results of the free energy calculation with those of the transmission rate, as obtained from transition-state theory, eqn. (4), we can compute the crossing rates. The results of this calculation are shown in Table 4. For the straight channel we find that the highest barrier is crossed $1.4 \times 10^{5}$ times $\mathrm{s}^{-1}$. This implies that a molecule resides in the intersection for $c a$. $7 \mu \mathrm{s}$, which is a very long time on the timescale of an MD simulation. Since, for both the zig-zag and straight channel, there is one barrier which is much higher than the others, we can assume that these barriers determine the hopping rates. With this assumption we obtain: $w_{\text {str }}=1.37 \times 10^{5}$ and $w_{\mathrm{zz}}=5.0 \times 10^{4}$ events $\mathrm{s}^{-1}$.

Having computed the hopping rates from one intersection to another either via a straight channel or via a zig-zag channel, we have to relate these crossing rates to the diffusion coefficients. In the limit of infinite dilution the molecules perform a random walk on a lattice spanned by the intersections. The unit cell of this lattice is shown in Fig. 8.

Since this lattice is anisotropic, we have three different diffusion coefficients for the $x$, $y$ and $z$ directions $^{21}$

$$
D_{x x}=\frac{1}{12} w_{\mathrm{zz}} \boldsymbol{a}^{2}, \quad D_{y y}=\frac{1}{12} w_{\mathrm{str}} \boldsymbol{b}^{2}, \quad D_{z z}=\frac{1}{12} \frac{w_{\mathrm{zz}} w_{\mathrm{str}}}{w_{\mathrm{zz}}+w_{\mathrm{str}}} \boldsymbol{c}^{2}
\tag{5}
$$

where $\boldsymbol{a}, \boldsymbol{b}$ and $\boldsymbol{c}$ are the unit vectors of the diffusion lattice (see Fig. 8), $w_{\mathrm{zz}}$ and $w_{\text {str }}$ are the hopping rates via the zig-zag and straight channels, respectively. The formula for the diffusion in the $z$ direction reflects that for a molecule to diffuse in this direction it has to jump via a straight channel followed by a jump via a zig-zag channel. For the overall diffusion coefficient, we can write

$$
D=\frac{1}{12} w_{\mathrm{zz}}\left(\boldsymbol{a}^{2}+\frac{w_{\mathrm{str}}}{w_{\mathrm{zz}}+w_{\mathrm{str}}} \frac{\boldsymbol{c}^{2}}{2}\right)+\frac{1}{12} w_{\mathrm{str}}\left(\boldsymbol{b}^{2}+\frac{w_{\mathrm{zz}}}{w_{\mathrm{zz}}+w_{\mathrm{str}}} \frac{\boldsymbol{c}^{2}}{2}\right)
\tag{6}
$$

Numerical values for the diffusion coefficient of 2-methylhexane are given in Table 5. Experimentally, diffusion coefficients of branched alkanes are found in the range $10^{-9}$ $10^{-11} \mathrm{~cm}^{2} \mathrm{~s}^{-1} .^{2}$ Comparison with our result: $8.5 \times 10^{-10} \mathrm{~cm}^{2} \mathrm{~s}^{-1}$ shows that our first estimate of the diffusion coefficient has the same order of magnitude as the experimental results.

In the previous calculations, we have assumed that transition-state theory holds. We have performed some MD simulations with configurations that start on top of the

<table>
<caption>Table 4 Hopping rates</caption>
<thead>
<tr>
<th></th>
<th>$-\beta F(q_{\text{min}})$</th>
<th>$-\beta F(q^{*})$</th>
<th>$k^{\text{TST}}/$<br>events $\mathrm{s}^{-1}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>str $(1 \to 2)$</td>
<td>$-22.9$</td>
<td>$-6.8$</td>
<td>$1.4 \times 10^{5}$</td>
</tr>
<tr>
<td>str $(2 \to 3)$</td>
<td>$-12.3$</td>
<td>$-6.9$</td>
<td>$4.3 \times 10^{10}$</td>
</tr>
<tr>
<td>str $(3 \to 1)$</td>
<td>$-11.9$</td>
<td>$-6.5$</td>
<td>$2.6 \times 10^{10}$</td>
</tr>
<tr>
<td>zz $(1 \to 2)$</td>
<td>$-23.8$</td>
<td>$-5.8$</td>
<td>$5.0 \times 10^{4}$</td>
</tr>
<tr>
<td>zz $(2 \to 3)$</td>
<td>$-9.6$</td>
<td>$-5.3$</td>
<td>$1.3 \times 10^{11}$</td>
</tr>
<tr>
<td>zz $(3 \to 4)$</td>
<td>$-10.5$</td>
<td>$-5.2$</td>
<td>$1.0 \times 10^{11}$</td>
</tr>
<tr>
<td>zz $(4 \to 1)$</td>
<td>$-20.2$</td>
<td>$-9.0$</td>
<td>$1.4 \times 10^{9}$</td>
</tr>
</tbody>
</table>

$\beta F(q)$ is the free energy for the order parameters, $q_{\text{min}}$ the bottom of the well and $q^{*}$ the top of the barrier, $k^{\text{TST}}$ is the hopping rate as approximated with transition-state theory.

![](./images/812654434625519619_8.jpg)

Fig. 8 Diffusion unit cell of silicalite; the intersections are represented by dots and the channels by lines. $a=20.1$, $b=19.9$ and $c=2\times13.4$ Å for this cell (where 20.1, 19.9 and 13.4 Å are the vectors of the unit cell of silicalite).

barrier, to test whether or not transition-state theory is a reasonable approximation. These preliminary calculations indicate that transition-state theory may overestimate the diffusion coefficients by a factor of 5-10. Unfortunately, these calculations were not sufficiently accurate to compute the crossing rate accurately.

## 5 Concluding remarks

We have used the CBMC technique to investigate the behaviour of linear and branched alkanes in the pores of the zeolite silicalite. We find that the calculated heats of adsorp- tion for both the linear and the branched alkanes are in good agreement with the experi- mental data.

The simulations indicate that siting of the branched alkanes is very different from the siting of the linear ones. The linear alkanes can move 'freely' in the channels of silicalite,

Table 5 Diffusion coefficients of 2-methylhexane in silicalite at $T=398$ K

<table>
<thead>
<tr>
<th>$D_{xx}$<br>/$\text{cm}^2\text{s}^{-1}$</th>
<th>$D_{yy}$<br>/$\text{cm}^2\text{s}^{-1}$</th>
<th>$D_{zz}$<br>/$\text{cm}^2\text{s}^{-1}$</th>
<th>$D$<br>/$\text{cm}^2\text{s}^{-1}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$1.7\times10^{-10}$</td>
<td>$4.7\times10^{-10}$</td>
<td>$2.1\times10^{-10}$</td>
<td>$8.5\times10^{-10}$</td>
</tr>
</tbody>
</table>

the branched alkanes, however, are trapped with their CH group in the intersections of the zig-zag and straight channels. This trapping suggests that the diffusion of the branched alkanes is an activated process; most of the time the molecules are in the intersections but once in while a molecule hops from one intersection to another via a straight or zig-zag channel. These straight and zig-zag channels form a barrier for the diffusion.

We demonstrate that the CBMC technique can be used to compute the free energy of these diffusion barriers. From these free energy barriers an estimate of the diffusion coefficient can be made, if we assume that transition-state theory is valid for this system. The resulting diffusion coefficient is in reasonable agreement with experimental data.

In the future we will extend these calculations to test whether the transition state is valid for this system. At this point it is important to note that these calculations have been performed for a rigid zeolite lattice; one can expect that allowing the zeolite atoms to move can have significant consequences for the height of the free energy barrier. It is therefore, important to repeat these calculations with a flexible zeolite lattice.

## Appendix: free energy calculation

One part of the calculation of barrier crossing rate is the computation of the free energy as a function of the order parameter. For the diffusion of branched alkanes in zeolites, we use the position of the head as the order parameter. Here, we demonstrate how to calculate the free energy as a function of this order parameter.

In the CBMC algorithm the Rosenbluth scheme is used to generate new conforma- tions of the hydrocarbons. A molecule is grown atom by atom using the algorithm of Rosenbluth and Rosenbluth. $^{23}$ During the growing of an atom several trial positions are probed, the energy of each of these positions is calculated, and the one with the lowest energy is selected with the highest probability according to:

$$
P_{i}(j)=\frac{\exp \left[-\beta u_{i}(j)\right]}{\sum_{l=1}^{k} \exp \left[-\beta u_{i}(l)\right]}=\frac{\exp \left[-\beta u_{i}(j)\right]}{w(i)},
$$

where $u_{i}(l)$ is the energy of atom $i$ at trial position $l$. When the entire chain is grown, the normalized Rosenbluth factor of the molecule in configuration $\Gamma$ can be computed:

$$
W(\Gamma)=\prod_{i=1}^{l} w(i) / k
$$

In ref. 20 it is shown that the average Rosenbluth factor is related to the chemical potential of the molecule:

$$
\langle\exp (-\beta \mu)\rangle=C\langle W\rangle
$$

where $C$ is a constant defining the reference chemical potential. One can also calculate the Rosenbluth factor as a function of the order parameter. This gives the chemical potential or free energy as a function of the order parameter.

The number of samples for a given value of the order parameter is determined by the way we grow the molecule. For example, if we start the growing procedure by giving the CH group a random position in the zeolite, we obtain a uniform sampling of all values of the order parameter, irrespective of whether we sample the top or the bottom of the barrier. The method does not rely on the acceptance of the configuration on top of the barrier.

The fact that we do not need to rely on sampling configurations in which the mol- ecule is on top of the barrier may cause difficulties when a flexible zeolite is used. During the simulation, the zeolite atom will never 'see' an alkane molecule on top of the barrier. As a consequence, one would never sample those configurations in which the zeolite

104
# Adsorption and diffusion of hydrocarbons in zeolites

lattice would 'respond' to the presence of a molecule on top of the barrier. Such fluctua- tions of the zeolite lattice may change the height of the barrier significantly. Therefore, it is important to use a scheme in which we force the system to sample configurations on top of the barrier. A method which allows us to do this is, for example, the multiplehistogram technique. $^{20}$

## References

1 *Modelling of Structure and Reactivity in Zeolites*, ed. C. R. A. Catlow, Academic Press, London, 1992.
2 S. D. Pickett, A. K. Nowak, J. M. Thomas, B. K. Peterson, J. F. Swift, A. K. Cheetham, C. J. J. den Ouden, B. Smit and M. Post, *J. Phys. Chem.*, 1990, **94**, 1233.
3 A. K. Nowak, C. J. J. den Ouden, S. D. Pickett, B. Smit, A. K. Cheetham, M. F. M. Post and J. M. Thomas, *J. Phys. Chem.*, 1991, **95**, 848.
4 R. L. June, A. T. Bell and D. N. Theodorou, *J. Phys. Chem.*, 1992, **96**, 1051.
5 E. Hernández and C. R. A. Catlow, *Proc. R. Soc. London, Ser. A*, 1995, **448**, 143.
6 B. Smit and J. I. Siepmann, *Science*, 1994, **264**, 1118.
7 B. Smit and T. L. M. Maesen, *Nature (London)*, 1995, **374**, 42.
8 S. P. Bates, W. J. M. van Wel, R. A. van Santen and B. Smit, *J. Am. Chem. Soc.*, 1996, **118**, 6753.
9 S. P. Bates, W. J. M. van Wel, R. A. van Santen and B. Smit, *J. Phys. Chem.*, 1996, **100**, 17573.
10 E. J. Maginn, A. T. Bell and D. N. Theodorou, *J. Phys. Chem.*, 1995, **99**, 2057.
11 Y. Wang, K. Hill and J. G. Harris, *J. Phys. Chem.*, 1994, **100**, 3276.
12 M. P. Allen and D. J. Tildesley, *Computer Simulation of Liquids*, Clarendon Press, Oxford, 1987.
13 A. G. Bezus, A. V. Kiselev, A. A. Lopatkin and P. Q. Du, *J. Chem. Soc., Faraday Trans. 2*, 1978, **74**, 367.
14 C. L. Cavalcante Jr. and D. M. Ruthven, *Ind. Eng. Chem. Rev.*, 1995, **34**, 177.
15 F. Eder, PhD thesis, Universiteit Twente, The Netherlands, 1996.
16 R. L. June, A. T. Bell and D. N. Theodorou, *J. Phys. Chem.*, 1990, **94**, 1508.
17 B. Smit and J. I. Siepmann, *J. Phys. Chem.*, 1994, **98**, 8442.
18 C. H. Bennett, in *Diffusion in Solids: Recent Developments*, ed. A. S. Nowick and J. J. Burton, Academic Press, New York, 1975, pp. 73-113.
19 D. Chandler, *J. Chem. Phys.*, 1978, **68**, 2959.
20 D. Frenkel and B. Smit, *Understanding Molecular Simulations: from Algorithms to Applications*, Aca- demic Press, Boston, 1996.
21 B. Smit, L. D. J. C. Loyens, G. L. M. M. Verbist and D. Frenkel, in preparation.
22 J. Kärger and D. M. Ruthven, *Diffusion in Zeolites and other Microporous Solids*, Wiley, New York,1992.
23 M. N. Rosenbluth and A. W. Rosenbluth, *J. Chem. Phys.*, 1955, **23**, 356.

*Paper 7/01559C; Received 5th March, 1997*