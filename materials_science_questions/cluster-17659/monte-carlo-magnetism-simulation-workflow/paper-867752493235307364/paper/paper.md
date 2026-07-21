
# Quantum annealing of the p-spin model under inhomogeneous transverse field driving

Yuki Susa, \( ^{1,*} \)  Yu Yamashiro, \( ^{2} \)  Masayuki Yamamoto, \( ^{3} \)  Itay Hen, \( ^{4,5,6} \)  Daniel A. Lidar, \( ^{4,5,7,8} \)  and Hidetoshi Nishimori \( ^{1} \) 

 \( ^{1} \) Institute of Innovative Research, Tokyo Institute of Technology, Oh-okayama, Meguro-ku, Tokyo 152-8550, Japan

 \( ^{2} \) Department of Physics, Tokyo Institute of Technology, Oh-okayama, Meguro-ku, Tokyo 152-8550, Japan

 \( ^{3} \) Graduate School of Information Sciences, Tohoku University, Sendai 980-8579, Japan

 \( ^{4} \) Center for Quantum Information Science & Technology,

University of Southern California, Los Angeles, California 90089, USA

 \( ^{5} \) Department of Physics & Astronomy, University of Southern California, Los Angeles, California 90089, USA

 \( ^{6} \) Information Sciences Institute, University of Southern California, Marina del Rey, California 90292, USA

 \( ^{7} \) Department of Electrical Engineering, University of Southern California, Los Angeles, California 90089, USA

 \( ^{8} \) Department of Chemistry, University of Southern California, Los Angeles, California 90089, USA

(Dated: October 23, 2018)

We solve the mean-field-like p-spin Ising model under a spatiotemporal inhomogeneous transverse field to study the effects of inhomogeneity on the performance of quantum annealing. We previously found that the problematic first-order quantum phase transition that arises under the conventional homogeneous field protocol can be avoided if the temperature is zero and the local field is completely turned off site by site after a finite time. We show in the present paper that, when these ideal conditions are not satisfied, another series of first-order transitions appear, which prevents us from driving the system while avoiding first-order transitions. Nevertheless, under these nonideal conditions, quantitative improvements can be obtained in terms of narrower tunneling barriers in the free-energy landscape. A comparison with classical simulated annealing establishes a limited quantum advantage in the ideal case, since inhomogeneous temperature driving in simulated annealing cannot remove a first-order transition, in contrast to the quantum case. The classical model of spin-vector Monte Carlo is also analyzed, and we find it to have the same thermodynamic phase diagram as the quantum model in the ideal case, with deviations arising at non-zero temperature.

## I. INTRODUCTION

Quantum annealing (QA) is a metaheuristic for combinatorial optimization problems and is closely related to adiabatic quantum computation  \( [1-7] \) , in which the final-time classical ground state of an Ising Hamiltonian encodes the optimal solution of a combinatorial optimization problem  \( [8] \) . Quantum fluctuations are applied to the Ising model, first with a very large amplitude and then slowly reduced to zero, to reach the ground state of the original Ising model representing the solution to the combinatorial optimization problem. The amplitude of quantum fluctuations is a key control parameter, analog to the temperature in the classical analog, simulated annealing  \( [9] \) .

As the amplitude of quantum fluctuations is reduced, quite generally a quantum phase transition takes place in the thermodynamic limit and at zero temperature from a disordered paramagnetic phase to an ordered phase. The existence of such a phase transition can be a serious problem for QA because it may slow down the annealing process significantly. This can be understood in terms of the adiabatic theorem of quantum mechanics, which states that a sufficient condition for the system to stay in the instantaneous ground state is that the total evolution time is inversely proportional to a polynomial of the energy gap between the instantaneous ground state and the first excited state  \( [10, 11] \) . It is known empirically that the energy gap decreases exponentially as a function of the system size at a first-order quantum phase transition \( ^{1} \)  whereas the scaling of gap decrease is significantly milder, i.e., polynomial in the system size, at a second-order transition as expected generally from finite-size scaling  \( [14] \) . This, in combination with the adiabatic theorem, means that the order of a quantum phase transition, or its mere existence, can be a decisive factor for the efficiency of QA in its adiabatic realization, because the time complexity grows exponentially for a first-order transition but is polynomial at a second-order transition or for the case of no transition. \( ^{2} \)  The situation is considerably more complicated at finite temperature in an open system, where the quantum adiabatic theorem involves the gap of the Liouvillian rather than the Hamiltonian  \( [15, 16] \) . Nevertheless, similar scaling considerations apply  \( [17] \) .

While the phase-transition perspective is certainly not sufficient for a complete understanding of the scaling of QA-based algorithms, since there does not exist a strict relation between the static properties in the thermodynamic limit and the dynamic properties at finite system size, it is nevertheless an insightful heuristic amenable to an analytical treatment that allows one to anticipate the finite-size scaling behavior, and we adopt it here for this reason, in line with a recent series of other studies, e.g., Refs. [18–22]. \( ^{3} \)  In the same vein, efforts
 

have been invested to reduce the difficulty arising from a first-order transition by, for example, the increase of the order of the transition from first to second using nonstoquastic Hamiltonians  \( [25–28] \)  or by the reverse annealing protocol  \( [29] \) .

Recently, the protocol of inhomogeneous driving of the transverse field has been studied as a candidate to enhance the performance of QA. In this method, one changes the amplitude of quantum fluctuations site by site individually. \( ^{4} \)  For example, the one-dimensional ferromagnetic Ising model with weak disorder was studied in Refs. [30, 31], where the residual energy was found to be smaller than in the homogeneous case. Similar improvements by inhomogeneous driving were reported in one-dimensional models in Refs. [32, 33]. Inhomogeneous field driving for the random 3-SAT problem has been shown to mitigate difficulties near the end of annealing processes by numerical computations in Ref. [34]. Avoidance of problematic anticrossings near the end of the anneal was also discussed analytically in Refs. [35, 36] and was tested on an experimental quantum annealer [37]. See also Refs. [38–40] for related studies.

Given these circumstances, several of the present authors solved the ferromagnetic p-spin model under inhomogeneous driving of the transverse field exactly \( ^{5} \)  and showed that first-order transitions can be removed if the inhomogeneity of the field is appropriately controlled [42]. However, the analysis in Ref. [42] is valid under idealized conditions such as the zero-temperature limit and complete turning off of the field at each site after a finite amount of time. Here we generalize this previous study and investigate what happens under more realistic conditions, including a nonzero temperature. We also compare the quantum system with its classical counterparts to clarify if and how quantum effects are essential in the present problem.

This paper is organized as follows. In Sec. II, we formulate the problem. In Sec. III, we examine the effects of inhomogeneous driving of the transverse field under idealized conditions. Section IV removes some of those conditions. In Sec. V, we consider two classical approaches, simulated annealing with site dependent temperature and the spin-vector Monte Carlo method. The final section is devoted to conclusions.

## II. FORMULATION

We write the Hamiltonian of QA as

 \[ \hat{H}(s)=s\hat{H}_{0}+\hat{V}, \quad (1) \] 

where  \( \hat{H}_{0} \)  is the target Hamiltonian, the ground state of which encodes the solution to a given combinatorial optimization problem,  \( \hat{V} \)  is the driver Hamiltonian used to induce quantum fluctuations, and s is a dimensionless parameter that controls the time dependence. We choose the p-spin model as the target Hamiltonian,

 \[ \hat{H}_{0}=-N\left(\frac{1}{N}\sum_{i=1}^{N}\hat{\sigma}_{i}^{z}\right)^{p}, \quad (2) \] 

where  \( p(\geq 3) \)  is an integer,  \( \hat{\sigma}_{i}^{z} \)  is the z component of the Pauli operator, N is the total number of spins, and i is the site (qubit) index running from 1 to N.

The ground state of  \( \hat{H}_{0} \)  is trivial,  \( \otimes_{i=1}^{N}|0\rangle_{i} \)  for odd p, where  \( |0\rangle_{i} \(  denotes the spin-up state, i.e.,  \) \hat{\sigma}_{i}^{z}\left|\hat{0}\right\rangle_{i}=\left|0\right\rangle_{i} \( . For even p, another state  \) \otimes_{i=1}^{N}|1\rangle_{i} \(  is also a ground state, where  \) \hat{\sigma}_{i}^{z}\left|1\right\rangle_{i}=-\left|1\right\rangle{}_{i} \( . This model reduces to the Grover problem [43] in the limit  \) p\to\infty \(  [19].

We choose the driver Hamiltonian in the following form:

 \[ \hat{V}=-\sum_{i=1}^{N}\Gamma_{i}\hat{\sigma}_{i}^{x}, \quad (3) \] 

where  \( \hat{\sigma}_{i}^{x} \)  is the x component of the Pauli operator. We assume  \( \Gamma_{i} \geq 0 \)  without loss of generality.

Let us briefly recall the situation under conventional QA, where the coefficient  \( \Gamma_{i} \)  satisfies  \( \Gamma_{t} = 1 - s \) , which is homogeneous in i. In this case the ground state of the driver Hamiltonian is trivial,  \( \otimes_{i=1}^{N}(|0\rangle_{i} + |1\rangle_{i})/\sqrt{2} \) . As time evolves, s increases from 0 to 1, and the Hamiltonian (1) changes from  \( \hat{V} \)  at s = 0 to  \( \hat{H}_{0} \)  at s = 1. Under this homogeneous transverse field, it is known that QA for the p-spin model has a first-order phase transition for  \( p \geq 3 \)  [19]. This would appear to be a disturbing failure of QA, since the optimization problem is trivial but is difficult for QA, although classical simulated annealing also fails due to a first-order thermal phase transition. However, it is possible to change this first-order transition to second order by the introduction of antiferromagnetic transverse interactions, which makes the Hamiltonian nonstoquastic [25–27]. It is also possible to remove the transition by reverse annealing [29].

An alternative way to circumvent the difficulties of first-order transitions is via spatiotemporal inhomogeneity of the transverse field [42]:

 \[ \Gamma_{i}=\begin{cases}1&for 0\leq i/N\leq1-\tau,\\N(1-\tau)+(1-i)&for 1-\tau<i/N<1-\tau+1/N,\\0&for 1-\tau+1/ N\leq i/N\leq1.\end{cases} \quad (4) \] 

Here,  \( \tau \)  is another dimensionless time-dependent parameter varying from 0 to 1, used to control the number of spins under the influence of the transverse field. This describes a step function with a diagonal drop. In the limit  \( N \gg 1 \) , the drop becomes vertical [the range of i in the middle line on the right-hand side of Eq. (4) becomes negligible] and the following form is asymptotically correct:

 \[ \Gamma_{i}=\begin{cases}1&for 0\leq i/N\leq1-\tau,\\0&for 1-\tau<i/N\leq1.\end{cases} \quad (5) \]
 

In this limit the driver Hamiltonian  \( \hat{V} \)  with the above  \( \Gamma_{i} \)  reduces to the simple form

 \[ \hat{V}=-\sum_{i=1}^{N(1-\tau)}\hat{\sigma}_{i}^{x}, \quad (6) \] 

which describes a “zipper-closing”-like schedule for the transverse field, starting from the last site.

## III. IDEALIZED CASE

We first recapitulate the idealized case with the transverse field applied only to a part of the system as in Eq. (6) at zero temperature as studied in Ref. [42]. We can derive an explicit form of the free energy for the Hamiltonian (1) with the p-spin model (2) and the general driver Hamiltonian (3) by the standard method of the Suzuki-Trotter decomposition in combination with the static approximation. We delegate the details to Appendix A and just write the results for the free energy per spin and the self-consistent equation for the magnetization at finite temperature  \( T(=1/\beta) \) :

 \[ \begin{aligned}f(m)=&s(p-1)m^{p}\\&-\frac{1}{\beta}\int_{0}^{1}dx\ln2\cosh\beta\sqrt{(spm^{p-1})^{2}+\Gamma(x)^{2}},\\m=&\int_{0}^{1}dx\frac{spm^{p-1}}{\sqrt{(spm^{p- 1})^{2}+\Gamma(x)}}\\&\times\tanh\beta\sqrt{(spm^{p-1})^{2}+\Gamma(x)},\end{aligned} \quad (7a) \quad (7b) \] 

respectively, where x is the normalized site index i/N in the continuous (large-N) limit. In the zero-temperature limit, these equations reduce to

 \[ f(m)=s(p-1)m^{p}-\int_{0}^{1}d x\sqrt{(s p m^{p-1})^{2}+\Gamma(x)^{2}}, \quad (8a) \] 

 \[ m=\int_{0}^{1}d x\frac{s p m^{p-1}}{\sqrt{(s p m^{p-2})^{2}+\Gamma(x)}}. \quad (8b) \] 

Substituting the continuum limit of Eq. (5) into the free energy (8a), we reproduce Eq. (1) of Ref. [42],

 \[ \begin{aligned}f(m)=&s(p-1)m^{p}-(1-\tau)\sqrt{(spm^{p-1})^{2}+1}\\&-\tau(spm^{p-1}).\end{aligned} \quad (9) \] 

We can draw the phase diagram from these equations as in Fig. 1. The process of annealing starts at  \( s = \tau = 0 \)  and terminates at  \( s =  \tau = 1 \) . It is seen that we can choose a path that avoids phase transitions between the starting and the ending points. This is to be contrasted with the case of a homogeneous transverse field, corresponding to the  \( \tau = 0 \)  axis, in which there is no way to avoid a first-order transition.

Another quantity that it would be instructive to look at is the entanglement entropy, which also exhibits the characteristic behavior of phase transitions (or their absence) depending on

![](./images/867752493235307364_1.jpg)

FIG. 1. Phase diagram on the s- \( \tau \)  plane for the idealized case at zero temperature. Each color denotes a line of first-order transitions for a given p, which is chosen to be 3, 4, and 5.

the path connecting the starting and end points, as described in Appendix B.

We can evaluate the energy gap  \( \Delta \)  in the limit of large system size  \( N \rightarrow \infty \)  by the standard semiclassical method [26, 44] as explained in some detail in Appendix B. The result is

 \[ \Delta=\min(\Delta_{a_{1}},\Delta_{b}) \quad (10a) \] 

 \[ \Delta_{a_{1}}=\delta\sqrt{1-\epsilon^{2}},\Delta_{b}=2sp\{\tau+(1-\tau)\cos\theta_{0}\}^{p-1}, \quad (10b) \] 

where

 \[ \theta_{0}=\arg\min_{\theta}\left\{-s[\tau+(1-\tau)\cos\theta]^{p}-(1-\tau)\sin\theta\right\} \quad (11a) \] 

 \[ \epsilon=-\frac{2\gamma}{\delta}, \quad (11b) \] 

 \[ \gamma=-\frac{1}{2}sp(p-1)(1-\tau)\sin^{2}\theta_{0}\{\tau+(1-\tau)\cos\theta_{0}\}^{p-2}, \quad (11c) \] 

 \[ \delta=\Delta_{b}\cos\theta_{0}+2\sin\theta_{0}+2\gamma. \quad (11d) \] 

Figures 2(a) and 2(b) show the two energy gap candidates,  \( \Delta_{a_{1}} \)  and  \( \Delta_{b} \) , for p = 3 along the paths  \( \tau = s \) , which avoids phase transitions, and  \( \tau = \frac{s^{2.366}}{3} \) , which just touches the critical point where the first-order line terminates (the paths are illustrated in Fig. 9 in Appendix B). The smaller of these two candidates is the true energy gap as shown in Appendix B. In Fig. 2(a),  \( \Delta_{b} \)  is seen to be the smaller one and is a monotonically increasing function of s. On the other hand, in Fig. 2(b), the energy gap  \( \Delta_{a_{1}} \)  is seen to vanish at the critical point  \( s_{c} \approx 0.52 \) , as expected. To check these thermodynamic limit predictions, we calculated the energy gap for finite-size systems by direct numerical diagonalization along the  \( \tau = s \)  path. The result is plotted in Fig. 2(c), which is compatible with the asymptotic behavior in the limit  \( N \to \infty \)  as observed in  \( \Delta_{b} \)  of Fig. 2(a). It is seen in Fig. 2(c) that the energy gap takes its minimum value when the transverse field is turned off at the first site as indicated by the arrows, which implies that the minimum of the gap is located at s = 0 in the  \( N \to \infty \)  limit.

It is interesting and important to check the behavior of the minimum energy gap as a function of the system size. As seen
 
![](./images/867752493235307364_2.jpg)

(a)

![](./images/867752493235307364_3.jpg)

(b)

![](./images/867752493235307364_4.jpg)

(c)

FIG. 2. Two types of energy gap  \( \Delta_{a1} \)  and  \( \Delta_{b} \)  for p = 3 as functions s for (a)  \( \tau = s \)  (away from the transition line) and (b)  \( \tau = s^{2.366} \)  (just touching the critical point). The smaller of these two is the final energy gap. (c) The energy gap for finite-size systems with  \( \tau = s \)  obtained by direct numerical diagonalization. The location of the minimum is indicated by an arrow for each N.

![](./images/867752493235307364_5.jpg)

(a)

![](./images/867752493235307364_6.jpg)

(b)

![](./images/867752493235307364_7.jpg)

(c)

FIG. 3. (a) The dashed lines show the schedule of  \( \tau \)  expressed by Eq. (12) in the phase diagram. The black sold line represents first-order phase transitions. (b) The minimal value of the energy gap against N in a log-log scale as calculated by numerical diagonalization. (c) The energy gap for N = 70 in two cases a = 0.7 and 0.8 of Eq. (12). The inset shows the behavior around the phase transition point. All results shown are for p = 3.

in Figs. 2(a) and 2(c), the minimum of the energy gap exists near the origin  \( \tau = s = 0 \)  when there is no transition along the annealing path  \( (\tau = s) \) , whereas the minimum is at the critical point when such a transition exists along the path [Fig. 2(b)]. We have chosen a series of paths as drawn in Fig. 3(a) to see the combined effects of the conventional path  \( (\tau = 0) \)  and the inhomogeneous driving protocol  \( (\tau > 0) \) . More explicitly,  \( \tau \)  follows the schedule

 \[ \tau=\left\{\begin{array}{ll}0&if s<a,\ $ s-a)/(1-a)&if s\geq a,\end{array}\right. \quad (12) \] 

with a control parameter a. The path  \( \tau = s \)  is reproduced with a = 0, and the path with a = 0.4 just touches the critical point at the end of the first-order line for p = 3. For a = 0.8, the path goes across the first-order transition point in the conventional homogeneous way ( \( \tau = 0 \) ) and, only after the transition is crossed, the inhomogeneity sets in. The minimal energy gap as a function of the system size, as shown in Fig. 3(b), is seen to decrease polynomially for a = 0 and 0.4. The case of a = 0.8 has an exponential decrease as expected from the existence of a first-order transition. The remaining a = 0.6 and 0.7 are marginal; a clear signal of an exponential decrease would show up only for larger system sizes than we studied here, N = 70. In other words, the energy gap stays relatively large until the system size becomes very large if we choose a path along the  \( \tau = 0 \)  axis (the conventional protocol) until just before a first-order phase transition is hit and then introduce the inhomogeneity. Figure 3(c) shows the s dependence of the gap for N = 70, the largest system size we studied.

## IV. NONIDEAL CASES

The problem we studied in the previous section concerns the ideal case of zero temperature and a complete turning off of the transverse field at each site. In this section we relax some of these restrictions in order to see what happens under nonideal circumstances.
 
![](./images/867752493235307364_8.jpg)

(a)

![](./images/867752493235307364_9.jpg)

(b)

![](./images/867752493235307364_10.jpg)

(c)

![](./images/867752493235307364_11.jpg)

(d)

![](./images/867752493235307364_12.jpg)

(e)

![](./images/867752493235307364_13.jpg)

(f)

FIG. 4. Two nonideal cases: (a)–(c) finite temperature and (d)–(f) incomplete turn-off. (a) Illustrative behavior of the free energy  \( f(m) \)  and the jump  \( \Delta m \)  in the order parameter at a first-order phase transition. (b) Finite-temperature phase diagram for p = 3. All curves represent first-order phase transitions. The red circle and blue square correspond to the respective points in panel (c). (c) Jump in magnetization along the line of first-order transitions depicted in panel (b). Symbols in red circle and blue square represent the respective points in the phase diagram of panel (b). (d) Amplitude of the transverse field  \( \Gamma_{i} \)  of Eq. (13). (e) Phase diagram for p = 3. The curves represent first-order phase transitions. (f) Jump in magnetization  \( \Delta m \)  along the first-order transition line. We note that (e) and (f) are remarkably similar to (b) and (c), though we do not presently have an explanation for this fact.

## A. Phase transition at finite temperature

It is straightforward to draw the phase diagram at finite (but low) temperature from the free energy and the self-consistent equation, Eqs. (7a) and (7b). The result is depicted in Fig. 4(b) with the annealing schedule of Eq. (5) kept intact.

As seen in the case of T = 0.01, a new line of first-order transitions appears at low but finite temperature in addition to the line that already exists at T = 0. This new line of first-order transitions merges with the existing line at T = 0 as the temperature rises, as observed in the cases of T = 0.1 and 1.

To understand what happens at this new transition line, it is useful to fix  \( \tau \)  at a low but finite value and consider the system behavior as s is increased. For small s, the influence of the ferromagnetic interactions in the cost function  \( \hat{H}_{0} \)  is weak and the system is disordered (magnetization m = 0) due to thermal fluctuations at finite temperature. As s increases, the system is driven into the ferromagnetic phase (m > 0), which is heralded by the new first-order transition appearing in the finite-temperature phase diagram. For small  \( \tau \) , the other first-order transition that already existed at T = 0 causes a jump in magnetization from a small value to a larger value. If we reduce the temperature from a small but finite value toward zero, the location of this first-order transition comes closer to the s = 0 axis until it merges with the s = 0axis in the zero-temperature limit. In other words, at T = 0, the system becomes ordered (m > 0) as soon as a finite value of s is introduced, as long as  \( \tau > 0 \) .

The structure of the phase diagram makes it impossible to avoid a first-order transition at finite temperature when one starts from the origin  \( s = \tau = 0 \)  and proceeds toward the goal at  \( s = \tau = 1 \) . Nevertheless, the inhomogeneous driving protocol leads to quantitative improvements, if not qualitative, over its homogeneous counterpart. To see this, we calculate the jump in magnetization  \( \Delta m \)  along the line of first-order transitions. The jump represents the width of a free energy barrier at a first-order transition as illustrated in Fig. 4(a). Thus, a decrease of the jump  \( \Delta m \)  enhances the quantum tunneling rate through the free energy barrier quantitatively through the exponential dependence of the tunneling rate on the system.
 

size is unchanged. \( ^{6} \) 

Figure 4(c) shows the result. The red circle denotes the value of the jump at the point marked by the same red circle in the phase diagram of Fig. 4(b), as a representative example of the system behavior under inhomogeneous field. The same is true for the blue square in Figs. 4(c) and 4(b), this being for the conventional homogeneous annealing case. In general, any point on the purple curve T = 0.01 in Fig. 4(c) shows  \( \Delta m \)  at the corresponding first-order transition point on the purple curve (T = 0.01) in Fig. 4(b). It is clearly seen that the jump is reduced at T = 0.01 and 0.1 for most values of s in comparison with the homogeneous case marked by the blue square. We may therefore conclude that inhomogeneous driving is advantageous to standard homogenous driving in that it enhances the tunneling rate even when a first-order transition is unavoidable, as in the present nonideal (finite temperature) situation.

## B. Different types of inhomogeneity

Let us next consider the case with a nonvanishing final value of the transverse field, at T = 0. We expect this prescription to induce a similar behavior to the finite-temperature case as the nonvanishing transverse field may disorder the system after the field is turned off incompletely.

 \[ \Gamma_{i}\left(\tau;a\right)=\begin{cases}0&\\a\left(1-\tau\right)-\left(a-1\right)\frac{i}{N-1}&\\1&\end{cases} \] 

which is drawn in Fig. 5(a). The parameter a controls the slope that interpolates two values  \( \Gamma_{i}=0 \)  and 1. The limit  \( a\to1 \)  corresponds to the homogeneous field, whereas  \( a\to\infty \)  is the simple step function of Eq. (5).

The zero-temperature free energy is derived from Eqs. (8a) and (15) and reads

 \[ \begin{aligned}f(s,\tau;m)=&(p-1)sm^{p}+x_{1}\sqrt{(spm^{p-1})^{2}+1}\\&+G(\Gamma_{0})-G(\Gamma_{1})+(1-x_{0})spm^{p-1},\end{aligned} \quad (16) \] 

The formal definition of the transverse field is now

 \[ \Gamma_{i}=\begin{cases}1&for0\leq i/N\leq1-\tau,\\ \gamma&for1-\tau<i/N\leq1,\end{cases} \quad (13) \] 

where a small transverse field  \( (0 < \gamma < 1) \)  remains after an incomplete turn-off [Fig. 4(d)]. It is easy to show from Eq. (8a) that the free energy at zero temperature becomes

 \[ \begin{aligned}f(m)=&s(p-1)m^{p}-(1-\tau)\sqrt{(spm^{p-1})^{2}+1}\\&-\tau\sqrt{(spm^{p-1})^{2}+\gamma^{2}},\end{aligned} \quad (14) \] 

which is to be compared with Eq. (9). The phase diagram and the behavior of the order parameter can be derived from this free energy.

Figure 4(e) is the phase diagram and Fig. 4(f) is the jump in magnetization  \( \Delta m \)  along the transition line. The qualitative similarity to the finite temperature case depicted in Figs. 4(b) and 4(c) is striking. We conclude that quantum fluctuations induced by a small but finite  \( \gamma \)  indeed play a similar role as the temperature effects.

As the second example, we study the following function [30],

 \[ \begin{aligned}&for\tau>-\left(1-\frac{1}{a}\right)\frac{i}{N-1}+1\\&otherwise\\&for\tau<-\left(1-\frac{1}{a}\right)\frac{i}{N-1}+1-\frac{1}{a}\\ \end{aligned} \quad (15) \] 

where

 \[ x_{1}=\begin{cases}1-\frac{a}{a-1}&for\tau<1-\frac{1}{a},\\0&for1-\frac{1}{\alpha}\leq\tau,\end{cases} \quad (17) \] 

 \[ x_{0}=\begin{cases}1&for\tau<\frac{1}{a}\\ \frac{a}{a-1}(1-\tau)&for\frac{1}{a}\leq\tau,\end{cases} \quad (18) \] 

 \[ \Gamma_{1}=\begin{cases}1&for\tau<1-\frac{1}{a},\\a(1-\tau)&for1-\frac{1}{a}\leq\tau,\end{cases} \quad (19) \] 

 \[ \Gamma_{0}=\begin{cases}1-a\tau&for\tau<\frac{1}{a},\\0&for\frac{1}{a}\leq\tau,\end{cases} \quad (20) \] 

and

 \[ \begin{aligned}G(\Gamma)=&-\frac{1}{2(a-1)}\left\{\Gamma\sqrt{(spm^{p-1})^{2}+\Gamma^{2}}\right.\\&\left.+(spm^{p-1})^{2}\ln\left(\sqrt{(spm^{p-2})^{2}+\Gamma^{2}}+\Gamma\right)\right\}.\end{aligned} \quad (21) \] 

Figure 5(b) is the resulting phase diagram. It can be seen that
 
![](./images/867752493235307364_14.jpg)

(a)

![](./images/867752493235307364_15.jpg)

(b)

FIG. 5. (a) The field amplitude  \( \Gamma_{i}(\tau; a) \)  of Eq. (15). (b) Phase diagram for p = 3 for several values of a.

paths exist that avoid first-order transitions when the inhomogeneity is turned on, i.e., a > 1.

As mentioned earlier, Ref. [30] discusses inhomogeneous annealing for a weakly disordered ferromagnetic one-dimensional chain. It is not straightforward to compare our results with theirs, since this is a very different problem with its own characteristics such as a low cost of domain formation. Nevertheless, the conclusion common to both this work and Ref. [30] is that inhomogeneous driving is useful for reaching better solutions.

## C. Longitudinal random field

We next consider the case with random longitudinal fields:

 \[ \hat{H}_{0}=-N\left(\frac{1}{N}\sum_{i=1}^{N}\hat{\sigma}_{i}^{z}\right)^{p}-\sum_{i=1}^{N}h_{i}\hat{\sigma}_{i}^{z}, \quad (22) \] 

where each  \( h_{i} \)  is drawn from the bimodal or the Gaussian distribution:

 \[ P_{b}(h_{i})=\frac{1}{2}\left[\delta(h_{i}+h_{0})+\delta(h_{i}-h_{0})\right], \quad (23a) \] 

 \[ P_{g}(h_{i})=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-h_{i}/2\sigma^{2}}. \quad (23b) \] 

![](./images/867752493235307364_16.jpg)

(a)

![](./images/867752493235307364_17.jpg)

(b)

FIG. 6. (a) Phase diagram for bimodal random longitudinal fields with strengths  \( h_{0}=0.1 \) , 0.5, and 1. (b) Phase diagram for Gaussian random longitudinal fields with standard deviations  \( \sigma=0.1 \) , 0.5, and 1. All lines are for first-order phase transitions. All the data are for p=3.

It is noteworthy that the introduction of nonstoquasticity into the Hamiltonian of the p-spin model without random field removes a first-order phase transition for p > 3 [25, 26, 28] whereas the same idea fails if random longitudinal field exists [45]. Thus, this model with random field is a test bed to compare the performance of inhomogeneous driving and that of the nonstoquastic Hamiltonian.

The computation of the free energy proceeds as before, and the result for T = 0 is

 \[ f(m)=s(p-1)m^{p}-\left[\int_{0}^{1}d x\sqrt{(s p m^{p-1}+h)^{2}+\Gamma(x)^{2}}\right], \quad (24) \] 

where the brackets  \( [\cdots] \)  denote the average over the distribution of the random field variable denoted as h, and we have used the law of large numbers,

 \[ \lim_{N\to\infty}\frac{1}{N}\sum_{i=1}^{N}(\cdots)=[(\cdots)]. \quad (25) \] 

Figure 6 shows the phase diagram for the simple inhomogeneity of Eq. (4). Panels (a) and (b) are for the bimodal
 

and Gaussian distributions, respectively. In both cases we see that the inhomogeneous transverse field eliminates first-order phase transitions. This leads to the interesting conclusion that the present method of inhomogeneous driving of the transverse field is more powerful for the removal of first-order transitions than the introduction of non-stoquastic Hamiltonians, at least for the p-spin model under random longitudinal fields.

## V. COMPARISON WITH CLASSICAL MODELS

It is useful to compare the results of the previous sections with those of the classical counterparts of QA. Here we focus on two classical models: simulated annealing [9] and spin vector Monte Carlo (SVMC) [46].

## A. Simulated Annealing with an Inhomogeneous Temperature Schedule

A “limited quantum speedup” is a speedup of quantum annealing relative to its classical counterparts, such as simulated annealing [47]. Indeed, it was through this viewpoint that the concept of quantum annealing was proposed in Ref. [1]. We therefore study the classical Ising model with an inhomogeneous driving parameter, i.e., the (inverse) temperature in simulated annealing. We consider the p-spin model under random local fields:

 \[ H=-N\left\{\frac{1}{N}\sum_{i=1}^{N}\beta_{i}\sigma_{i}\right\}^{p}-\sum_{i=1}^{N}\beta_{i}h_{i}\sigma_{i}, \quad (26) \] 

where  \( \sigma_{i}(=\pm1) \)  is a simple classical Ising variable and  \( \beta_{i} \)  is the inhomogeneous (site-dependent) inverse temperature. It is to be noted that we take the above Hamiltonian to be dimensionless, corresponding to the product  \( \beta H \) , where  \( \beta \)  is the (homogeneous) inverse temperature. The site-dependent temperature  \( T_{i}=1/\beta_{i} \)  is also dimensionless. The random field  \( h_{i} \)  follows the bimodal or the Gaussian distribution.

The partition function can be calculated as

 \[ \begin{aligned}Z=&Tr e^{-H}\\=&Tr\int dm\delta\left(Nm-\sum_{i=1}^{N}\beta_{i}\sigma_{i}\right)e^{N m^{p}+\sum_{i=1}^{N}\beta_{i}h_{i}\sigma_{i}}\\=&Tr\int dm d\tilde{m}e^{-\tilde{m}(Nm-\sum_{i=1}^{N}\beta_{i}\sigma_{i})+Nm^{p}+\sum_{i=1}^{N}\beta_{i}h_{i}\sigma_{i}}\\=&\int dm d\tilde{m}e^{-Nm\tilde{m}+Nm^{p}+\sum_{i=1}^{N}\ln2\cosh\beta(\tilde{m}+h_{i})}.\end{aligned} \quad (27) \] 

The saddle-point condition with respect to m is  \( \tilde{m} = pm^{p-1} \) . Then the free energy per site is

 \[ f=(p-1)m^{p}-\frac{1}{N}\sum_{i=1}^{N}\ln2\cosh\beta_{i}(p m^{p-1}+h_{i}). \quad (28) \] 

Under the inhomogeneous protocol we decrease the local temperature or increase the inverse temperature  \( \beta_{i} \)  sitewise. Suppose that  \( \beta_{l}=0 \)  for  \( i=1,2,\cdots,N(1-\tau) \)  and  \( \beta_{l}=\beta_{0} \)  for

![](./images/867752493235307364_18.jpg)

![](./images/867752493235307364_19.jpg)

FIG. 7. Behavior of the order parameter in simulated annealing with inhomogeneous temperature driving. We choose \(p = 3\) and \(\beta_{0} = 2\) and the bimodal distribution of random local fields.

 \( i = N(1 - \tau) + 1, \cdots, N \) . In other words, the local temperature  \( T_{i} = 1/\beta_{i} \)  has been decreased from  \( \infty \)  to  \( 1/\beta_{0} \)  for  \( N\tau \)  spins and is kept  \( \infty \)  for the remaining  \( N(1 - \tau) \)  spins. Thus, as we increase  \( \tau \)  from 0 to 1, the fraction of sites with low temperature increases. Under this prescription, the free energy per spin becomes

 \[ f=(p-1)m^{p}-\tau\left[\ln2\cosh\beta_{0}(p m^{p-1}+h_{i})\right]+\mathrm{c o n s t.} \quad (29) \] 

Figure 7 shows the order parameter  \( m = (1/N) \sum_{i=1}^{N} \beta_{i} \sigma_{i} \)  evaluated from the free energy. Here the amplitude of the bimodal distribution of random fields is chosen as (a)  \( h_{0} = 0.5 \)  and (b)  \( h_{0} = 1 \) . This figure shows that the first-order phase transition does not disappear in simulated annealing under inhomogeneous temperature driving, since the order parameter has a discontinuity. We found essentially the same behavior for any combination of the parameters,  \( p (\geq 3) \) ,  \( \beta_{0} \) ,  \( h_{0} \) , and  \( \tau \) , as long as  \( \beta_{0} \)  or  \( h_{0} \)  is not too large, in which cases the final state belongs to the same paramagnetic phase as the initial one, and therefore no phase transition can ever happen. The same holds for the Gaussian distribution of random fields. We therefore conclude that inhomogeneous temperature driving of simulated annealing is incapable of removing a first-order transition (at least for the p-spin model), in contrast to the corresponding quantum case.

## B. Spin vector Monte Carlo

In this section we consider the spin vector Monte Carlo (SVMC) algorithm, in which one replaces  \( \hat{\sigma}_{i}^{x} \)  and  \( \hat{\bar{\sigma}}_{i}^{z} \)  by  \( \sin\theta_{i} \)  and  \( \cos\theta_{i} \) , respectively, and applies Metropolis moves to update the angles. This algorithm was developed as a classical model for the D-Wave processors [46], and has been the subject of scrutiny in this context [48–52]. It can be derived as the semiclassical limit of the spin-coherent states path integral, so that it can be understood as a mean-field approximation of the simulated quantum annealing (SQA) algorithm [48, 53]. We therefore anticipate that it will be a close approximation to our mean-field solution of the p-spin model as well.

In the context of the p-spin model with an inhomogeneous transverse field, the Hamiltonian is rewritten in the SVMC
 

model as

 \[ H(s)=-s N\left(\frac{1}{N}\sum_{i=1}^{N}\cos\theta_{i}\right)^{P}-\sum_{i=1}^{N}\Gamma_{i}\sin\theta_{i}. \quad (30) \] 

The partition function is calculated as

 \[ \begin{aligned}Z=&\mathrm{Tr}e^{-\beta H(s)}\\=&\mathrm{Tr}\int dm\delta\left(Nm-\sum_{i=1}^{N}\cos\theta_{i}\right)e^{\beta\left(NNm^{p}+\sum_{i=1}^{N}\Gamma_{i}\sin\theta_{i}\right)}\\=&\mathrm{Tr}\int dm\int d\tilde{m}e^{i(Nm-\sum_{i=1}^{N}\cos\theta_{i})\tilde{m}+\beta(sNm^{p}+\sum_{i=1}^{N}\Gamma_{i}\sin\theta_{i})}.\end{aligned} \quad (31) \] 

The saddle-point condition for m is  \( i\tilde{m} + \beta spm^{p-1} = 0 \) . The trace over the angles is straightforwardly evaluated as

 \[ \begin{aligned}&\mathrm{Tr}\exp\left[-i m\sum_{i=1}^{N}\cos\theta_{i}+\beta\sum_{i=1}^N\Gamma_{i}\sin\theta_{i}\right]\\&=\prod_{i=1}^{N}\int_{0}^{2\pi}d\theta_{i}\exp\left[\beta spm^{p-1}\cos\theta_{i}+\beta\Gamma_{i}\sin\theta_{i}\right]\\&=\prod_{i=1}^{N}2\pi I_{0}\left(\beta\sqrt{(spm^{p-1})^{2}+\Gamma_{i}^{2}}\right),\\ \end{aligned} \quad (32) \] 

where  \( I_{n}(x) \)  is the modified Bessel function of the first kind. Then we have:

 \[ \begin{aligned}Z&=\int dm\exp\Bigg[-\beta(p-1)s N m^{p}\\&\quad+\sum_{i=1}^{N}\ln\left(2\pi I_{0}\left(\beta\sqrt{(s p m^{p-1})^{2}+\Gamma_{i}^{2}}\right)\right)\Bigg].\end{aligned} \quad (33) \] 

Thus the free energy per spin is

 \[ \begin{aligned}f=&s(p-1)m^{p}\\&-\frac{1}{\beta}N\sum_{i=1}^{N}\ln\left(2\pi I_{0}\left(\beta\sqrt{(s p m^{p-1})^{2}+\Gamma_{i}^{2}}\right)\right)\\=&s(p-1)m^{p}\\&-\frac{1}{\beta}\int_{0}^{1}dx\ln\left(2\pi I_{0}\left(\beta\sqrt{(s p m^{p-1})^{2}+\Gamma(x)^{2}}\right)\right),\end{aligned} \quad (34) \] 

where we replaced \(i/N\) by a continuous variable \(x\) for large \(N\). In the zero-temperature limit \(\beta \to \infty\), this free energy reduces to

 \[ f=s(p-1)m^{p}-\int_{0}^{1}d x\sqrt{(s p m^{p-1})^{2}+\Gamma(x)^{2}}, \quad (35) \] 

which coincides with the free energy (8a) for the quantum model. The finite-temperature phase diagram as depicted in Fig. 8 has qualitatively the same structure as the quantum counterpart, Fig. 4(b), when the temperature is low. Therefore, as long as static properties in the large-N and low-temperature limits are concerned, the SVMC model faithfully describes the behavior of the quantum system.

![](./images/867752493235307364_20.jpg)

FIG. 8. Phase diagram for p = 3 for the SVMC model.

## VI. CONCLUSIONS

We have solved the ferromagnetic p-spin model with and without random longitudinal field under inhomogeneous driving of the transverse field. The zero-temperature phase diagram for the case of ideal control of the transverse field, i.e., complete turning off of the field at each site, showed that the first-order transition that exists under homogeneous driving can be circumvented by inhomogeneous driving. Under non-ideal circumstances, with a nonzero temperature or a nonzero value of the final transverse field, a new line of first-order transitions appears, which prevents us from avoiding a first-order transition. However, the new first-order transitions are weaker than the original one in the sense that the width of the free-energy barrier between local minima is smaller than in the original homogeneous case, which leads to an increase in the quantum tunneling rate. We therefore conclude that inhomogeneous driving of the transverse field has the potential to be at least quantitatively beneficial for a performance enhancement of quantum annealing.

It is not easy to understand why inhomogeneous driving mitigates the difficulties of first-order transitions. A phase transition is a phenomenon involving a large number of microscopic degrees of freedom simultaneously and cooperatively, resulting in a diverging correlation length in the case of a second-order transition. The introduction of a spatiotemporal inhomogeneity of the driving field significantly reduces the number of microscopic degrees of freedom that are involved in the process of modification of the system properties at a given time, concurrently reducing the correlation length and modifying critical exponents, which may lead to the disappearance of transition as observed here. A theory based on a suppression of topological defects (Kibble-Zurek mechanism [54]) via inhomogeneous driving in interacting spin systems that can be mapped onto a free fermionic system has been proposed in Ref. [31]. Our mean-field approach complements this theory and leads to similar conclusions about the benefits of inhomogeneous driving.

Related is the problem of practical inhomogeneous driving protocols, e.g., the order in which spins are to be chosen to have the transverse field turned off. In our mean-field-like model, all spins are equivalent in the cost function, and there
 

is no specific way to choose a particular spin as the next target. Even spin i = N, which has its transverse field turned off immediately after the annealing process starts, points in the right direction thanks to the weak but non-negligible effective field from other spins,  \( -s(\sum_{i=1}^{N-1}\hat{\sigma}_{i}^{z})^{p-1}/N \) . This mechanism clearly comes from the uniform mean-field characteristics of the present problem and is not straightforward to generalize. The situation is nontrivial in general problems. Empirical protocols have been devised and tested on a physical quantum annealing device [37, 40]. Systematic theoretical guidelines remain to be established.

In practice, quantum annealing operates away from the adiabatic limit and is a dynamical process, and thus the static analysis in the present paper needs careful scrutiny before its conclusions are applied to practical situations. For example, though the static phase diagram is shared by the quantum model and the classical SVMC model in the ideal situation of zero temperature and complete turning off of the transverse field, the dynamical properties are expected to be quite different since quantum dynamics for large but finite-size systems allows tunneling through an energy barrier whereas there is no such mechanism classically at T = 0. Nevertheless, dynamics is notoriously difficult to analyze since we should, in principle, solve the time-dependent Schrödinger equation directly, which is in general out of reach beyond small to moderate sizes. It is encouraging in this respect that the static properties of the p-spin model are very much in accordance with the dynamical behavior in the case of reverse annealing. \( ^{7} \)  Further investigations of dynamics will shed more light on the relevance of the static analysis to physical quantum annealing, and are highly desired.

## ACKNOWLEDGMENTS

This work was partially funded by JSPS KAKENHI Grant No. 26287086. The research is based upon work partially supported by the Office of the Director of National Intelligence (ODNI), Intelligence Advanced Research Projects Activity (IARPA), via U.S. Army Research Office Contract No. W911NF-17-C-0050. The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies or endorsements, either expressed or implied, of the ODNI, IARPA, or the U.S. Government. The U.S. Government is authorized to reproduce and distribute reprints for Governmental purposes notwithstanding any copyright annotation thereon.

## Appendix A: Derivation of the free energy

In this appendix we derive the free energy Eq. (8a) for the Hamiltonian in Eqs. (1)–(3), following the standard procedure [19, 25].

Using the Suzuki-Trotter decomposition, we can write the partition function as

 \[ Z=\lim_{M\rightarrow\infty}Z_{M}=\lim_{M\rightarrow\infty}\mathrm{T r}\left(e^{-\left(\beta/M\right)s\hat{H}_{0}}e^{-\left(\beta/M\middle)\hat{V}\right)}\right)^{M}=\lim_{M\rightarrow\infty}\mathrm{T r}\left\{\exp\left[\frac{\beta s N}{M}\left(\frac{1}{N}\sum_{i=1}^{N}\hat{\sigma}_{i}^{z}\right)^{p}\right]\exp\left[\frac{\beta}{M}\sum_{i=1}^{N}\Gamma_{i}\hat{\sigma}_{i}^{x}\right]\right\}^{M}, \quad (A1) \] 

where  \( \beta \)  is the inverse temperature. For M replicas, we insert the closure relation

 \[ \hat{\mathrm{I}}(\alpha)=\sum_{\{\sigma_{i}^{z}(\alpha)\}}\left|\{\sigma_{i}^{x}(\alpha)\}\right\rangle\left\langle\{\sigma_{i}^{z}(\alpha)\}\right|\sum_{\{\sigma_{i}^{x}(\alpha)\}}\left|\{\sigma_{i}^{y}(\alpha)\}\right\rangle\left\langle\{\sigma_{i}^{x}(\alpha)\}\right|\quad(\alpha=1,2,\cdots,M), \quad (A2) \] 

and obtain

 \[ Z_{M}=\sum_{\{\sigma_{i}^{z}(\alpha)\}}\sum_{\{\sigma_{j}^{x}(\alpha)\}}\prod_{\alpha=1}^{M}\exp\left[\frac{\beta s N}{M}\left(\frac{1}{N}\sum_{i=1}^{N}\sigma_{i}^{z}(\alpha)\right)^{p}\right]\exp\left[\frac{\beta}{M}\sum_{i=1}^{N}\Gamma_{i}\sigma_{i}^{x}(\alpha)\right]\prod_{i=1}^{N}\left\langle\sigma_{i}^{x}(\alpha)\middle|\sigma_{i}^{x}(\omega)\middle|\sigma_{j}^{z}(\alpha+1)\right\rangle. \quad (A3) \] 

Periodic boundary conditions are imposed by the trace operation,  \( \left|\sigma_{i}^{x}(1)\right\rangle = \left|\sigma_{j}^{x}(M+1)\right\rangle \) .

To facilitate the calculations, we use the following relation

 \[ \delta\left(N m(\alpha)-\sum_{i=1}^{N}\sigma_{i}^{z}(\alpha)\right)=\int d\tilde{m}(\alpha)\exp\left[-\tilde{m}(\alpha)\left(N m(\alpha)-\sum_{i=1}^{N}\sigma_{i}^{z}(\alpha)\right)\right] \quad (A4) \]
 

and express the partition function as

 \[ \begin{align*}Z_{M}&=\sum_{\{\sigma_{i}^{z}(\alpha)\}}\sum_{\{\sigma_{t}^{z}(\alpha)\}} \prod_{\alpha=1}^{M}\int dm(\alpha)d\tilde{m}(\alpha)\exp\left[N\left(\frac{\beta s}{M}m(\alpha)^{p}-\tilde{m}(\alpha)m(\alpha)\right)\right]\\&\quad\times\exp\left[\sum_{i=1}^{N}\left(\tilde{m}(\alpha)\sigma_{i}^{z}(\alpha)+\frac{\beta}{M}\Gamma_{i}\sigma_{i}^{x}(\alpha)\right)\right]\prod_{i=1}^{N}\left\langle\sigma_{i}^{z}(\alpha)|\sigma_{i}^{x}(\alpha)\right\rangle\left\langle\sigma_{i}^{x}(\α)|\sigma_{i}^{z}(\alpha+1)\right\rangle\\&=\int\prod_{\alpha=1}^{M}dm(\alpha)d\tilde{m}(\alpha)\exp\left[N\sum_{\alpha=1}^{M}\left(\frac{\beta s}{M}m(\alpha)^{p}-\tilde{m}(\alpha)m(\alpha)\right)\right]\exp\left[\sum_{i=1}^{N}\ln\mathrm{Tr}\prod_{\alpha=1}^{M}\exp\left(\tilde{m}(\alpha)\hat{\sigma}^{z}\right)\exp\left(\frac{\beta}{M}\Gamma_{i}\hat{\sigma}^{x}\right)\right]\\&=\int\prod_{\alpha=1}^{M}dm(\alpha)d\tilde{m}(\alpha)\exp\left[-N\beta f_{N,M}\right].\end{align*} \quad (A5) \] 

For  \( N \gg 1 \) , the saddle-point condition for  \( \tilde{m}(\alpha) \)  reads

 \[ \tilde{m}(\alpha)=\frac{\beta s p}{M}m(\alpha)^{p-1}. \quad (A6) \] 

Then, the free energy becomes

 \[ f_{N,M}(\{m(\alpha)\})=s(p-1)\frac{1}{M}\sum_{\alpha=1}^{M}m(\alpha)^{p}-\frac{1}{\beta N}\sum_{i=1}^{N}\ln\mathrm{Tr}\prod_{\alpha=1}^{M}\exp\left(\frac{\beta s p}{M}m(\alpha)^{p-1}\hat{\sigma}^{z}\right)\exp\left(\frac{\beta}{M}\Gamma_{i}\hat{\sigma}^{x}\right), \quad (A7) \] 

We now use the static approximation  \(  m = m(\alpha)  \)  for all  \( \alpha \) . Taking the trace by the reverse operation of the Suzuki-Trotter decomposition for  \( M \to \infty \) , we obtain

 \[ f(m)=s(p-1)m^{p}-\frac{1}{\beta N}\sum_{i=1}^{N}\ln2\cosh\beta\sqrt{(s p m^{p-1})^{2}+\Gamma_{i}^{2}}. \quad (A8) \] 

The extremization condition of  \( f(m) \)  leads to

 \[ m=\frac{1}{N}\sum_{i=1}^{N}\frac{s p m^{p-1}}{\sqrt{(s p m^{p- 1})^{2}+\Gamma_{i}^{2}}}\tanh\beta\sqrt{(s p m^{p-1})^{2}+\Gamma_{i}^{2}}. \quad (A9) \] 

For  \( N \gg 1 \) , we rewrite  \( \Gamma_{i} \)  with discrete valuable i in terms of  \( \Gamma(x) \)  with a continuous valuable  \( x \sim i/N \) . Then the free energy and self-consistent equation reduce to

 \[ f(m)=s(p-1)m^{p}-\int_{0}^{1}dx\ln2\cosh\beta\sqrt{(s p m^{p-1})^{2}+\Gamma(x)^{2}}, \quad (A10) \] 

 \[ m=\int_{0}^{1}dx\frac{s p m^{p-1}}{\sqrt{(s p m^{p-12})+\Gamma(x)^{2}}}\tanh\beta\sqrt{(s p m^{p-1})^{2}+\Gamma(x)^{2}}. \quad (A11) \] 

Appendix B: Semiclassical computations of the energy gap and the entanglement entropy

We calculate in this appendix the energy gap in the limit  \( N \to \infty \)  as quoted in Sec. III and the entanglement entropy by the semiclassical method [26, 44]. The methods we employ are semiclassical since a large spin (for large N) behaves classically.

We divide the system into two subsystems A and B, the former with  \( i = 1, \cdots, N(1 - \tau) \)  and the latter for the rest of the sites. Note that according to our convention the transverse field is turned on in subsystem A but is off in subsystem B. We further divide subsystem A into two subsystems,  \( A_{1} \)  with  \( i = 1, \cdots, Nu(1 - \tau) \) ,  \( A_{2} \)  with  \( i = Nu(1 - \tau) + 1, \cdots, N(1 - \tau \) , where u is a parameter between 0 and 1. Our goal is to compute the energy gap and the entanglement entropy between the two subsystems  \( A_{1} \)  and  \( A_{2} \)  in the limit of large N.

To do so, we introduce two macroscopic spin operators as

 \[ \hat{S}_{A_{1}}^{x,x}=\frac{1}{2}\sum_{i=1}^{N u(1-\tau)}\hat{\sigma}_{i}^{z,x}, \quad (B1) \] 

 \[ \hat{S}_{A_{2}}^{z,x}=\frac{1}{2}\sum_{i=N u(1-\tau)+1}^{N(1-\tau)}\hat{\sigma}_{i}^{z,x}, \quad (B2) \] 

 \[ \hat{S}_{A_{2}}^{z,x}=\frac{1}{2}\sum_{i=N(1-\tau)+1}^{N}\hat{\sigma}_{i}^{z,x}. \quad (B3) \] 

The Hamiltonian is then rewritten as

 \[ \hat{H}(s,\tau)=-s N\left\{\frac{2}{N}(\hat{S}_{A_{1}}^{z}+\hat{S}_{A_{2}}^{z}+\hat{S_{B}^{z}})\right\}-2(\hat{S}_{A_{1}}^{x}+\hat{S}_{A_{2}}^{x}). \quad (B4) \] 

Rotating the spin operators around the y axis by an angle \(\theta\) as

 \[ \left(\begin{array}{c}{\hat{S}_{A_{1,2}}^{x}}\\ {\hat{S}_{A_{2,1}}^{z}}\\ \end{array}\right)=\left(\begin{array}{c c}{\cos\theta}&{\sin\theta}\\ {-\sin\theta}&{\cos\theta}\\ \end{array}\right)\left(\begin{array}{c}{\hat{S}_{A_{1,2}}^{x}}\\ {\hat{S}_{A_{2,1}}^{z}}\\ \end{array}\right), \quad (B5) \]
 

we employ the Holstein-Primakoff transformation to treat quantum corrections to the classical limit as

 \[ \hat{S}_{A_{1,2}}^{z}=\frac{N_{1,2}}{2}-\hat{a}_{1,2}^{\dagger}\hat{a}_{1, 2}, \quad (B6) \] 

 \[ \hat{S}_{A_{1,2}}^{+}=(N_{1,2}-\hat{a}_{1,2}^{\dagger}\hat{a}_{1, 2})^{1/2}\hat{a}_{1.2}=(\hat{S}_{A_{1,2}}^{-})^{\dagger}, \quad (B7) \] 

 \[ \hat{S}_{B}^{z}=\frac{N\tau}{2}-\hat{b}^{\dagger}\hat{b}, \quad (B8) \] 

 \[ \hat{S}_{B}^{+}=(N\tau-\hat{b}^{\dagger}\hat{b})^{1/2}\hat{b}=(\hat{S}_{B}^{-})^{\dagger}, \quad (B9) \] 

where  \( N_{1} = Nu(1 - \tau) \) ,  \( N_{2} = N(1 - u)(1 - \tau) \) , and  \( \hat{a}_{1} \) ,  \( \hat{a} \) , and  \( \hat{b} \)  are bosonic annihilation operators. Substituting these transformations into the Hamiltonian Eq. (B4) and expanding it to  \( \mathcal{O}(N^{0}) \)  (the semiclassical limit), the Hamiltonian becomes

 \[ \begin{aligned}\hat{H}(s,\tau)=&Ne+\gamma+\delta(\hat{a}_{1}^{\dagger}\hat{a}_{1}+\hat{a}_{2}^{\dagger}\hat{a_{2}})\\&+\gamma\left[u\{(\hat{a}_{1}^{\dagger})^{2}+(\hat{a}_{1})^{2}\}+(1-u)\{(\hat{a}_{2}^{\dagger})^{2}+(\hat{a}_{2})^{2}\}\right.\\&\left.+2\sqrt{u(1-u)}(\hat{a}_{1}^{\dagger}\hat{a}_{2}^{\dagger}+\hat{a}_{1}\hat{a}_{2})\right]\\&+\Delta_{b}\hat{b}^{\dagger}\hat{b},\end{aligned} \quad (B10) \] 

where

 \[ e=-s[\tau+(1-\tau)\cos\theta_{0}]^{p}-(1-\tau)\sin\theta_{0}, \quad (B11) \] 

 \[ \gamma=-\frac{1}{2}sp(p-1)(1-\tau)\sin^{2}\theta_{0}\{\tau+(1-\tau)\cos\theta_{0}\}^{p-2}, \quad (B12) \] 

 \[ \delta=\Delta_{b}\cos\theta_{0}+2\sin\theta_{0}+2\gamma, \quad (B13) \] 

 \[ \Delta_{b}=2sp\{\tau+(1-\tau)\cos\theta_{0}\}^{p-1} \quad (B14) \] 

with

 \[ \theta_{0}=\arg\min_{\theta}\left\{-s[\tau+(1-\tau)\cos\theta]^{p}-(1-\tau)\sin\theta\right\}. \quad (B15) \] 

To compute the energy gap and the entanglement entropy, we diagonalize the Hamiltonian using the Bogoliubov transformation as

 \[ \hat{a}_{1}=\sqrt{u}\left(\cosh\frac{\Theta}{2}\hat{a}_{1}^{\dagger}+\sinh\frac{\Theta}{4}\hat{a}_{1}^{{\dagger}}\right)+\sqrt{1-u}\hat{a}_{2}, \quad (B16) \] 

 \[ \hat{a}_{2}=\sqrt{1-u}\left\{\cosh\frac{\Theta}{2}\hat{a}_{1}+\sinh\frac{\Theta}{4}\hat{a}_{1}^{\dagger}\right\}-\sqrt{u}\hat{a}_{2}, \quad (B17) \] 

where

 \[ \tanh\Theta=-2\gamma/\delta=\epsilon, \quad (B18) \] 

and  \( \hat{a}_{1} \)  and  \( \hat{a} \)  are new bosonic annihilation operators. The diagonalized Hamiltonian is given as

 \[ \begin{aligned}\hat{H}(s,\tau)=&Ne+\gamma+\frac{\delta}{2}(\sqrt{1-\epsilon^{2}}-1)\\&+\Delta_{a_{1}}\hat{a}_{1}^{\dagger}\hat{a}_{1}+\Delta_{a_{2}}\hat{a}_{2}^{\dagger}\hat{a}_{2}+\Delta_{b}\hat{b}^{\dagger}\hat{b},\end{aligned} \quad (B19) \] 

where

![](./images/867752493235307364_21.jpg)

![](./images/867752493235307364_22.jpg)

![](./images/867752493235307364_23.jpg)

![](./images/867752493235307364_24.jpg)

FIG. 9. Left top panel is the phase diagram, where the solid line represents a line of first-order phase transitions, and three lines (a), (b), and (c) indicate paths with  \( \tau = s \) ,  \( s^{2.366} \)  and 0. Panels (a)–(c) show the entanglement entropy for the corresponding paths. In each case we set p = 3 and u = 1/2.

 \[ \Delta_{a_{1}}=\delta\sqrt{1-\epsilon^{2}}, \quad (B20) \] 

 \[ \Delta_{a_{2}}=\delta. \quad (B21) \] 

Since  \( \Delta_{a_{2}} \geq \Delta_{a_{1}} \) , the minimum energy gap is the smaller of  \( \Delta_{a_{1}} \)  and  \( \Delta_{b} \) , i.e.,

 \[ \Delta=\min(\Delta_{a_{1}},\Delta_{b}). \quad (B22) \] 

The entanglement entropy between subsystems  \( A_{1} \)  and  \( A_{2} \)  is defined as  \( \mathcal{E} = -\mathrm{Tr}_{A_{1}}(\hat{\rho}_{A_{1}}\ln\hat{\rho}_{A_{}1}) \) , where  \( \hat{\rho}_{A_{1}} = \mathrm{Tr}_{A_{2}}\hat{\rho}_{A} \)  is the density matrix of subsystem  \( A_{1} \)  and  \( \hat{\rho}_{A} \)  is the one for subsystem A. The technique for computing  \( \hat{\rho}_{A_{1}} \)  is detailed in Ref. [44]. Using this method, the density matrix of subsystem  \( A_{1} \)  is described as

 \[ \hat{\rho}_{A_{1}}=\frac{2}{\mu+1}\exp\left[-\ln\left(\frac{\mu+1}{\mu-1}\right)\hat{c}^{\dagger}\hat{c}\right], \quad (B23) \] 

where  \( \hat{c}^{\dagger} \)  and  \( \hat{c} \)  are bosonic creation and annihilation operators and

 \[ \mu=\sqrt{[(1-u)+u\alpha][(1-u)+u/\alpha]}, \quad (B24) \] 

 \[ \alpha=\sqrt{(1-\epsilon)/(1+\epsilon)}. \quad (B25) \] 

The entanglement entropy E then becomes

 \[ \mathcal{E}=\frac{\mu+1}{2}\ln\frac{\mu+1}{-}-\frac{\mu-1}{2}\ln\frac{\mu-1}{-}. \quad (B26) \] 

Figure 9 shows the entanglement entropy E along three paths: (a) no crossing of the first-order transition line, (b) passing through the critical point, and (c) crossing the first-order transition line along the path corresponding to conventional
 

QA ( \( \tau = 0 \) ). In the case (b) we can confirm that the entropy diverges continuously around the critical point. In contrast,

[1] T. Kadowaki and H. Nishimori, Phys. Rev. E 58, 5355 (1998).

[2] E. Farhi, J. Goldstone, S. Gutmann, J. Lapan, A. Lundgren, and D. Preda, Science 292, 472 (2001).

[3] G. E. Santoro, R. Martonák, E. Tosatti, and R. Car, Science 295, 2427 (2002).

[4] G. E. Santoro and E. Tosatti, J. Phys. A 39, R393 (2006).

[5] A. Das and B. K. Chakrabarti, Rev. Mod. Phys. 80, 1061 (2008).

[6] S. Morita and H. Nishimori, J. Math. Phys. 49, 125210 (2008).

[7] T. Albash and D. A. Lidar, Rev. Mod. Phys. 90, 015002 (2018).

[8] A. Lucas, Front. Phys. 2, 5 (2014).

[9] S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi, Science 220, 671 (1983).

[10] S. Jansen, M.-B. Ruskai, and R. Seiler, J. Math. Phys. 48, 102111 (2007).

[11] D. A. Lidar, A. T. Rezakhani, and A. Hamma, J. Math. Phys. 50, 102106 (2009).

[12] C. R. Laumann, R. Moessner, A. Scardicchio, and S. L. Sondhi, Phys. Rev. Lett. 109, 030502 (2012).

[13] J. Tsuda, Y. Yamanaka, and H. Nishimori, J. Phys. Soc. Jpn. 82, 114004 (2013).

[14] H. Nishimori and G. Ortiz, Elements of Phase Transitions and Critical Phenomena (Oxford University Press, Oxford, U.K., 2011).

[15] J. E. Avron, M. Fraas, G. M. Graf, and P. Grech, Commun. Math. Phys. 314, 163 (2012).

[16] L. C. Venuti, T. Albash, D. A. Lidar, and P. Zanardi, Phys. Rev. A 93, 032118 (2016).

[17] L. C. Venuti, T. Albash, M. Marvian, D. Lidar, and P. Zanardi, Phys. Rev. A 95, 042302 (2017).

[18] T. Jörg, F. Krzakala, J. Kurchan, and A. C. Maggs, Phys. Rev. Lett. 101, 147204 (2008).

[19] T. Jörg, F. Krzakala, J. Kurchan, A. C. Maggs, and J. Pujos, Europhys. Lett. 89, 40004 (2010).

[20] H. Nishimori, J. Tsuda, and S. Knysh, Phys. Rev. E 91, 012104 (2015).

[21] S. Matsuura, H. Nishimori, T. Albash, and D. A. Lidar, Phys. Rev. Lett. 116, 220501 (2016).

[22] S. Matsuura, H. Nishimori, W. Vinci, T. Albash, and D. A. Lidar, Phys. Rev. A 95, 022308 (2017).

[23] C. R. Laumann, R. Moessner, A. Scardicchio, and S. L. Sondhi, Eur. Phys. J. Spec. Top. 224, 75 (2015).

[24] G. A. Durkin, arXiv:1806.07602.

[25] Y. Seki and H. Nishimori, Phys. Rev. E 85, 051112 (2012).

[26] B. Seoane and H. Nishimori, J. Phys. A 45, 435301 (2012).

[27] Y. Seki and H. Nishimori, J. Phys. A 48, 335301 (2015).

[28] H. Nishimori and K. Takada, Front. ICT 4, 2 (2017).

[29] M. Ohkuwa, H. Nishimori, and D. A. Lidar, Phys. Rev. A 98, 022314 (2018).

for the case (c) a discontinuity exists at the transition point, a feature of a first-order phase transition [55].

[30] M. M. Rams, M. Mohseni, and A. del Campo, New J. Phys. 18, 123034 (2016).

[31] M. Mohseni, J. Strumpfer, and M. M. Rams, arXiv:1804.11037.

[32] J. Dziarmaga and M. M. Rams, New J. Phys. 12, 055007 (2010).

[33] W. H. Zurek and U. Dorner, Philos. Trans. R. Soc., A 366, 2953 (2008).

[34] E. Farhi, J. Goldstone, D. Gosset, S. Gutmann, H. B. Meyer, and P. Shor, Quantum Inf. Process. 11, 181 (2011).

[35] N. G. Dickson and M. H. S. Amin, Phys. Rev. Lett. 106, 050502 (2011).

[36] N. G. Dickson and M. H. Amin, Phys. Rev. A 85, 032303 (2012).

[37] T. Lanting, A. D. King, B. Evert, and E. Hoskinson, Phys. Rev. A 96, 042322 (2017).

[38] A. Del Campo, T. W. B. Kibble, and W. Zurek, J. Phys.: Condens. Matter 25, 404210 (2013).

[39] F. Gómez-Ruiz and A. del Campo, arXiv:1805.00525.

[40] J. I. Adame and P. L. McMahon, arXiv:1806.11091.

[41] M. Okuyama and M. Ohzeki, arXiv:1808.09707.

[42] Y. Susa, Y. Yamashiro, M. Yamamoto, and H. Nishimori, J. Phys. Soc. Jpn. 87, 023002 (2018).

[43] L. K. Grover, Phys. Rev. Lett. 79, 325 (1997).

[44] M. Filippone, S. Dusuel, and J. Vidal, Phys. Rev. A 83, 022327 (2011).

[45] T. Ichikawa, Master's thesis, Tokyo Institute of Technology, 2014.

[46] S. Shin, G. Smith, A. Smolin, and U. Vaziriani, arXiv:1404.6499.

[47] T. F. Rønnow, Z. Wang, J. Job, S. Boixo, S. V. Isakov, D. Wecker, J. M. Martinis, D. A. Lidar, and M. Troyer, Science 345, 420 (2014).

[48] T. Albash, T. F. Rønnow, M. Troyer, and D. A. Lidar, Eur. Phys. J. Spec. Top. 224, 111 (2015).

[49] T. Albash, W. Vinci, A. Mishra, P. A. Warburton, and D. A. Lidar, Phys. Rev. A 91, 042314 (2015).

[50] K. L. Pudenz, T. Albash, and D. A. Lidar, Phys. Rev. A 91, 042302 (2015).

[51] S. Boixo, V. N. Smelyanskiy, A. Shabani, S. V. Isakov, M. Dykman, V. S. Denchev, M. H. Amin, A. Y. Smirnov, M. Mohseni, and H. Neven, Nat. Commun. 7, 10327 (2016).

[52] A. Mishra, T. Albash, and D. A. Lidar, Nat. Commun. 9, 2917 (2018).

[53] P. J. D. Crowley, T. Durić, W. Vinci, P. A. Warburton, and A. G. Green, Phys. Rev. A 90, 042317 (2014).

[54] A. del Campo and W. H. Zurek, Int. J. Mod. Phys. A 29, 1430018 (2014).

[55] L. A. Wu, M. S. Sarandy, and D. A. Lidar, Phys. Rev. Lett. 93, 250404 (2004).
 
