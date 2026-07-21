![](./images/813227439168684033_1.jpg)

Contents lists available at SciVerse ScienceDirect

# Annals of Physics
journal homepage: www.elsevier.com/locate/aop

![](./images/813227439168684033_2.jpg)

# Low-temperature magnetization relaxation in magnetic molecular solids

![](./images/813227439168684033_3.jpg)

Avinash Vijayaraghavan, Anupam Garg*

Department of Physics and Astronomy, Northwestern University, Evanston, IL 60208, United States

## HIGHLIGHTS
- A novel set of non-linear rate equations for the coupled evolution of the magnetization and dipole field distribution.
- An analytic derivation of the short-time square root in time behavior of the magnetization relaxation.
- Agreement between theory and simulations without further fitting parameters.

## ARTICLE INFO
Article history:
Received 12 March 2013
Accepted 4 April 2013
Available online 2 May 2013

Keywords:
Rate equation
Slow relaxation
Molecular magnet

## ABSTRACT
The low temperature relaxation of the magnetization in molecular magnetic solids such as $Fe_8$ is studied using Monte Carlo simulations. A set of rate equations is then developed to understand the simulations, and the results are compared. The simulations show that the magnetization of an initially saturated sample deviates as a square-root in time at short times, as observed experimentally, and this law is derived from the rate equations analytically.

© 2013 Elsevier Inc. All rights reserved.

---

## 1. Introduction
The low temperature relaxation of the magnetization of magnetic molecular solids such as $Fe_8$ has proven difficult to understand ever since the earliest experimental studies [1–3]. The time dependence of this relaxation is highly non-exponential, and fits to forms such as stretched exponentials have provided no insight even when the fits seem to be good. A second puzzling feature is that for short times, the relaxation is observed to follow a square-root behavior with time in a large number of protocols: demagnetization, magnetization, and hole-digging in which the magnetic field is abruptly changed after the magnetization has been allowed to come to an equilibrium or quasi-equilibrium

---
* Corresponding author. Tel.: +1 847 491 3229; fax: +1 847 491 9982.
E-mail address: agarg@northwestern.edu (A. Garg).

0003-4916/$ – see front matter © 2013 Elsevier Inc. All rights reserved.
http://dx.doi.org/10.1016/j.aop.2013.04.011

state in response to a previous value of the applied magnetic field. A good review of the subject is given by Gatteschi, Sessoli, and Villain [4]. These authors give many more references to experimental studies [1-3,5-8], theoretical analyses [9], and Monte Carlo simulations [10,11]. Additional work is contained in Refs. [12,13].

The fundamental microscopic mechanism by which the spin of an individual molecule changes at low temperatures (say below 50 mK) is incoherent tunneling between the lowest energy states. In both $Fe_8$ and $Mn_{12}$, the anisotropy of the molecule is of the Ising type, and the lowest energy states have Zeeman quantum numbers $m = \pm S$, where $S$ is the spin of the molecule. The tunnel splitting between these states is of order 100 Hz (in frequency units) for $Fe_8$ and unobservably small for $Mn_{12}$. It must be stressed that in the solid, the tunneling is not of the coherent flip-flop type seen in the $NH_3$ molecule, and previous authors have examined various decoherence processes by which the tunneling dynamics of a single molecule change from coherent to incoherent [14,15]. This is not enough to explain the observed non-exponential time behavior, for if there were a single characteristic time scale for relaxation of a single molecule, and all molecules relaxed independently, the magnetization would relax essentially exponentially in time with the same time scale as for one molecule. Thus, the non-exponential time behavior is a strong indicator that the molecules in the solid do not relax independently of each other. The biggest and most obvious coupling between molecules is the dipole-dipole interaction, and while this has been considered by many previous authors [2,9,4] a complete theory is still lacking. In particular, the $\sqrt{t}$ form has been written down by Prokofev and Stamp [9], but as noted by Gatteschi, Sessoli, and Villain [4], several aspects of their argument are unclear, and it is also unclear if the $\sqrt{t}$ form applies to all situations. These latter authors also give a heuristic argument for the $\sqrt{t}$ law for the particular case of the demagnetization problem. (We comment further or this below.) In sum, our understanding of the relaxation phenomena is incomplete and/or heuristic, and an independent analysis seems worthwhile. It is the purpose of this paper to provide one.

We note here that a rather different explanation for the $\sqrt{t}$ behavior is given by Miyashita and Saito [12]. In their approach, the magnetization relaxes entirely due to nuclear spins, which are taken to provide a field at the molecular spin site in the form of a random walk. This model has been examined in detail by Villain [13], who concludes that while it may apply to other molecular magnets under certain conditions, it cannot apply to real $Fe_8$, not only because the dipole field of the molecules is about 10 times larger than the nuclear spin field, but also because it is valid only if the nuclear spin relaxation is very slow. The reader is referred to Villain's paper for more details.

Our first approach to the problem is Monte Carlo simulation, as also done in Refs. [10,11]. In keeping with general practice, the detailed behavior of various microscopic features of the system are not reported in these references, so we found it necessary to do the simulation for ourselves in order to understand completely the effect of various parameters. However, Monte Carlo simulation is ultimately a form of numerical experimentation, and by itself it does not provide a physical framework for understanding of the phenomenon. We present in this paper such a framework by developing a set of rate equations for the magnetization, and the up and down spin populations on a subset of sites where the dipole field is very close to zero. These rate equations entail the distribution of dipole fields at the molecular sites. For the specific problem of demagnetization, we can construct an approximate model for this distribution, which then enables us to solve the rate equations numerically. We find that the solution to the rate equations matches the Monte Carlo results quite closely. Furthermore, we can show analytically that the solution obeys a square-root behavior with time at short times. As in Ref. [4] we have only studied the demagnetization problem. Further, the scaling behavior that we find for ancillary quantities also agrees with the heuristic argument in Ref. [4]. The additional and new features of our work over Refs. [4,9] are that we have a microscopic theory in the form of the rate equations, and the coefficient of the $\sqrt{t}$ law is *not* a fitting parameter, but is completely determined in terms of the parameters of the problem, since our model for the dipole field distributions and the rate equations requires no further ingredients or fitting parameters beyond those involved in specifying the Monte Carlo process. In this paper we focus on the problem of demagnetization of a spherical sample with a cubic lattice in order to minimize the complications from demagnetizing fields, and study the shape independent aspects of the problem, but we believe that our rate equation approach offers a method to attack a much wider class of problems, and in the future we hope to study other experimental protocols, sample shapes, and lattice types.

The plan of the paper is as follows. In Section 2 we describe the basic physical model underlying the relaxation [9,15]. We then describe our Monte Carlo simulations and results in Section 3. The theory for the rate equations and the bias distribution are developed in Sections 4 and 5. Finally, in Section 6 we present our analytical solution to the rate equations, and the $\sqrt{t}$ law.

## 2. Physical model for relaxation

As shown in Ref. [15], the fundamental process that governs the dynamical behavior of the spins is as follows. In a short time interval $dt$, the spin of the $i$th molecule flips from $m=-S$ to $m=S$, or $m=S$ to $m=-S$, with a probability
$$
p_{\text{flip},i} = \Gamma_i dt, \tag{2.1}
$$
with
$$
\Gamma_i \equiv \Gamma(E_i) = \frac{\sqrt{2\pi}}{4} \frac{\Delta^2}{W} \exp\left(-\frac{E_i^2}{2W^2}\right). \tag{2.2}
$$

Here, $\Delta$ is defined via the statement that $i\Delta/2$ is the quantum mechanical amplitude per unit time for a spin to tunnel between the $m=\pm S$ states, $W \simeq 10E_{dn}$, where $E_{dn}$ is the energy of dipole-dipole interaction between the molecular electronic spin and the nuclear spins of nearby nonmagnetic atoms such as N and H which are always present in the molecules studied, and $E_i$ is the energy of the $m=S$ state relative to the $m=-S$ state due to the net magnetic field seen by the $i$th molecule. We shall refer to $E_i$ as the bias on site $i$ [16]. For Fe$_8$, $\Delta \sim 10^{-8}$ K, $E_{dn} \sim 1$ mK, and $E_i \sim 0.1$ K in temperature units. (We shall set $\hbar$ and $k_B$ to unity in all working formulas, so temperature, energy, and frequency all have the same units.)

The dominant feature in Eq. (2.2) is the exponential suppression of the flip rate with the square of the bias energy $E_i$, and a large part of this energy arises from the dipolar field of the other molecular spins in the solid, which can be estimated to be of order 100 Oe for near neighbor spins, leading to the energy scale 0.1 K quoted above. More explicitly, the dipolar part of $E_i$ is given by
$$
E_{i,\text{dip}} = \sum_{j \neq i} K_{ij}\sigma_j, \tag{2.3}
$$
$$
K_{ij} = 2\frac{E_{dm}a^3}{r_{ij}^3}\left(1 - 3\frac{z_{ij}^2}{r_{ij}^2}\right). \tag{2.4}
$$

Here, $E_{dm}$ is the energy scale of interaction for near neighbors, $a$ is the near-neighbor distance, $r_{ij}$ is the distance between spins $i$ and $j$, $z_{ij}$ is the projection of the corresponding displacement onto the $z$-axis, the easy axis of the spins. Finally, $\sigma_i$ is an Ising spin variable such that $\sigma_i = \pm 1$ when the true spin on site $i$ is $\pm S$.

Since the dipole field is long ranged, and $E_{dm} \gg E_{dn}$ K, the flip of the $i$th spin changes the bias field on a large number of neighboring spins, and thus changes the flip probability for those spins significantly. The relaxation of the magnetization of the entire solid is therefore a complex coupled process in which every individual spin essentially waits until it experiences a bias field less than $W$ in magnitude, and then flips with a probability per unit time equal to approximately $\Delta^2/W$. The flip of this spin changes the bias field at many other molecules, and if one of them then happens to have a near-zero bias field, it flips, leading to the possibility of flips at yet more molecules. Ref. [4] refers to this scenario as a long-range Glauber model.

## 3. Monte Carlo simulation

### 3.1. Simulation protocol

As explained in Section 1, in this paper we only report on simulations on spherical samples of $N$ spins on a cubic lattice in order to eliminate the effects of inhomogeneous demagnetizing fields. In addition, we only consider the demagnetization process. Thus, the spin $\sigma_i$ is initialized to the value $+1$ at

every site. Starting from this configuration, we simulate the time evolution of the sample (as described below) for between 60 and 500 runs, and then average the total magnetization of the entire sample over these runs. We have performed simulations for two sample sizes, with $N=9171$ and 82,519.

The initial spin polarization creates an almost delta-function-like distribution of bias fields centered at zero field, exactly as expected theoretically. We see small deviations from a perfectly uniform distribution due to the finite size of the sphere.

The evolution of the system from time step $t$ to the next time step $t+dt$ is carried out using the following protocol. At time $t$, the bias energy $E_i$ is computed at every site using Eq. (2.3). All spins are then flipped or not flipped using the flipping protocol described below. We are now at time $t+dt$. The bias fields are recomputed at all sites, and the process is repeated.

The flipping protocol we employ entails a slightly modified flip probability

$$
p_{\text{flip},i} = \frac{\Delta_2^2}{4W} \Theta(W - |E_i|) dt, \tag{3.1}
$$

instead of the original form (2.2). Here, $\Theta(\cdot)$ is the Heaviside function equal to unity for positive argument and to zero for negative argument. In other words, a spin flips only if the bias field on it is less than $W$ in magnitude. This modification is not material to the physics, and it reduces the run time of the simulations. We refer to the spins in the window $|E_i| < W$ as reversible. We have also used Eq. (2.2) in a few cases, and not found any significant differences in the results. Further, $\Delta_2 = \sqrt{\pi} \Delta$, and the prefactor in Eq. (3.1) is chosen to ensure that the integral $\int_{-\infty}^{\infty} p_{\text{flip}}(E)dE$ is unchanged. In this way, the total magnetization that flips in a large subvolume containing many spins is unaffected. For future use we define

$$
\Gamma_0 = \frac{\Delta_2^2}{4W}. \tag{3.2}
$$

An important consideration arises with regard to the values of $E_{dm}$, $\Delta$, and $W$ to be used in the simulation. We know that the ratio of these quantities for real $\text{Fe}_8$ is $E_{dm}/\Delta \sim 10^7$, and $E_{dm}/W \sim 10$. Due to the long ranged nature of the dipole field, when a spin flips, it has the potential to bring $\sim 10E_{dm}/W$ spins into the reversibility region $|E_i| < W$. We refer to this as the influence sphere of the spin. To overcome finite size effects, we must make sure that our simulation includes a large number of influence spheres. Secondly, the rate at which a spin flips, even if it is within the reversibility window, is governed by $\Delta$, and our simulation would be much too slow if we used the actual value of $\Delta/E_{dm}$. We have therefore chosen different values for these quantities while still ensuring the physically important restriction $E_{dm} \gg W \gg \Delta$. Specifically, we take $\Delta_2 = 2.0$, $E_{dm} = 50\Delta_2$, and vary $W$ over a range of values between $\Delta_2$ and $E_{dm}$.

The next consideration is over the choice of the time step $dt$. We set $dt = 0.01E_{dm}/\Delta_2^2$, and hence independent of $W$. This is done in order to remain true to the idea that the flip probability for a reversible spin should depend on $W$ only through the rate $\Gamma_0$, and not $dt$. With our choice of $dt$ this probability is

$$
\begin{aligned}
p_{\text{flip}} &= \frac{\Delta_2^2}{4W} dt \\
&= 0.01 \frac{\Delta_2^2}{4W} \frac{E_{dm}}{\Delta_2^2} \\
&= 0.01 \frac{E_{dm}}{4W}. \tag{3.3}
\end{aligned}
$$

By choosing $E_{dm}/4W \lesssim 10$, we ensure that the flip probability in one time step is not too large, which in turn ensures that our discretization of time is not too coarse, and that the simulation is sufficiently close to a continuous process. At the same time, $p_{\text{flip}}$ is large enough that we do not expend unnecessary time steps in waiting for the spin configuration to change by a meaningful amount. The time-scale $\tau = E_{dm}/\Delta_2^2$ demarcates short versus long times, and we shall study relaxation for $\sim 10^3 \tau$ in some cases, i.e., $\sim 10^5$ time steps. For real $\text{Fe}_8$ we have $\tau \simeq 10^4$ s.

![](./images/813227439168684033_4.jpg)

Fig. 1. Long-time decay of magnetization for the $N=82,519$ spin sample, averaged over 60 runs. The parameter values are $W=2.5\Delta_{2}$, and $E_{dm}=50\Delta_{2}$.

Some other details of the simulation are as follows. The spherical sample is built from a cube having an odd number of sites on a simple cubic lattice with lattice constant 'a', and selecting those sites within a distance $Da/2$ of the origin in order to get a sphere of diameter $Da$. The two system sizes $N=9171$ and $N=82,519$ correspond to sphere diameters $D=27$ and $D=55$ respectively. The sites are indexed from 1 to $N$, and their Cartesian coordinates are stored in one-dimensional arrays. To reduce computer time, at the start a one-dimensional look-up table is made of the kernel $K_{ij}$ by converting the triple of distances $(x_{ij}, y_{ij}, z_{ij})$ into a single unique number using some artificial but easy-to-implement formula that is invertible, i.e., capable of yielding the triple $(x_{ij}, y_{ij}, z_{ij})$ from the single number.

### 3.2. Quantities measured

The central quantity of interest that is measured in our simulations is the magnetization,
$$
m=(N_{\uparrow}-N_{\downarrow})/N, \tag{3.4}
$$
where $N_{\uparrow}$ and $N_{\downarrow}$ are the number of up and down spins. The magnetization is measured at every time step.

In addition, we also measure at every time step, the bias distribution $\rho(E)$, defined such that $\rho(E)dE$ is the fraction of spins experiencing a bias field between $E$ and $E+dE$. The bin width for numerical purposes is chosen as $W$ itself as this is a sufficiently small number compared to $E_{dm}$. Secondly, the distribution is measured for biases that satisfy $|E_{i}| \leq 15E_{dm}$. In practice, we find that the fraction of sites that lie outside this range is $O(10^{-2})$.

### 3.3. Results of the simulations

As mentioned above, we have performed the simulations for different relative values of $W$ and $E_{dm}$. For a test case, we made the contraphysical choice $W \gg E_{dm}$. In this case we expect each spin to remain reversible most of the time, and rarely move out of the reversibility window when neighboring spins flip. Each spin should then relax essentially independently of the others, leading to exponential relaxation of the magnetization with a rate $2\Gamma_{0}$. This is indeed what is observed, giving us confidence in our numerical code.

The physically interesting simulations are performed for $E_{dm} \gg W$. In Fig. 1, we show the magnetization versus time for one such simulation over a time $1000\tau$. It is evident that the decay of $m$ is nonexponential, and that there is a steep initial drop in $m$ over a time of order $\tau$. This drop is shown in more detail in Fig. 2, and is quite well fit by a square-root form; we discuss this in more detail in Section 6. In both these figures, we have performed an average over 60 runs.

![](./images/813227439168684033_5.jpg)

Fig. 2. Short-time behavior of the magnetization, with the same parameters as in Fig. 1. Also shown is the result from the numerical solution of the rate equations.

![](./images/813227439168684033_6.jpg)

Fig. 3. Histogram of the short-time bias distribution for the $N = 82,519$ spin sample, averaged over 60 runs, with the same parameters as in Figs. 1 and 2. The bin width in the bias is 5.0.

In Figs. 3 and 4 we show the short- and long-time bias distribution $\rho(E)$ for the same parameters as in Figs. 1 and 2. At short times, the distribution is marked by three clear peaks, as well as a few shoulders, which we shall explain in more detail in Section 5. Here we note that the two main peaks other than at the center are at $-4E_{dm}$ and $8E_{dm}$. It is also evident that the peaks and shoulders become less distinct as $t$ increases. Indeed, for $t \geq 100\tau$, they disappear completely, as shown in Fig. 4. Here we see a new feature developing, namely a hole in the distribution at $E = 0$, for $t \geq 500\tau$.

The bias distributions also provide a good indicator of whether our system size is large enough and whether the averaging procedure is valid. To this end, we show in Figs. 5 and 6 the short- and long-time distributions for the smaller sample size ($N = 9171$) but all parameters the same as in previous figures. The two figures are drawn for averages over 60 and 30 runs, respectively. As can be seen, the statistical scatter is only minimally greater, and the quantitative features – heights and locations of the peaks at short times, the hole at zero bias at long times – are identical. Finally, in Fig. 7, we show the short-time distribution for a single run of the larger sample. The features seen in the 60-run average are all clearly present, showing that questions of self-averaging do not arise in this system.

## 4. Rate equations for magnetization relaxation

To understand our simulations, we have developed a theory based on rate equations. The key realization lies in the very different role played by the reversible and the nonreversible spins, and

![](./images/813227439168684033_7.jpg)

Fig. 4. Same as Fig. 3 but for long times, and averaged over 10 runs only. Note the reduced scale on the y axis.

![](./images/813227439168684033_8.jpg)

Fig. 5. Same as Fig. 3 for the $N=9171$ spin sample. The average is over 60 runs.

![](./images/813227439168684033_9.jpg)

Fig. 6. Same as Fig. 4 for the $N=9171$ sample. The average is over 30 runs.

that we therefore need to understand the time-development of each set separately. We denote by $N_r$, $N_{r\uparrow}$, and $N_{r\downarrow}$ the total number of reversible spins at any instant (i.e., those with a bias satisfying $|E|\leq W$), and the parts of this number whose spins are up or down. Corresponding lower case symbols $n_r$, $n_{r\uparrow}$, $n_{\uparrow}$ etc. are used for the fractions $N_r/N$, $N_{r\uparrow}/N$, $N_{\uparrow}/N$, etc. We also denote the number of nonreversible spins, $N-N_r$, by $N_{\bar{r}}$, and the sets of spins of various types by $\mathcal{S}_r$, $\mathcal{S}_{r\uparrow}$, $\mathcal{S}_{\bar{r}}$ etc. These

![](./images/813227439168684033_10.jpg)

Fig. 7. Single-run short-time bias distribution for the $N=82,519$ sample, with the same parameters as before. There is no averaging.

sets obey obvious relations such as $\mathcal{s}_r = \mathcal{s}_{r\uparrow} \cup \mathcal{s}_{r\downarrow}$ and so on, which need not be listed. It also pays to introduce the reversible magnetization,

$$
m_{r}=n_{r \uparrow}-n_{r \downarrow}, \tag{4.1}
$$

the total magnetic moment $M=Nm$, and its reversible part, $M_{r}=Nm_{r}$.

### 4.1. Processes that change the state of a spin

We now examine how different spins can develop in a small time interval $dt$. A non-reversible spin (at site $i$, say) can
1. Move into the reversible bias range with a probability $p_{\text{in},i}$.
2. Remain in the non-reversible range with a probability $1-p_{\text{in},i}$.

Naturally, since this spin cannot flip in the interval $dt$, these possibilities depend on the behavior of other spins. We shall address the probability $p_{\text{in},i}$ below.

A reversible spin (again taken to be at site $i$), on the other hand, can do the following:
1. Flip and move out of the reversible range with probability $p_{\text{flip}}p_{\text{out},i}$.
2. Flip and remain in the reversible range with probability $p_{\text{flip}}(1-p_{\text{out},i})$.
3. Not flip and become nonreversible with probability $(1-p_{\text{flip}})p_{\text{out},i}$.
4. Not flip and stay reversible with reversibility $(1-p_{\text{flip}})(1-p_{\text{out},i})$.

Once again, the probability $p_{\text{out},i}$ depends on the behavior of other spins, and will be estimated below. We have also introduced the quantity

$$
p_{\text{flip}}=\Gamma_{0} d t, \tag{4.2}
$$

in which the index $i$ is omitted in $p_{\text{flip}}$, since this is the flip probability for all reversible spins. Clearly, our model assumes that the processes of flipping and of moving in or out of the reversibility range are independent, which in turn means that different spins flip or do not flip completely independently of each other, with a probability that depends only on the local bias. This assumption will be valid provided the bias distribution $\rho(E)$ is reasonably spatially homogeneous across the sample at all times. Such is the case for our spherical samples, but will need to be reexamined for other shapes.

With the above hypothesis, the change in the numbers of various types of spins in a short time interval $dt$ are easily written down. For $dN_{r\uparrow}$, we have

$$
\begin{aligned}
d N_{r \uparrow}= & -\sum_{i \in \mathcal{s}_{r \uparrow}}\left[p_{\text{flip}} p_{\text{out}, i}+p_{\text{flip}}\left(1-p_{\text{out}, i}\right)+\left(1-p_{\text{flip}}\right) p_{\text{out}, i}\right] \\
& +\sum_{i \in \mathcal{s}_{r \downarrow}} p_{\text{flip}}\left(1-p_{\text{out}, i}\right)+\sum_{i \in \mathcal{s}_{\uparrow}} p_{\text{in}, i}.
\end{aligned} \tag{4.3}
$$

The first four terms on the right correspond to the four processes enumerated above for reversible spins, while the fifth term corresponds to nonreversible up spins becoming reversible. Simplifying, we get

$$
dN_{r\uparrow}=-\sum_{i\in \mathcal{S}_{r\uparrow}}\left[p_{\text{flip}}+(1-p_{\text{flip}})p_{\text{out},i}\right]+\sum_{i\in \mathcal{S}_{r\downarrow}}p_{\text{flip}}(1-p_{\text{out},i})+\sum_{i\in \mathcal{S}_{\bar{r}\uparrow}}p_{\text{in},i}.\tag{4.4}
$$

Similarly,

$$
dN_{r\downarrow}=-\sum_{i\in \mathcal{S}_{r\downarrow}}\left[p_{\text{flip}}+(1-p_{\text{flip}})p_{\text{out},i}\right]+\sum_{i\in \mathcal{S}_{r\uparrow}}p_{\text{flip}}(1-p_{\text{out},i})+\sum_{i\in \mathcal{S}_{\bar{r}\downarrow}}p_{\text{in},i}.\tag{4.5}
$$

Adding the last two equations, we get a very simple equation for the change in the total number of reversible spins,

$$
dN_{r}=-\sum_{i\in \mathcal{S}_{r}}p_{\text{out},i}+\sum_{i\in \mathcal{S}_{\bar{r}}}p_{\text{in},i},\tag{4.6}
$$

which does not depend on $p_{\text{flip}}$ at all, since we do not discriminate between up and down spins in the set $\mathcal{S}_{r}$, and the changes in its size are a function of the behavior of neighboring spins of the members of this set.

By taking the difference of Eqs. (4.4) and (4.5), we get the change in the unnormalized reversible magnetization:

$$
dM_{r}=dN_{r\uparrow}-dN_{r\downarrow}.\tag{4.7}
$$

We can simplify the expression that results upon substitution of the actual forms of $dN_{r\uparrow}$ and $dN_{r\downarrow}$ by anticipating that the probabilities $p_{\text{out},i}$ and $p_{\text{in},i}$ will also be proportional to $dt$. Thus terms such as $p_{\text{flip}}p_{\text{out},i}$ are $O(dt)^{2}$ and may be omitted. In this way, we get

$$
dM_{r}=-2p_{\text{flip}}M_{r}-\left(\sum_{i\in \mathcal{S}_{r\uparrow}}p_{\text{out},i}-\sum_{i\in \mathcal{S}_{r\downarrow}}p_{\text{out},i}\right)+\left(\sum_{i\in \mathcal{S}_{\bar{r}\uparrow}}p_{\text{in},i}-\sum_{i\in \mathcal{S}_{\bar{r}\downarrow}}p_{\text{in},i}\right).\tag{4.8}
$$

Lastly, we find $dM$, the change in the total unnormalized magnetization. Since this change can come about only by the flipping of reversible spins, and since each flip changes $M$ by 2,

$$
\begin{aligned}
dM&=-2\sum_{i\in \mathcal{S}_{r\uparrow}}p_{\text{flip}}+2\sum_{i\in \mathcal{S}_{r\downarrow}}p_{\text{flip}}\\
&=-2p_{\text{flip}}M_{r}.
\end{aligned}\tag{4.9}
$$

### 4.2. The probabilities $p_{\text{in}}$ and $p_{\text{out}}$

For the equations for $dN_{r}$, $dM_{r}$, and $dM$ to be useful, we need the probabilities $p_{\text{in}}$ and $p_{\text{out}}$. Let us begin by considering a nonreversible spin $i\in \mathcal{S}_{\bar{r}}$ that sees a bias $E_{i}>W$. For this spin to move into the reversible range, reversible spins at other sites will need to flip and alter the bias at site $i$ to satisfy $|E_{i}'|\leq W$, where the prime indicates the bias after a time interval $dt$. Now,

$$
E_{i}'=E_{i}+\sum_{j\in \mathcal{S}_{r}}'K_{ij}d\sigma_{j}.\tag{4.10}
$$

Here, the site $i$ is excluded from the sum, and $d\sigma_{j}$ is the change in the spin at site $j$ in the time $dt$. The requirement that $|E_{i}'|<W$ implies that only a particular set of reversible spins determined by the geometry of the lattice and the form of the dipole kernel $K_{ij}$ can be effective in making spin $i$ reversible. We shall refer to such spins as triggering spins. To estimate their number we make the critical simplification that we may ignore simultaneous spin flips since such processes will have a very low probability proportional to $(dt)^{2}$, which may be neglected as $dt$ is infinitesimal. Thus, in Eq. (4.10),

we take $d\sigma_j=0$ for all but one distant reversible spin. Taking this spin to be up, so that $d\sigma_j=-2$, we get
$$
E_{i}'=E_{i}-2K_{ij}(\uparrow),\qquad(4.11)
$$
where the arrow in $K_{ij}(\uparrow)$ indicates that the distant spin is up. The condition $|E_{i}'|<W$ then implies that
$$
\frac{E_{i}-W}{2}\leq K_{ij}(\uparrow)\leq\frac{E_{i}+W}{2}.\qquad(4.12)
$$

Similarly, if the distant spin is down, we require
$$
\frac{-E_{i}-W}{2}\leq K_{ij}(\downarrow)\leq\frac{-E_{i}+W}{2}.\qquad(4.13)
$$

We now find the number of sites for which the couplings $K_{ij}$ lie in the range (4.12) or (4.13). If we define
$$
K_{1}(E_{i})=\frac{1}{2}(E_{i}-W),\quad K_{2}(E_{i})=\frac{1}{2}(E_{i}+W),\qquad(4.14)
$$
then these two ranges correspond to intervals $[K_{1},K_{2}]$, and $[-K_{2},-K_{1}]$ in which $K_{ij}$ must lie. Let us denote the numbers of sites in each interval by $N_{[K_{1},K_{2}]}$ and $N_{[-K_{2},-K_{1}]}$. We have
$$
N_{[K_{1},K_{2}]}=\int_{K_{1}}^{K_{2}}g(K)\,dK,\qquad(4.15)
$$
and similarly for $N_{[-K_{2},-K_{1}]}$, where $g(K)$ is the density of dipole couplings found in Ref. [15]. That is, $g(K)dK$ is the number of sites for which the coupling to a central site lies between $K$ and $K+dK$. We have
$$
g(K)=\alpha\frac{E_{dm}}{K^{2}},\quad\alpha=\frac{16\pi}{9\sqrt{3}}.\qquad(4.16)
$$

It then follows that
$$
\begin{aligned}
N_{[K_{1},K_{2}]}&=N_{[-K_{2},-K_{1}]}\\
&=\alpha E_{dm}\left(\frac{1}{K_{1}}-\frac{1}{K_{2}}\right)\\
&=4\alpha\frac{E_{dm}W}{E_{i}^{2}-W^{2}}.
\end{aligned}\qquad(4.17)(4.18)
$$

Since the number of distant sites at which a triggering spin could be located is independent of whether that spin is up or down, we can calculate the probability that spin $i$ will become reversible, that is to say $p_{\text{in},i}$, as the product of three factors: (i) the number (4.18), (ii) the fraction of these sites at which the spin is itself reversible, $n_{r}$, and (iii) the probability that any one of these spins will flip, $p_{\text{flip}}$. Thus,
$$
p_{\text{in},i}=4\alpha n_{r}\frac{E_{dm}W}{E_{i}^{2}-W^{2}}\Gamma_{0}dt.\qquad(4.19)
$$

The above calculation assumes once again that the local reversible fraction $n_{r}$ in the vicinity of spin $i$ is spatially homogeneous, and thus independent of the location of site $i$.

We next turn to the calculation of $p_{\text{out}}$, which proceeds in close parallel to that of $p_{\text{in}}$. Consider a reversible spin at site $i$, i.e., the bias $E_{i}$ obeys $|E_{i}|\leq W$. We refer to this site as the central reversible spin. This spin will become nonreversible if a distant reversible spin flips in such a way as to push the bias at site $i$ outside the interval $[-W,W]$. Suppose the distant spin flips from up to down. Since we have $|E_{i}|\leq W$ and want $|E_{i}'|>W$, the coupling $K_{ij}$ must be such that
$$
K_{ij}\notin[K_{1},K_{2}],\qquad(4.20)
$$

where $K_1$ and $K_2$ are as defined in Eq. (4.14). Noting that now $K_1 < 0$ and $K_2 > 0$, the number of sites that meet this requirement is given by

$$
\int_{-\infty}^{K_{1}} g(K) d K+\int_{K_{2}}^{\infty} g(K) d K=4 \alpha \frac{E_{d m} W}{W^{2}-E_{i}^{2}}. \tag{4.21}
$$

Similarly, if the distant spin flips from down to up, the condition on $K_{ij}$ is

$$
K_{i j} \notin\left[-K_{2},-K_{1}\right], \tag{4.22}
$$

which is met by a number of sites equal to

$$
\int_{-\infty}^{-K_{2}} g(K) d K+\int_{-K_{1}}^{\infty} g(K) d K=4 \alpha \frac{E_{d m} W}{W^{2}-E_{i}^{2}}, \tag{4.23}
$$

which is the same as Eq. (4.21). Thus, once again, the number of sites on which a triggering spin can be located is independent of whether that spin is up or down, and we may calculate $p_{\text{out},i}$ as the product of (i) the number of sites (4.21), (ii) the fraction $n_r$ that the spin on one of these sites is reversible, and (iii) the probability $\Gamma_0 dt$ that this spin will indeed flip. Thus,

$$
p_{\text{out}, i}=4 \alpha n_{r} \frac{E_{d m} W}{W^{2}-E_{i}^{2}} \Gamma_{0} d t. \tag{4.24}
$$

The expressions (4.19) and (4.24) suffer from unpleasant singularities when $E_i = \pm W$. These singularities are unphysical, and are a consequence of using the modified spin-flip probability (3.1) with the hard cutoffs at $\pm W$. Better estimates are obtained by noting that for $p_{\text{in},i}$, $|E_i|$ is likely to be much bigger than $W$, while for $p_{\text{out},i}$ the converse is true. We therefore neglect the term $W^2$ in the denominator of Eq. (4.19) and $E_i^2$ in the denominator of Eq. (4.24), leading to the expressions

$$
p_{\text{in}}\left(E_{i}\right)=4 \alpha n_{r} \frac{E_{d m} W}{E_{i}^{2}} \Gamma_{0} d t, \tag{4.25}
$$

$$
p_{\text{out}}\left(E_{i}\right)=4 \alpha n_{r} \frac{E_{d m}}{W} \Gamma_{0} d t. \tag{4.26}
$$

We note here the intuitively reasonable fact that $p_{\text{out}}$ is much greater than $p_{\text{in}}$. The set $\delta_r$ is much smaller than $\delta_{\bar{r}}$, so an initially reversible spin will be knocked out of reversibility by almost all flips of neighboring spins. By contrast, to move an initially nonreversible spin into reversibility, one must cancel the preexisting bias at the nonreversible site nearly exactly, which can only be done by flipping distant spins at a very specific set of sites. For this same reason, $p_{\text{out},i}$ essentially does not depend on $E_i$, while $p_{\text{in},i}$ does.

Note also that $p_{\text{in}}$ and $p_{\text{out}}$ are both proportional to $dt$ as anticipated earlier.

### 4.3. The rate equations

We now substitute Eqs. (4.19) and (4.24) into Eqs. (4.6), (4.8) and (4.9) for $dN_r$, $dM_r$, and $dM$, and divide by the total number of spins $N$ at the same time in order to get equations for intensive quantities. Let us begin by considering the two sums in Eq. (4.6) one by one. Since $p_{\text{out},i}$ is independent of $E_i$ as noted above, we have

$$
\frac{1}{N} \sum_{i \in \mathcal{S}_{r}} p_{\text{out}, i}=p_{\text{out}} \frac{N_{r}}{N}=4 \alpha n_{r}^{2} \frac{E_{d m}}{W} \Gamma_{0} d t. \tag{4.27}
$$

For the second sum, we need to sum over the set $\delta_{\bar{r}}$. We do this by including all sites where the bias exceeds $W$ in magnitude. This leads to the approximation

$$
\frac{1}{N} \sum_{i \in \mathcal{S}_{\bar{r}}} p_{\text{in}, i}=4 \alpha n_{r} \frac{E_{d m}}{W} \mathcal{F} \Gamma_{0} d t, \tag{4.28}
$$


where $\mathcal{F}$ is a dimensionless functional of the bias distribution $\rho(E)$, given by
$$
\mathcal{F}[\rho(E)]=W^{2} \int_{|E|>W} \frac{\rho(E)}{E^{2}} d E. \tag{4.29}
$$

Hence,
$$
\frac{d n_{r}}{d t}=-4 \alpha \Gamma_{0} \frac{E_{d m}}{W} n_{r}\left(n_{r}-\mathcal{F}\right). \tag{4.30}
$$

Next, we examine Eq. (4.8) for $d M_{r} / d t$. For the term with the sums over the sets $\mathcal{s}_{r \uparrow}$ and $\mathcal{s}_{r \downarrow}$, we have,
$$
\frac{1}{N}\left(\sum_{i \in \mathcal{s}_{r \uparrow}} p_{\text {out }, i}-\sum_{i \in \mathcal{s}_{r \downarrow}} p_{\text {out }, i}\right)=4 \alpha n_{r} m_{r} \frac{E_{d m}}{W} \Gamma_{0} d t. \tag{4.31}
$$

For the remaining two sums, we estimate the sizes of the sets $\mathcal{s}_{\bar{r} \uparrow}$ and $\mathcal{s}_{\bar{r} \downarrow}$ as $N_{\uparrow}$ and $N_{\downarrow}$ times the size of $\mathcal{s}_{\bar{r}}$ on the theory that when $n_{r} \ll 1$, most of the spins are nonreversible and the bias at any site is uncorrelated with whether the spin at that site is up or down, and that when $n_{r} \simeq 1, m \simeq m_{r}$. It follows that
$$
\frac{1}{N}\left(\sum_{i \in \mathcal{s}_{\bar{r} \uparrow}} p_{\text {in }, i}-\sum_{i \in \mathcal{s}_{\bar{r} \downarrow}} p_{\text {in }, i}\right) \simeq 4 \alpha n_{r} m \frac{E_{d m}}{W} \mathcal{F} \Gamma_{0} d t. \tag{4.32}
$$

Hence,
$$
\frac{d m_{r}}{d t}=-2 \Gamma_{0} m_{r}-4 \alpha \Gamma_{0} \frac{E_{d m}}{W} n_{r}\left(m_{r}-m \mathcal{F}\right). \tag{4.33}
$$

Lastly, we obtain the equation for $d m / d t$, which is the simplest of all:
$$
\frac{d m}{d t}=-2 \Gamma_{0} m_{r}. \tag{4.34}
$$

Eqs. (4.30), (4.33) and (4.34) are the desired rate equations. They are manifestly nonlinear, but more importantly and contrary to our initial hope, they are not a closed system because of the presence of the functional $\mathcal{F}$ of the full bias distribution $\rho(E)$. At present this puts a big limitation on their use. For the relaxation problem we have been able to circumvent this limitation by constructing an interpolation form for $\rho(E)$ which we believe is reasonably accurate and self-consistent over a wide range of times, well past that over which the square-root time development is seen. We describe our approximation for $\rho(E)$ in the next section.

## 5. The bias distribution

### 5.1. The three-Gaussian approximation

As seen from the Monte Carlo simulations, the bias distribution at short times is dominated by three peaks at $E=0, E=-4 E_{d m}$, and $E=8 E_{d m}$. The locations of the two side peaks are a strong indicator of their origin. Consider a site with its six nearest neighbors. Four of these neighbors are in the $x y$ plane, and two are along the $z$ axis. If any of the neighboring spins in the $x y$ plane flips from up to down, the bias at the central site will change by an amount $-4 E_{d m}$, while if any of the $z$ axis neighbors flips, the field at the central site will change by $8 E_{d m}$. This explains the peak locations. Further, since there are twice as many near neighbors of any site in the $x y$ plane as there are along the $z$ axis, we should expect the peak at $-4 E_{d m}$ to be about twice as high as the peak at $8 E_{d m}$ as long as $N_{r} \ll N$. This is also seen in the data. The smaller peak at $-8 E_{d m}$ and shoulder at $4 E_{d m}$ can also be associated with spin flips at pairs of near neighbor sites.

Motivated by this idea, we try and represent $\rho(E)$ as a sum of three Gaussians centered at $0, -4E_{dm}$, and $8E_{dm}$. Suppose that at a given time, $N_\downarrow$ spins have flipped where $N_\downarrow \ll N$, allowing us to ignore the possibility that two flipped spins are near neighbors of each other or even of a common third spin. Then there are $4N_\downarrow$ spins that have a flipped neighbor in the $xy$ plane, and $2N_\downarrow$ spins that have a flipped neighbor along the $z$ axis, leaving $N - 6N_\downarrow$ spins which have no flipped neighbors at all. Thus the weights of the $0, -4E_{dm}$ and $8E_{dm}$ peaks are proportional to $(1 - 6n_\downarrow)$, $4n_\downarrow$, and $2n_\downarrow$ respectively. We can further argue that the widths of all three peaks are equal and proportional to $n_\downarrow^{1/2}$, since the fields at sites far away from all flipped spins should continue to vanish on average, but should have a variance that grows linearly with the number of flipped spins. For a site next to a flipped spin, this variance is simply realized around the shift produced by the flipped neighbor. Thus for $n_\downarrow \ll 1$, the three-Gaussian approximation (TGA) to $\rho(E)$ takes the form

$$
\rho(E) \simeq (1 - 6n_\downarrow)g_0(E) + 2n_\downarrow g_+(E) + 4n_\downarrow g_-(E), \tag{5.1}
$$

where (with $\alpha = 0, +, \text{or} \, -, \text{and} \, E_0 = 0, \, E_+ = 8E_{dm}, \text{and} \, E_- = -4E_{dm}$)

$$
g_\alpha(E) = (2\pi n_\downarrow \tilde{\sigma}^2)^{-1/2} e^{-(E-E_\alpha)^2/2 n_\downarrow \tilde{\sigma}^2}, \quad (n_\downarrow \ll 1). \tag{5.2}
$$

The quantity $\tilde{\sigma}$ is $E_{dm}$ times an unknown constant of order unity.

The arguments underlying Eq. (5.1) start to become questionable for $n_\downarrow$ as small as 0.1, since sites with two near neighbor flipped spins start to become significant. To enable us to consider larger values of $n_\downarrow$, we generalize the TGA to the form

$$
\rho(E) \simeq a_0 g_0(E) + a_+ g_+(E) + a_- g_-(E), \tag{5.3}
$$

where

$$
g_\alpha(E) = (2\pi \sigma^2)^{-1/2} e^{-(E-E_\alpha)^2/2 \sigma^2}. \tag{5.4}
$$

That is, the peaks of the three Gaussians are still taken to be at $0, -4E_{dn}$ and $8E_{dn}$, the widths are taken to have a common value $\sigma$ not necessarily proportional to $n_\downarrow^{1/2}$, and the weights $a_0, a_+$, and $a_-$ are allowed to become arbitrary. We will determine these weights and the width by the procedure described in the next subsection. The form (5.1) at small $n_\downarrow$ will serve as a check on the procedure.

It is apparent that the TGA is qualitatively incapable of accounting for the very narrow hole that is burned in the distribution at long times, but here a different approximation scheme can be developed as the origin of the hole is physically obvious.

### 5.2. Moments of the bias distribution for uncorrelated spins

Our discussion above implies that for very small $n_\downarrow$, the flipped spins are randomly distributed in the lattice without any spatial correlations. We therefore extend this idea to larger $n_\downarrow$ and consider a model in which the spin on each site is up or down independently of other spins, with probabilities $(1 \pm m)/2$, where $m$ is the magnetization. We then calculate the first three moments of this model, and match those to the moments of the TGA, Eq. (5.3). These three moments, plus the normalization (or zeroth moment) give us the four conditions needed to determine the four quantities $a_0, a_-, a_+$, and $\sigma$.

The bias at any site $i$ is given by

$$
E_i = \sum_{j \neq i} K_{ij} \sigma_j. \tag{5.5}
$$

Consider first the uniform spin configuration with $m = 1$, i.e., $\sigma_i = 1$ for all $i$. We know that in this case the bias vanishes at all sites except those in a narrow layer near the surface of our spherical sample. Hence we may take

$$
\sum_{j \neq i} K_{ij} = 0 \tag{5.6}
$$

for essentially all sites. This result will be employed repeatedly in the calculations of the moments for configurations in which $m \neq 1$. Thus, for the first moment, we have

$$
\begin{aligned}
\left\langle E_{i}\right\rangle &=\sum_{j \neq i} K_{i j}\left\langle\sigma_{j}\right\rangle \\
&=\sum_{j \neq i} K_{i j} m \\
&=0.
\end{aligned}
\tag{5.7}
$$

Similarly, for the second moment, we get

$$
\left\langle E_{i}^{2}\right\rangle=\sum_{j, k}^{\prime} K_{i j} K_{i k}\left\langle\sigma_{j} \sigma_{k}\right\rangle.
\tag{5.8}
$$

The prime on the sum signifies that $j \neq i$ and $k \neq i$. Now $\langle\sigma_{j} \sigma_{k}\rangle$ equals 1 if $j=k$, and $m^{2}$ if $j \neq k$. Hence,

$$
\begin{aligned}
\left\langle E_{i}^{2}\right\rangle &=\sum_{j, k}^{\prime} K_{i j} K_{i k}\left[\delta_{j k}+\left(1-\delta_{j k}\right) m^{2}\right] \\
&=\sum_{j \neq i} K_{i j}^{2}\left(1-m^{2}\right)+m^{2} \sum_{j}^{\prime} K_{i j} \sum_{k}^{\prime} K_{i k} \\
&=\kappa_{2} E_{d m}^{2}\left(1-m^{2}\right),
\end{aligned}
\tag{5.9}
$$

where we have used Eq. (5.6), and defined

$$
\kappa_{2}=\frac{1}{E_{d m}^{2}} \sum_{j \neq i} K_{i j}^{2}.
\tag{5.10}
$$

Numerical evaluation of the sum gives

$$
\kappa_{2}=53.427.
\tag{5.11}
$$

For the third moment, we have

$$
\left\langle E_{i}^{3}\right\rangle=\sum_{j, k, l}^{\prime} K_{i j} K_{i k} K_{i l}\left\langle\sigma_{j} \sigma_{k} \sigma_{l}\right\rangle.
\tag{5.12}
$$

Again, the prime signifies that $j \neq i, k \neq i$, and $l \neq i$. The only issue requiring care in performing the sum is the enumeration of the various cases of equality or inequality of the indices $j, k$, and $l$. The first case is where all three indices are distinct. Then $\langle\sigma_{j} \sigma_{k} \sigma_{l}\rangle=m^{3}$, and the contribution of this case to $\langle E_{i}^{3}\rangle$ can be evaluated as

$$
\begin{aligned}
\left\langle E_{i}^{3}\right\rangle_{1} &=m^{3} \sum_{j, k, l}^{\prime} K_{i j} K_{i k} K_{i l}\left(1-\delta_{j k}\right)\left(1-\delta_{k l}\right)\left(1-\delta_{l j}\right) \\
&=m^{3} \sum_{j, k, l}^{\prime} K_{i j} K_{i k} K_{i l}\left(1-3 \delta_{j k}+3 \delta_{j k} \delta_{j l}-\delta_{j k} \delta_{k l} \delta_{l j}\right) \\
&=m^{3}\left[\left(\sum_{j}^{\prime} K_{i j}\right)^{3}-3 \sum_{j}^{\prime} K_{i j}^{2} \sum_{l}^{\prime} K_{i l}+3 \sum_{j}^{\prime} K_{i j}^{3}-\sum_{j}^{\prime} K_{i j}^{3}\right] \\
&=2 m^{3} \sum_{j \neq i} K_{i j}^{3}.
\end{aligned}
\tag{5.13}
$$

In line 2 above we have used the symmetry of the summand, and in line 4 we have used Eq. (5.6).

The second case is where two of the indices $j$, $k$, and $l$ are the same, but distinct from the third. Now $\langle\sigma_j\sigma_k\sigma_l\rangle = m$. This case has three identically contributing subcases, and for its net contribution to $\langle E_i^3\rangle$ we have

$$
\begin{aligned}
\langle E_i^3\rangle_2 &= 3m \sum_{j,k,l}' K_{ij}K_{ik}K_{il} \delta_{jk}(1 - \delta_{jl}) \\
&= 3m\left[\sum_{j}' K_{ij}^2 \sum_{k}' K_{ik} - \sum_{j}' K_{ij}^3\right] \\
&= -3m \sum_{j\neq i} K_{ij}^3,
\end{aligned}
\tag{5.14}
$$

where we have again used Eq. (5.6) in the last line.

The third and last case is that where $j = k = l$. Now $\langle\sigma_j\sigma_k\sigma_l\rangle = m$, and the contribution to $\langle E_i^3\rangle$ is, therefore,

$$
\langle E_i^3\rangle_3 = m \sum_{j\neq i} K_{ij}^3.
\tag{5.15}
$$

Adding together Eqs. (5.13)-(5.15), we get

$$
\langle E_i^3\rangle = -2m(1 - m^2) \sum_{j\neq i} K_{ij}^3.
\tag{5.16}
$$

We write this as

$$
\langle E_i^3\rangle = \kappa_3 E_{dm}^3 m(1 - m^2),
\tag{5.17}
$$

where

$$
\kappa_3 = -\frac{2}{E_{dm}^3} \sum_{j\neq i} K_{ij}^3 = 190.47,
\tag{5.18}
$$

and the last result is found numerically.

It should be noted that in this model, the moments of $E$ are simply geometrical constants determined by the type of lattice times the appropriate power of the energy scale $E_{dm}$.

### 5.3. Moment matching

We now match the moments from the previous subsection with those of the three-Gaussian approximation (5.3). The latter yields

$$
\langle E\rangle = 8E_{dm}a_+ - 4E_{dm}a_-,
\tag{5.19}
$$

$$
\langle E^2\rangle = \sigma^2(a_0 + a_+ + a_-) + 64E_{dm}^2 a_+ + 16E_{dm}^2 a_-,
\tag{5.20}
$$

$$
\langle E^3\rangle = 12E_{dm}\sigma^2(2a_+ - a_-) + 512E_{dm}^3 a_+ - 64E_{dm}^3 a_-.
\tag{5.21}
$$

Equating these moments to those from the uncorrelated spin distribution yields

$$
4E_{dm}(2a_+ - a_-) = 0,
\tag{5.22}
$$

$$
\sigma^2(a_0 + a_+ + a_-) + 16E_{dm}^2(4a_+ + a_-) = \kappa_2 E_{dm}^2(1 - m^2),
\tag{5.23}
$$

$$
12E_{dm}\sigma^2(2a_+ - a_-) + 64E_{dm}^3(8a_+ - a_-) = \kappa_3 E_{dm}^3 m(1 - m^2).
\tag{5.24}
$$

Solving these equations along with the normalization condition,

$$
a_0 + a_+ + a_- = 1,
\tag{5.25}
$$

![](./images/813227439168684033_11.jpg)

Fig. 8. Comparison between the three-Gaussian approximation (TGA) to the bias distribution and the simulation results for short times. The sample has $N=82,519$ spins, and all other parameters are as in previous figures.

we obtain

$$
a_{0}=1-\frac{\kappa_{3}}{128} m\left(1-m^{2}\right), \tag{5.26}
$$

$$
a_{+}=\frac{\kappa_{3}}{384} m\left(1-m^{2}\right), \tag{5.27}
$$

$$
a_{-}=\frac{\kappa_{3}}{192} m\left(1-m^{2}\right), \tag{5.28}
$$

$$
\sigma^{2}=\frac{1}{4}\left(4 \kappa_{2}-\kappa_{3} m\right)\left(1-m^{2}\right) E_{d m}^{2}. \tag{5.29}
$$

At this point let us ask whether the solution (5.26)-(5.29) approaches Eqs. (5.1) and (5.2) when $n_{\downarrow} \ll 1$. In that limit, since $m=1-2 n_{\downarrow}, m\left(1-m^{2}\right) \approx\left(1-m^{2}\right)=4 n_{\downarrow}$. Feeding in the value $\kappa_{3}=190.2$, we get $a_{+}=1.98 n_{\downarrow}$, and $a_{-}=3.96 n_{\downarrow}$, instead of $2 n_{\downarrow}$ and $4 n_{\downarrow}$. The differences are rather small, however, and can be eliminated entirely if we make the replacement

$$
\kappa_{3} \rightarrow \kappa_{3}^{\prime}=192. \tag{5.30}
$$

This leads to the final forms we shall use in our three-Gaussian approximation, Eqs. (5.3) and (5.4):

$$
a_{0}=1-\frac{3}{2} m\left(1-m^{2}\right), \tag{5.31}
$$

$$
a_{+}=\frac{1}{2} m\left(1-m^{2}\right), \tag{5.32}
$$

$$
a_{-}=m\left(1-m^{2}\right), \tag{5.33}
$$

$$
\sigma^{2}=\left(\kappa_{2}-48 m\right)\left(1-m^{2}\right) E_{d m}^{2}. \tag{5.34}
$$

### 5.4. Comparison with simulations

When we now compare the TGA with the simulations, we discover that the agreement is off by $\sim 10 \%$ if we use the value $\kappa_{2}=53.4$. This value was calculated for an infinite lattice, and for a finite sized sample the variance of $E_{i}^{2}$ should be smaller. Using the value 50 appropriate to the 82519 spin sample, we find that the agreement is considerably improved. In Fig. 8 we show the TGA with the choice $\kappa_{2}=50$ along with the results of the simulations for the 82519 spin sample for $t / \tau=0.1,0.3$, and 0.5 , where $\tau=E_{d m} / \Delta^{2}$. At these three times, $m=0.93,0.89$, and 0.86 . The agreement becomes poorer for larger $t$, and it is about as good as could be expected given how simple-minded the approximation is.

## 6. Short-time decay of magnetization: the $\sqrt{t}$ law

In Fig. 2 we show $m(t)$ for short times from our simulations, and from solving the rate equations with the value $\kappa_{2}=53.4$. As can be seen the general trend is the same, although the detailed

![](./images/813227439168684033_12.jpg)

Fig. 9. Same as Fig. 2, except that the rate equations are solved using $\kappa _{2}=50$.

agreement is only good to about 3%. Once again, the agreement is improved if we set $\kappa _{2}=50$, as shown in Fig. 9. The same data are shown on a log-log plot in Fig. 10. As can be seen, both the simulations and the rate equation show a power law behavior, with the same exponent. The best fit gives an exponent of 0.46, which is very close to 0.5 as it would be for $\sqrt{t}$ behavior. We now show that this behavior can be understood analytically on the basis of our rate equations, and that this exponent does not depend on the choice of $\kappa _{2}$.

### 6.1. Solution of the rate equations
The first key point is that starting from a delta-function at $t=0$, the bias distribution becomes broader than the reversibility region at some ultra-short time when the fraction of flipped spins is still very small. From Eq. (5.29), we find that for $n_{\downarrow }\ll A^{2}/2\kappa _{3}$,
$$
\sigma ^{2}\approx A^{2}E_{dm}^{2}n_{\downarrow },\qquad(6.1)
$$
where $A^{2}=4\kappa _{2}-\kappa _{3}$. Thus $\sigma \lesssim W$ only as long as $n_{\downarrow }\lesssim (W/AE_{dm})^{2}$, which is of order $10^{-3}$. For such ultrasmall values of $n_{\downarrow }$, $n_{r}=1-6n_{\downarrow }$, and $\mathcal{F }\simeq 0$, so the rate equation for $n_{r}$ simplifies to
$$
\frac{dn_{\downarrow }}{dt}=\frac{2}{3}\alpha \Gamma _{0}\frac{E_{dm}}{W}.\qquad(6.2)
$$
This has the solution $n_{\downarrow }=(2\alpha \Gamma _{0}E_{dm}/3W)t$, and so the condition that $\sigma \lesssim W$ holds only for $t\lesssim t_{\text{us}}$, where
$$
t_{\text{us}}\sim \frac{1}{A^{2}}\left( \frac{W}{E_{dm}} \right) ^{4}\tau \qquad(6.3)
$$
is an ultra-short time scale of order $10^{-5}\tau$.

It follows that there is a large range of times, $t_{\text{us}}\lesssim t\ll \tau$, for which $\sigma \gg W$ even though $n_{\downarrow }\ll 1$, i.e., very few spins are flipped. Thus almost all the weight in the bias distribution is still in the central Gaussian, i.e., $a_{0}\simeq 1$, and the dimensionless functional that determines the repopulation of the reversibility region can be approximated as
$$
\mathcal{F }=2\frac{W^{2}}{\sqrt{2\pi \sigma ^{2}}}\int_{W}^{\infty }\frac{e^{-E^{2}/2\sigma ^{2}}}{E^{2}}dE.\qquad(6.4)
$$

![](./images/813227439168684033_13.jpg)

Fig. 10. Log-log plot of the short-time behavior of the magnetization. Also shown is the solution given by the rate equations with $\kappa_{2}=50$, and a linear fit to the latter. This fit gives an exponent equal to 0.46, close to 0.5 for an exact square root.

Now, by integrating by parts, we get
$$
\begin{aligned}
\int_{W}^{\infty} \frac{e^{-E^{2 / 2} \sigma^{2}}}{E^{2}} d E &=\frac{1}{W} e^{-W^{2 / 2} \sigma^{2}}-\frac{1}{\sigma^{2}} \int_{W}^{\infty} e^{-E^{2 / 2} \sigma^{2}} d E \\
&=\frac{1}{W} e^{-W^{2 / 2} \sigma^{2}}-\frac{1}{\sigma^{2}}\left[\sqrt{\frac{\pi}{2}} \sigma-\int_{0}^{W} e^{-E^{2 / 2} \sigma^{2}} d E\right].
\end{aligned}\tag{6.5}
$$

The last expression can be expanded in powers of $W$, and we get
$$
\mathcal{F} \simeq \sqrt{\frac{2}{\pi}} \frac{W}{\sigma}\left(1-\sqrt{\frac{\pi}{2}} \frac{W}{\sigma}+\cdots\right).\tag{6.6}
$$

The second key point is that even though $n_{\downarrow} \ll 1$, almost all the spins have been knocked out of the reversibility region, i.e., $n_{r} \ll 1$. To see this we again approximate the bias distribution by neglecting the weight outside the central Gaussian, and setting $a_{0}=1$, so
$$
n_{r} \simeq \frac{1}{\sqrt{2 \pi \sigma^{2}}} \int_{-W}^{W} e^{-E^{2 / 2} \sigma^{2}} d E.\tag{6.7}
$$

Expanding the integrand in powers of $E$ and integrating, we get
$$
n_{r} \simeq \sqrt{\frac{2}{\pi}} \frac{W}{\sigma}\left(1-\frac{W^{2}}{6 \sigma^{2}}+\cdots\right).\tag{6.8}
$$

Thus, to first order in $W / \sigma, n_{r}=\mathcal{F}$, and the difference is of higher order:
$$
n_{r}-\mathcal{F}=\frac{W^{2}}{\sigma^{2}}.\tag{6.9}
$$

We can express this in terms of $n_{r}$ itself by using Eq. (6.8). We have
$$
\frac{W}{\sigma} \simeq \sqrt{\frac{\pi}{2}} n_{r},\tag{6.10}
$$
so
$$
n_{r}-\mathcal{F}=\frac{\pi}{2} n_{r}^{2}.\tag{6.11}
$$

The rate equation for $n_r$ then reads
$$
\frac{d n_{r}}{d t}=-\frac{\pi}{2} \zeta n_{r}^{3},\qquad(6.12)
$$
where we have defined
$$
\zeta=4 \alpha \Gamma_{0} \frac{E_{d m}}{W}=\alpha \frac{\Delta_{2}^{2} E_{d m}}{W^{2}}.\qquad(6.13)
$$

The integration of Eq. (6.12) is elementary. Since this equation only holds for $t \gtrsim t_{\mathrm{us}}$, we can write the integral in the form
$$
\frac{1}{n_{r}^{2}}=\pi \zeta\left(t+t^{*}\right),\qquad(6.14)
$$
where $t^{*}$ is a time of order $t_{\mathrm{us}}$. We thus have an explicit solution for the time dependence of the reversible fraction:
$$
n_{r}(t)=\frac{1}{\sqrt{\pi \zeta}} \frac{1}{\left(t+t^{*}\right)^{1 / 2}}.\qquad(6.15)
$$

The other rate equations can now be solved as follows. We have by definition,
$$
n_{r}=n_{r \uparrow}+n_{r \downarrow}, \quad m_{r}=n_{r \uparrow}-n_{r \downarrow}.\qquad(6.16)
$$

Since $n_{r \downarrow}<n_{\downarrow} \ll 1$, the answer for $m_{r}$ is immediate:
$$
m_{r} \approx n_{r \uparrow} \approx n_{r}=\frac{1}{\sqrt{\pi \zeta}} \frac{1}{\left(t+t^{*}\right)^{1 / 2}}.\qquad(6.17)
$$

The rate equation for $m$ now reads
$$
\frac{d m}{d t}=-\frac{2 \Gamma_{0}}{\sqrt{\pi \zeta}} \frac{1}{\left(t+t^{*}\right)^{1 / 2}}.\qquad(6.18)
$$

The integration is again elementary. Assuming that $t_{\mathrm{us}} \lesssim t \lesssim \tau$, we can write the result as
$$
m(t) \simeq 1-\sqrt{\Gamma_{1 / 2} t},\qquad(6.19)
$$
where
$$
\Gamma_{1 / 2}=16 \frac{\Gamma_{0}^{2}}{\pi \zeta}=\frac{1}{\pi \alpha} \frac{\Delta_{2}^{2}}{E_{d m}}.\qquad(6.20)
$$

Eq. (6.19) is the experimentally observed $\sqrt{t}$ law.

### 6.2. Comparison with previous work

As noted in Section 1, earlier explanations of the $\sqrt{t}$ law are given in Refs. [9,4]. Ref. [9] writes down a formal kinetic equation for the joint probability distribution of the spin and bias field at a site, in which the collision term is written in terms of the formal two-site distribution. As in the equations of the BBGKY hierarchy, such an equation is intractable unless some approximation is made for the two-site distribution. An equation for $d M / d t$ is then obtained from this kinetic equation by (apparently) neglecting the collision term completely. We see no a priori justification for this approximation, and that it works is somewhat fortuitous. Its success depends on the near-perfect cancellation between the depopulation and repopulation of the reversibility window implied by the near equality of $n_{r}$ and $\mathcal{F}$ (see Eqs. (6.6) and (6.8)). This cancellation does not appear to us to be obvious, since, as noted after Eq. (6.6), almost all the spins are knocked out of the reversibility region after an ultra short time. Secondly, and, crucially, Ref. [9] takes the one-site distribution as a cut-off Lorentzian, for which approximation the authors cite Refs. [17,18]. Ref. [17] is an abstract of

a talk at a meeting of the American Physical Society and contains no details. Details are given by Abragam [18], and the central point of the argument is that when $n_{\downarrow} \ll 1$, the half-width at half-maximum of the one-site distribution is proportional to $n_{\downarrow}$, and much less than the second moment of the distribution, which varies as $n_{\downarrow}^{1 / 2}$. A cut-off Lorentzian is a mathematically convenient distribution with this property, but it is not the only one. A perfect Lorentzian without a cutoff is obtained in the 'statistical theory' described by Abragam (for which again Ref. [17] is cited), but this theory allows the spins to approach arbitrarily close to one another, which is unphysical. Thus, while the basis for the Lorentzian form is physically plausible, it is not water-tight, and an independent analysis such as we have provided is useful. (Further, Abragam's argument is, strictly speaking, for the NMR line shape in magnetically dilute substances, and not for the actual dipole field distribution. This difference is however, minor, as the arguments are easily generalized.) As noted by Abragam at the beginning of his discussion, the real reason the width is much less than the second moment is that the latter acquires large contributions from clusters of two or more spins close to one another. Our three-Gaussian approximation is motivated by precisely such considerations, and as can be seen, gives a better description of the full time evolution of the dipole field distribution at moderately long times. Finally, as far as we can tell, the $\sqrt{t}$ curve in Fig. 1 of Ref. [9], is a fit with an adjustable coefficient, whereas we determine the coefficient completely.

The authors of Ref. [4] arrive at the $\sqrt{t}$ law by a different argument, which though heuristic, is very pretty. They reason that $\sigma(t)$ must be of the order of the typical dipole field when the spins start flipping, and thus proportional to $a^{3} / \ell^{3}(t)$, where $\ell(t)$ is the typical distance between reversed spins. They then note that $a^{3} / \ell^{3}(t) \propto n_{\downarrow}(t)$, so that $\sigma(t) \propto n_{\downarrow}(t)$. They then estimate $m_{r}(t)$ as $W / \sigma(t)$, from which it follows that $d m / d t \sim 1 / n_{\downarrow}(t)$, and that $n_{\downarrow}(t) \sim t^{1 / 2}$. As a by product, one also finds that $\sigma(t) \sim t^{1 / 2}$ and $n_{r}(t) \sim t^{-1 / 2}$. We find the same behavior for these quantities, so we vindicate the intuition of these authors, but we have also found the detailed scaling behavior of $m(t), n_{\downarrow}(t)$ and $\sigma(t)$ along with the prefactors. Our procedure is rather different. Instead of positing that $\sigma(t) \sim n_{\downarrow}(t)$ as our starting point, we find the delicate noncancellation between $n_{r}$ and $\mathscr{F}$ in order to first find the differential equation obeyed by $n_{r}(t)$, and determine that $n_{r}(t) \sim t^{-1 / 2}$, after which the equation for $m(t)$ is elementary. The agreement with [4] gives us encouragement that we can use our more detailed rate equations to analyze other experimental protocols in the future.

## Acknowledgments

This work was begun with support from the NSF via grant number DMR-0202165. We are indebted to Rahul Pandit and Nandini Trivedi for useful comments on Monte Carlo techniques.

## References

[1] C. Sangregorio, T. Ohm, C. Paulsen, R. Sessoli, D. Gatteschi, Phys. Rev. Lett. 78 (1997) 4645.
[2] T. Ohm, C. Sangregorio, C. Paulsen, Eur. Phys. J. B 6 (1998) 195.
[3] W. Wernsdorfer, T. Ohm, C. Sangregorio, R. Sessoli, D. Mailly, C. Paulsen, Phys. Rev. Lett. 82 (1999) 3903.
[4] D. Gatteschi, R. Sessoli, J. Villain, Molecular Nanomagnets, Oxford University Press, Oxford, 2006. This book gives a comprehensive and authoritative review of the entire field of SMM's. The problem of relaxation is especially (but not exclusively) discussed in Chapter 9.
[5] L. Miyashita, A. Caneschi, B. Barbara, Phys. Rev. Lett. 83 (1999) 2398.
[6] W. Wernsdorfer, A. Caneschi, R. Sessoli, D. Gatteschi, A. Cornia, V. Villar, C. Paulsen, Phys. Rev. Lett. 84 (2000) 2965.
[7] W. Wernsdorfer, R. Sessoli, A. Caneschi, D. Gatteschi, A. Cornia, Europhys. Lett. 50 (2000) 552.
[8] I.S. Tupitsyn, B. Barbara, in: J.S. Miller, M. Drillon (Eds.), Magnetism: Molecules to Materials III, Wiley-VCH, Weinheim, 2002.
[9] N.V. Prokofev, P. Stamp, Phys. Rev. Lett. 80 (1998) 5794; J. Low Temp. Phys. 113 (1998) 1147.
[10] A. Cuccoli, A. Fort, A. Rettori, E. Adam, J. Villain, Eur. Phys. J. B 12 (1999) 39.
[11] J.F. Fernandez, J.J. Alonso, Phys. Rev. Lett. 91 (2003) 047202;
J.F. Fernandez, J.J. Alonso, Phys. Rev. Lett. 92 (2004) 119702.
[12] S. Miyashita, K. Saito, J. Phys. Soc. Japan 70 (2001) 3238.
[13] J. Villain, Eur. Phys. J. B 48 (2005) 173.
[14] N.V. Prokofev, P. Stamp, J. Low Temp. Phys. 104 (1996) 143.
[15] A. Vijayaraghavan, A. Garg, Phys. Rev. B 79 (2009) 104423.
[16] It is apparent that the bias $E_{i}=2 \mu H_{i}$, where $\mu$ is the magnetic moment of a molecule, and $H_{i}$ is the magnetic field at the $i$ th site. We prefer to work with the bias as all interactions in the problem are then expressed in terms of energies.
[17] P.W. Anderson, Phys. Rev. 82 (1951) 341.
[18] A. Abragam, Principles of Nuclear Magnetism, Oxford University Press, Oxford, 1961, pp. 125-128. Sec. IV.IV.