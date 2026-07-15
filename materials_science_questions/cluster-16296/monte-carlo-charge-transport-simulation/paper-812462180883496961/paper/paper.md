# Enhancement of drift-velocity overshoot in silicon due to the intracollisional field effect

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1992 Semicond. Sci. Technol. 7 B383

(http://iopscience.iop.org/0268-1242/7/3B/100)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 129.115.103.99
This content was downloaded on 24/08/2015 at 04:59

Please note that terms and conditions apply.

# Enhancement of drift-velocity overshoot in silicon due to the intracollisional field effect

Fausto Rossi and Carlo Jacoboni

Dipartimento di Fisica ed Istituto Nazionale di Fisica della Materia dell'Università
di Modena, Via Campi 213/A, 41100 Modena, Italy

Abstract. A simulation of charge quantum transport in silicon is presented. We discuss how effects such as energy non-conserving transitions (or collisional broadening) and intracollisional field effect influence transient transport and, in particular, drift-velocity overshoot. The analysis is based on an improved version of the quantum Monte Carlo method developed by the authors during the last few years. Results show that, for the case of silicon, the intracollisional field effect plays the dominant role in determining deviations from the semiclassical results.

## 1. Introduction

Electron quantum transport in semiconductors is currently receiving a large amount of interest because of its possible relevance in small systems made available by modern technology [1,2]. Quantitative results are, however, still very scarce [3] owing to the mathematical difficulties encountered in solving quantum transport equations. One of the phenomena that are presumably influenced by quantum effects is drift-velocity overshoot at short times after the application of an electric field to a homogeneous system, because of the short timescale involved. A previous analysis [4] has shown that in GaAs the results of quantum transport calculations are very close to the semiclassical ones. However, as we shall see, it turns out that the effect is much stronger in silicon, due to the different wavevector dependence of the electronic scattering mechanisms.

The method developed by the authors for a numerical solution of the Liouville-von Neumann equation for the electronic density matrix [5] has been improved in order to increase its efficiency and to obtain accurate results for longer 'observation times' after the initial condition. The method is briefly described in the section 2. Numerical results are presented and discussed in section 3.

## 2. Theoretical approach and numerical procedure

In order to study the properties of the drift-velocity overshoot in a quantum scheme, we consider a non-interacting electron gas in a semiconductor crystal, coupled to the phonon gas. The system is assumed to be homogeneous, and its Hamiltonian is given by

$$
H=H_{\mathrm{e}}+H_{E}+H_{\mathrm{p}}+H_{\mathrm{ep}} \tag{1}
$$

where $H_{\mathrm{e}}$ is the Hamiltonian of an electron in a perfect crystal, $H_{E}=e E \cdot r$ is the term due to a homogeneous electric field and $H_{\mathrm{p}}$ is the Hamiltonian of the free-phonon system. The electron-phonon interaction Hamiltonian $H_{\mathrm{ep}}$ has the general form

$$
H_{\mathrm{ep}}=\sum_{\boldsymbol{q}} \mathrm{i} \hbar F(\boldsymbol{q})\left(a_{\boldsymbol{q}} \mathrm{e}^{\mathrm{i} \boldsymbol{q} \cdot \boldsymbol{r}}-a_{\boldsymbol{q}}^{\dagger} \mathrm{e}^{-\mathrm{i} \boldsymbol{q} \cdot \boldsymbol{r}}\right) \tag{2}
$$

where $F(\boldsymbol{q})$ is a function of the phonon momentum $\boldsymbol{q}$ whose explicit form depends on the particular scattering mechanism considered.

If we now consider the set of basis vectors $|x\rangle \equiv\left|\boldsymbol{k}_{0}, t\right\rangle\left|\left\{n_{\boldsymbol{q}}\right\}, t\right\rangle$ given by products of accelerated plane waves and phonon eigenstates [5], the Liouville-von Neumann equation that describes the time evolution of the density matrix $\rho$ in this representation contains only the perturbation Hamiltonian:

$$
\mathrm{i} \hbar \frac{\partial}{\partial t} \rho_{x, x^{\prime}}(t)=\left[H_{\mathrm{ep}}(t), \rho(t)\right]_{x, x^{\prime}} \tag{3}
$$

Starting from the above equation and following a standard procedure, a perturbative expansion for $\rho$ can be easily obtained, and this was the starting point for the quantum Monte Carlo (QMC) algorithm in its original version [5]. In this contribution we propose a refinement of the approach analogous to Chambers' formulation of transport.

As starting point, we introduce a transformed density matrix

$$
\bar{\rho}_{x, x^{\prime}}(t)=\exp \left(\int_{t_{0}}^{t} \gamma\left(t_{1}\right) \mathrm{d} t_{1}\right) \rho_{x, x^{\prime}}(t) \tag{4}
$$

in terms of a given arbitrary function $\gamma(t)$, whose physical interpretation will be discussed in what follows. Substituting $\rho$ as obtained from equation (4) into equation (3),

F Rossi and C Jacoboni

we derive the equation of motion for the transformed operator $\bar{\rho}$:
$$
\begin{aligned}
\frac{\partial}{\partial t} \bar{\rho}_{x, x^{\prime}}(t) & =\left\{\left(\mathscr{H}(t)+\frac{1}{2} \gamma(t)\right) \bar{\rho}(t)\right\}_{x, x^{\prime}} \\
& -\left\{\bar{\rho}(t)\left(\mathscr{H}(t)-\frac{1}{2} \gamma(t)\right)\right\}_{x, x^{\prime}}
\end{aligned}
\tag{5}
$$
where $\mathscr{H}=H_{\mathrm{ep}} / \mathrm{i} \hbar$.

After a formal integration of equation (5), a perturbative expansion for $\bar{\rho}$ can be easily obtained by iterative substitutions:
$$
\begin{aligned}
\bar{\rho}_{x, x^{\prime}}(t) & =\bar{\rho}_{x, x^{\prime}}\left(t_{0}\right)+\int_{t_{0}}^{t} \mathrm{~d} t_{1}\left\{\mathscr{H}\left(t_{1}\right) \bar{\rho}\left(t_{0}\right)\right\}_{x, x^{\prime}} \\
& -\int_{t_{0}}^{t} \mathrm{~d} t_{1}\left\{\bar{\rho}\left(t_{0}\right) \mathscr{H}\left(t_{1}\right)\right\}_{x, x^{\prime}} \\
& +\int_{t_{0}}^{t} \mathrm{~d} t_{1}\left\{\int_{t_{0}}^{t_{1}} \mathrm{~d} t_{2}\left\{\mathscr{H}\left(t_{1}\right) \mathscr{H}\left(t_{2}\right) \bar{\rho}\left(t_{0}\right)\right\}_{x, x^{\prime}}+\frac{1}{2} \gamma\left(t_{1}\right) \bar{\rho}_{x, x^{\prime}}\left(t_{0}\right)\right\} \\
& +\int_{t_{0}}^{t} \mathrm{~d} t_{1}\left\{\int_{t_{0}}^{t_{1}} \mathrm{~d} t_{2}\left\{\bar{\rho}\left(t_{0}\right) \mathscr{H}\left(t_{2}\right) \mathscr{H}\left(t_{1}\right)\right\}_{x, x^{\prime}}+\frac{1}{2} \gamma\left(t_{1}\right) \bar{\rho}_{x, x^{\prime}}\left(t_{0}\right)\right\} \\
& -\int_{t_{0}}^{t} \mathrm{~d} t_{1} \int_{t_{0}}^{t_{1}} \mathrm{~d} t_{2}\left\{\mathscr{H}\left(t_{1}\right) \bar{\rho}\left(t_{0}\right) \mathscr{H}\left(t_{2}\right)\right\}_{x, x^{\prime}} \\
& -\int_{t_{0}}^{t} \mathrm{~d} t_{1} \int_{t_{0}}^{t_{1}} \mathrm{~d} t_{2}\left\{\mathscr{H}\left(t_{2}\right) \bar{\rho}\left(t_{0}\right) \mathscr{H}\left(t_{1}\right)\right\}_{x, x^{\prime}}+\cdots \\
& =\bar{\rho}_{x, x^{\prime}}^{(0)}(t)+\Delta \bar{\rho}_{x, x^{\prime}}^{(1)}(t)+\Delta \bar{\rho}_{x, x^{\prime}}^{(2)}(t)+\cdots.
\end{aligned}
\tag{6}
$$

The above expansion for $\bar{\rho}$ differs from the original expansion for $\rho$ only for the appearance of the various $\gamma$ terms. In particular, reading equation (6) by means of the diagrammatic representation introduced in [5], it is possible to show that each term can still be regarded as a sequence of quantum processes in which any contribution due to a separated 'virtual' process is modified by a quantity $\gamma$. Therefore, the diagrams can be interpreted as sequences of real (in-scattering) processes, and between their vertices the propagators are 'dressed' by higher-order corrections to the function $\gamma(t)$. Thus $\gamma(t)$ plays the role of a lowest-order approximation to the quantum out-scattering rate (or the imaginary part of the self-energy).

Combining equations (4) and (6), we obtain:
$$
\begin{aligned}
\rho_{x, x^{\prime}}(t)= & \exp \left(-\int_{t_{0}}^{t} \gamma\left(t_{1}\right) \mathrm{d} t_{1}\right) \rho_{x, x^{\prime}}\left(t_{0}\right) \\
& +\exp \left(-\int_{t_{0}}^{t} \gamma\left(t_{1}\right) \mathrm{d} t_{1}\right) \sum_{n=1}^{\infty} \Delta \bar{\rho}_{x, x^{\prime}}^{(n)}(t).
\end{aligned}
\tag{7}
$$

The above result can be regarded as the quantum analogue of the iterative expansion of the Chambers integral equation for semiclassical transport. Here, the scattering-out damping factor is automatically accounted for by sampling the infinite sum through the generation of sequences of 'free flights' and interaction processes, as in the standard ensemble Monte Carlo procedure. The usual 'self-scattering' technique can also be employed. A constant $\gamma$ has been used in the present simulation.

A second improvement in the QMC procedure consists of a mixed, analytical/numerical, evaluation of the multiple time integrals in equation (6). Details on the present form of the QMC procedure will be published elsewhere.

![](./images/812462180883496961_1.jpg)

Figure 1. Quantum drift velocity (curve marked with circles) compared with the semiclassical one for different values of the applied electric field at low temperature $(T=10 \mathrm{~K})$.

## 3. Results and conclusions

The new version of the QMC procedure, discussed above, has been applied to the analysis of the drift-velocity overshoot in silicon. We used a simplified semiconductor model characterized by a single spherical and parabolic band (effective mass $0.295 m_{0}$ ). The electron-phonon interaction has been introduced in terms of a deformation potential due to a single optical-phonon mode (equivalent temperature $450 \mathrm{~K}$, coupling constant $8 \times 10^{8} \mathrm{eV} \mathrm{cm}^{-1}$, crystal density $2.329 \mathrm{~g} \mathrm{~cm}^{-3}$ ). Numerical results have been obtained for different values of applied electric field and temperature.

Figure 1 shows a comparison between the quantum and the semiclassical drift-velocity overshoot at a low temperature $(T=10 \mathrm{~K})$. Because of the quantum nature of the investigated phenomenon, the curves obtained from the QMC are intended to represent the expectation value of the electron drift velocity if measured at time $t$ after the initial condition, and therefore a separate simulation is required for each point of the curve. Here, for increasing values of the external field, we can see a corresponding enhancement of the quantum effect on the drift-velocity overshoot. This behaviour is mainly due to the intracollisional field effect (ICFE) [6]. In fact this effect depends inversely upon the scalar product $E \cdot q$ and therefore favours transitions with momentum transfer normal to the electric field, thus decreasing the drift-velocity relaxation. For a better understanding of this phenomenon, a detailed analysis of the lowest order contribution to the angular distribution of the carriers (i.e. the contribution due to trajectories containing a single quantum process) has been performed. Figure 2 shows the angular electron distribution obtained from the quantum simulation by subtracting the drift of the carriers after the mean time of the scattering process. We

B384

Enhancement of drift-velocity overshoot in silicon

![](./images/812462180883496961_2.jpg)

Figure 2. Angular distribution of the carriers after the scattering process, integrated over the final energies, as obtained from the QMC simulation. The different curves refer to the indicated values of the applied electric field.

see a strong anisotropy in the angular distribution of the carriers which for decreasing values of the electric field approaches the isotropic distribution of the final states obtained from the standard Fermi golden rule for the present case where $F(\boldsymbol{q})$ is $\boldsymbol{q}$-independent.

A similar effect was not found in the previous analysis for GaAs [4] because the explicit form of the electron-phonon interaction for a polar semiconductor $(F(\boldsymbol{q}) \propto$$1 / q)$ favours by itself low momentum transfers even in the semiclassical case.

In a recent paper [7] it has been suggested that ICFE should not have an appreciable influence in the high-field limit. The problem may be connected with the fact that, since ICFE depends upon $\boldsymbol{q} \cdot \boldsymbol{E}$, there is always a region in $\boldsymbol{q}$-space where the high-field limit is not reached. However, this point requires further investigation.

Figure 3 shows the electron mean kinetic energy. The difference between the quantum and the semiclassical results is smaller than for the drift velocity in figure 1.

Figure 4 shows a comparison between the quantum and the semiclassical drift velocity for $E=60 \mathrm{kV} \mathrm{cm}^{-1}$ at room temperature. Again, we find in the quantum analysis a lower velocity relaxation induced by the strong applied electric field.

![](./images/812462180883496961_3.jpg)

Figure 3. Quantum mean kinetic energy (curve marked with circles) compared with the semiclassical one for different values of the applied electric field.

![](./images/812462180883496961_4.jpg)

Figure 4. Quantum drift velocity (curve marked with circles) compared with the semiclassical one at room temperature for $E=60 \mathrm{kV} \mathrm{cm}^{-1}$.

Finally, even though the scattering mechanism considered in the model (optical phonons) has a classical threshold energy for emission, the quantum corrections due to below-threshold transitions are not relevant, similarly to the case of GaAs [4]. The reason is that the threshold energy is reached by the carriers at very short times when the effect of the perturbation on the electron dynamics is still very small.

In conclusion, the present analysis has shown how ICFE destroys the isotropy of deformation-potential optical-phonon scattering, thus decreasing the corresponding momentum relaxation. A strong influence on the drift-velocity overshoot in silicon has been found, and we may expect this effect to be present also in steady-state conditions.

### Acknowledgments
We are particularly grateful to Tilmann Kuhn for many stimulating and enjoyable discussions. This research was financed by Progetto Finalizzato Materiali e Dispositivi per l'Elettronica a Stato Solido (MADESS) del Consiglio Nazionale delle Ricerche (CNR).

### References
[1] Grubin H L, Ferry D K and Jacoboni C (eds) 1988 *The Physics of Submicron Semiconductor Devices* (NATO ASI Series B, vol. 180)
[2] Ferry D K, Barker J R and Jacoboni C (eds) 1990 *Quantum Transport in Semiconductors* (New York: Plenum) in press
[3] Rossi F, Brunetti R and Jacoboni C 1991 *Hot Carriers in Semiconductor Microstructures: Physics and Applications* ed J Shah (New York: Academic) in press
[4] Rossi F and Jacoboni C 1989 *Solid State Electron.* **32** 1411
[5] Brunetti R, Jacoboni C and Rossi F 1989 *Phys. Rev.* B **39** 10781
[6] Barker J R 1978 *Solid State Electron.* **21** 267
[7] Lipavský P, Khan F S, Abdolsalami F and Wilkins J W 1991 *Phys. Rev.* B **43** 4885

B385