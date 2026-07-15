# Second harmonic generation coefficients in push-pull polyenes: a model exact study *

S. Ramasesha $^{a}$ and Puspendu K. Das $^{b}$

$^{a}$ Solid State and Structural Chemistry Unit and $^{b}$ Department of Inorganic and Physical Chemistry,
Indian Institute of Science, Bangalore 560 012, India

Received 17 January 1990

The correlated Pariser-Parr-Pople (PPP) model for interacting $\pi$ electrons is employed for calculating the model exact SHG coefficients ($\beta^{\text{exact}}$) of push-pull polyenes with 4 to 10 carbon atoms in the all-trans configuration. These calculations are restricted to di-substituted polyenes with an electron donating (push) and an electron withdrawing (pull) groups. The effects of the push-pull strengths, the locations of the push and the pull groups in the chain, the twist around the polyene backbone, and the length of the chain, on the SHG response of these molecules are studied. These results are compared with that obtained ($\beta^{\text{CT}}$) from a simple two-state model where the excited state is a charge transfer state. The similarities and the differences in these two quantities ($\beta^{\text{exact}}$ and $\beta^{\text{CT}}$) are discussed. Based on these results we present guide lines for synthesizing molecules with larger SHG coefficients.

## 1. Introduction
Currently there is considerable interest in substituted conjugated polyenes and related compounds possessing second-order nonlinear optical (NLO) properties [1-12]. They normally exhibit large NLO responses due to the presence of $\pi$ electrons. For their potential technological applications, tailoring of organic molecules with ever larger NLO coefficients has attracted the attention of synthetic chemists [13-19]. To become successful in this venture, it is necessary to have proper guidelines to design such molecules. Unfortunately, most of the properties associated with NLO responses seem to require a knowledge of all the excited states of the molecule and thus become difficult to compute. Until recently, theoretical attempts were aimed at computing the SHG coefficients from the knowledge of a few low-lying states of the system. In the simplest case, a two-level picture has been used for the calculation of these coefficients [8,20,21]. Indeed the SHG coefficients computed by this model provided the only guidelines for designing organic molecules with large NLO response [22].

Though in principle, the calculation of NLO coefficients requires a knowledge of the full excitation spectrum of the molecule, in practice only the $\pi$ electrons in these molecules play the pivotal role. Consequently any calculation that takes into account the entire excitation spectrum of the $\pi$ system should suffice for making accurate predictions about the NLO properties. The conventional Hückel model for describing $\pi$ electrons has been widely used but with little success for the model does not include interactions among the electrons.

Recent studies on polyenes and other conjugated systems [23-26] based on the Pariser-Parr-Pople (PPP) model [27,28] for the description of the $\pi$ electrons has been successful in unifying all the known properties in these molecules. In order to obtain reliable NLO coefficients for conjugated systems, it is necessary to calculate these quantities within the framework of the correlated PPP model. In the independent particle model, all the excitations of the system are described by single particle excitations within the manifold of one particle energy levels. However, in the interacting models, this is not possible as these excitations are not eigen states of the system and each

---
* Communication No. 633 from the Solid State and Structural Chemistry Unit.

0301-0104/90/$ 03.50 © 1990 - Elsevier Science Publishers B.V. (North-Holland)

excitation has to be considered independently. The configuration space spanned by the $\pi$ electrons in a molecule with $N$ conjugated carbon atoms increases approximately as $4^{N}$ and even for relatively small $N$, the number of excitations becomes too large to handle individually. Therefore, any computation of the NLO coefficients based on the sum over states approach necessarily has to resort to the uncontrolled approximation of arbitrarily truncating the number of excitations considered in the multiple sums [29,30]. Approaches such as the finite field method [31,32] are not very useful in this context since they provide response of the system to static external perturbations only.

Recently, a formulation for the direct and exact calculation of NLO coefficients has been developed and implemented for calculating the SHG and THG (third harmonic generation) coefficients in conjugated molecules [29,30]. This method along with the PPP model has, for the first time, provided a means of computing the NLO properties of conjugated molecules without any uncontrolled approximations. The only approximations are that (i) the electric dipole term alone is retained in the interaction between radiation and matter and (ii) the $p_{z}$ orbitals in the conjugated system are taken into account while all other orbitals are neglected.

Using the direct formulation for the calculation of the NLO coefficients, in this paper, we examine in detail the SHG properties of push-pull polyenes. We compare the SHG coefficients obtained from the two-state calculations with exact results in the PPP models. We also report results on the dependence of SHG coefficients on the strength of push-pull groups, on the location of the push and the pull substituents and on the stereochemistry of the polyene backbone. We present the size dependence of the SHG coefficients in these molecules and correlate these coefficients with the change in dipole moment between the ground and excited states. In section 2, we introduce the PPP model and give a brief outline of the computational procedure. In section 3, we present results of our calculations and discuss these in terms of qualitative change at the molecular level. Finally, in section 4 we summarize the observations made in these calculations in the context of designing $\pi$-conjugated molecules with large SHG response.

## 2. PPP model Hamiltonian and the computational procedure

The PPP model Hamiltonian for polyenes is best described by starting with the Hückel model, which is now only of pedagogical importance. The Hückel Hamiltonian, $H_{0}$, for polyenes is defined by

$$
\begin{aligned}
H_{0}= & \sum_{p=1}^{N} \sum_{\sigma} \epsilon_{p} a_{p \sigma}^{*} a_{p \sigma} \\
& +\sum_{p=1}^{N-1} \sum_{\sigma} t_{0}\left[1-(-1)^{p} \delta\right]\left(a_{p \sigma}^{*} a_{p+1, \sigma}+\text { h.c. }\right),
\end{aligned}
$$

where $N$ is the number of carbon atoms in the polyene chain and $a_{p \sigma}^{*}\left(a_{p \sigma}\right)$ creates (annihilates) an electron with spin $\sigma$ in the $p_{z}$ orbital on the $p$ th carbon atom. The Hückel resonance integral between the carbon atoms $p$ and $p+1$ is given by $t_{0}\left[1-(-1)^{p} \delta\right]$ where $\delta$ is the bond alternation parameter and $\epsilon_{p}$ is the orbital energy of the $\mathrm{p}_{z}$ orbital on the $p$ th carbon atom. In the lowest level of approximation, we may introduce electron-electron interactions by assuming that repulsion exists between two electrons only when they are occupying the same orbital. The Hamiltonian for this model, known as the Hubbard model [33], is given by

$$
H_{\text {Hubbard }}=H_{0}+U \sum_{p=1}^{N} \hat{n}_{p, \sigma} \hat{n}_{p,-\sigma},
$$

where $U$ is the Hubbard correlation strength and $\hat{n}_{p, \sigma}$ are the occupation number operators. This model was first invented for treating electron-electron interactions in metals where the screening due to mobile conduction electrons severly truncates the range of Coulomb interactions. However, it is not appropriate for polyenes which in the limit of infinite chain length are known to be semiconducting. In these systems, we expect the range of inter-electron interactions to extend beyond the same site. It is reasonable to assume that the inter-electron repulsions in the limit of large separation is inversely proportional to the distance between them. In the other limit of two electrons occupying the same site the repulsion is given by $U$, the difference in the electron affinity and the ionization potential for the site. For intermediate distances, Ohno [34] interpolated the potential between these two limits. Thus, Ohno parameterization for carbon atom is given by

$$V_{p p^{\prime}}=14.397\left(1.6348+r_{p p^{\prime}}^{2}\right)^{-1 / 2}\qquad(3)$$

and the PPP Hamiltonian with Ohno parameteriza- tion becomes,
$$H_{\mathrm{PPP}}=H_{\text {Hubbard }}+\sum_{p>p^{\prime}} V_{p p^{\prime}} \hat{n}_{p} \hat{n}_{p^{\prime}}.\qquad(4)$$

The PPP Hamiltonian also results from a full many electron Hamiltonian after making a zero differential overlap (ZDO) approximation and parameterizing the nonvanishing integrals as above. Extensive theo- retical studies of polyenes have shown that the PPP model is apt for describing these systems [23-26]. In our calculations, we have chosen $t_{0}=2.4 eV$ andδ=0.07 which are appropriate for polyenes. The ge- ometry of the polyene chain used for our purpose is shown in fig. 1. The transfer integral $t_{0}(1+\delta)$ of the double bond around which rotation is carried out is assumed to take the value $t_{0}(1+\delta) cos \Theta$ when ro tated by an angle $\Theta$ . The rotation also leads to a change in the potential energy of the VB states due to a change in the geometry of the molecule.

An all-trans polyene with identical orbital ener- gies, $\epsilon_{p}$ , has a center of inversion and as a conse quence has a zero SHG coefficient. However, substi- tuted all-trans polyenes with the substituents breaking the inversion symmetry result in nonzero SHG coef- ficients. In the case of push-pull polyenes, we assume that the push and the pull groups do not participate in the conjugation but merely shift the orbital ener- gies by $\epsilon$ at the substituent sites. The strength of the push (pull) group is reflected in the magnitude of the shift in the energy of the $p_{z}$ orbital on the carbon to which the group is attached. In all our calculations we assume that the absolute strengths of the push or pull groups are the same. In other words, though the en- ergy of the $p_{z}$ orbital at the carbon site to which the push group is attached is lowered and that of the $p_{z}$ orbital at the pull site is raised, we assume that the absolute shift at both these sites remains the same. We have also restricted our calculations to just one push and one pull groups over a polyene chain.

![](./images/811083529730392065_1.jpg)

Fig. 1. Geometry of the polyene chain and the transfer integrals for the single and double bonds. Also shown is the bond around which rotation is carried out for altering the stereochemistry of the conjugated backbone.

A general method [29,30] that has recently been developed for computing static as well as dynamic polarizabilities and hyperpolarizabilities of a model Hamiltonian in the state L involves computing the perturbation correction, $\phi_{i, L}^{(1)}$ , to the eigenfunction, $\phi_{L}^{(0)}$ , using the formula
$$\left(\hat{H}-E_{L}-\hbar \Omega\right) \phi_{i, L}^{(1)}(\Omega)=-\hat{\mu}_{i} \phi_{L}^{(0)}\qquad(5)$$
with $\hat{\mu}_{i}$ being the i th component of the dipole dis placement operator defined by
$$\hat{\mu}_{i}=e \sum_{p} r_{p, i} \hat{n}_{p}-\mu_{i, L},\qquad(6)$$
where $r_{p, i}$ is the i th component of the position vector of the pth carbon atom and $\mu_{i, L}$ is the i th component of the dipole moment in the state L. The SHG coef- ficients $\beta_{i j k}$ in the ground state in which we are cur rently interested are given by
$$\begin{aligned}
& \beta_{i j k}\left(\Omega_{1}, \Omega_{2}\right) \\
& \quad=\mathrm{P}\left\langle\phi_{i}^{(1)}\left(-\Omega_{1},-\Omega_{2}\right)\left|\hat{\mu}_{j}\right| \phi_{k}^{(1)}\left(-\Omega_{2}\right)\right\rangle / 8,
\end{aligned}\qquad(7)$$
where P is an operator that permutes the pairs $(-\Omega_{1}$  $-\Omega_{2}, i),(\Omega_{1}, j)$ , and $(\Omega_{2}, k)$ and generates six terms. The perturbation corrections are calculated with re- spect to the ground state $\phi_{G}^{(0)}$ .

The introduction of push-pull groups destroys the electron-hole (or alternancy) symmetry besides lift- ing the inversion symmetry. However, the total spin invariance of the Hamiltonian is preserved and, therefore, working with a spin adopted basis such as the VB basis is still possible [35]. The state $\phi_{G}^{(0)}$ for a given N is solved exactly by carrying out a full con- figuration interaction (CI) calculation in the VB ba- sis. The equation for $\phi^{(1)}$ is solved by transforming the operator form of eq. (5) into a set of inhomoge- neous simultaneous equations by expressing the function $\phi^{(1)}$ as a superposition of VB functions [36]. The function $\phi^{(1)}$ is completely determined if we solve for the coefficients in the superposition. Further- more, $\phi^{(1)}$ is determined exactly, if the linear equa tions are set up in the complete Hilbert space spanned

by these functions. In all our calculations, we have indeed used the complete Hilbert space spanned by the appropriate Hamiltonians for setting up the linear system of equations and therefore the value of the coefficients $\beta$ that we calculate are model exact (henceforth will be called $\beta^{\text{exact}}$). The resulting linear system for $\phi^{(1)}$, in our case, cannot be solved by Gauss-Seidel iteration scheme and we resort to the conjugate gradient technique. The calculations reported here have been carried out on a $\mu$VAX II system. The computation for the SHG coefficients of the 10 site push-pull polyene takes the longest time. In this case the complete space of singlets spans a 19404-dimensional Hilbert space. The cpu time required to get all the six components of $\beta$ is approximately 100 h for each frequency for a given push-pull strength, $\epsilon$.

## 3. Results and discussion

We have carried out calculation of the model exact coefficients $\beta_{ijk}^{\text{exact}}$ as a function of $\epsilon$ (push-pull strength) for polyene chains of 4, 6, 8 and 10 carbon atoms using the above formulation. The dependence of the $\beta$ coefficients on the frequency, $\Omega$, for most values of $\epsilon$ has also been studied. We have obtained an approximate functional dependence of $\beta$ on the length of the polyene backbone and on the relative positions of the push and the pull groups. Besides, we have looked at the variation of $\beta$ as a function of the torsional angle $\theta$ when the polyene backbone is rotated about the central bond in the push-pull all-trans hexatrienes (fig. 1). We compare $\beta^{\text{exact}}$ with $\beta^{\text{CT}}$, obtained from the two level system where the excited state is the charge transfer state. These results are discussed separately below.

### 3.1. Dependence of $\beta^{\text{exact}}$ on the push-pull strength

For studying this dependence, we set the orbital energies of all the carbon $p_{z}$ orbitals to zero, except the terminal carbon atoms which are fixed at $+\epsilon$ and $-\epsilon$ to simulate the pull and the push strengths respectively. In real systems, if the push-pull effect is obtained by introducing hetero atoms such as nitrogen or oxygen, besides the site energies the correlation energies would be different and we need to modify eq. (3) for intersite repulsions. However, if the push-pull effect is through substituted alkyl groups then our present formulation would be adequate. In these cases, one could expect $\epsilon$ to vary between 0.5 and 2.0 eV. While it is possible to calculate $\beta$ for many values of $\epsilon$ in the case of chains of 4, 6 and 8 carbon atoms, the same in the case of ten carbon chain is computationally time consuming. Since the all-trans push-pull polyenes are planar in our model, the $i, j$ and $k$ values correspond to $x$ or $y$ only. To calculate the tumbling averaged component $\beta_{x}^{\text{exact}}$, we use the relation [20]

$$
\beta_{x}=\beta_{x x x}+\left(\beta_{x y y}+2 \beta_{y y x}\right) / 3. \tag{8}
$$

In fig. 2, we show the dependence of $\beta^{x}$ on $\epsilon$ for a push-pull polyene chain of eight carbon atoms for three different values of $\Omega$. $\beta_{x}$ increases linearly with increasing $\epsilon$ for all the frequencies. The slope of the $\beta_{x}$ versus $\epsilon$ curve also increases with increasing $\Omega$. This in effect means that the SHG coefficient increases with increasing strength of the push and the pull groups and also that this increase is faster at higher

![](./images/811083529730392065_2.jpg)

Fig. 2. $\beta_{x}$ versus $\epsilon$ for 1, 8 substituted all-trans octatetraene at three different excitation frequencies.

frequencies. The rapid rise in $\beta^{\text{exact}}$ as a function of $\epsilon$ at higher frequencies may be explained in the following manner. We note (table 1) that the charge transfer excitation gap (for which the transition moment as well as the change in dipole moment are very large) reduces as $\epsilon$ increases. As a result, as the excitation frequency approaches resonance the dispersion in $\beta^{\text{exact}}$ as a function of $\epsilon$ is enhanced. At low excitation frequencies, this dispersion is small and hence we find this slow rise in the SHG coefficients with increasing push-pull strength.

### 3.2. Variation of $\beta$ with the system size

The SHG coefficients are strongly dependent on the size of the $\pi$ system. In order to obtain a reliable algebraic relation between the SHG coefficient and the length of the push-pull polyenes, a knowledge of $\beta^{\text{exact}}$ is essential. This is because, approximate values of $\beta$ obtained from truncated sums or from states obtained within an incomplete basis will not be size consistent. In the case of third harmonic generation, it has been demonstrated that the THG coefficients obtained from incomplete CI calculation and a truncated sum show a stronger dependence on the system size than the exact values [29,30]. Fig. 3 displays a log-log plot of $\beta_{x}$ versus $L$ where $L$ is the length of the polyene backbone. The exact value has the exponent $\alpha \approx 2.5$ for $\epsilon=0.6 \mathrm{eV}$ and $\alpha \approx 3.4$ for $\epsilon=2.0 \mathrm{eV}$, where $\alpha$ is defined by

$$
\beta^{\text{exact}} \approx a L^{\alpha}. \tag{9}
$$

It is interesting to note that the exponent $\alpha$ is different for different push-pull strengths and increases with increase in the push-pull strength.

<table>
<caption>Table 1<br>The charge transfer excitation gap in push-pull polyenes as a function of the push-pull strength, $\epsilon$, for all-trans polyene chains of 6, 8 and 10 carbon atoms</caption>
<thead>
<tr>
<th>Ser.<br>No.</th>
<th>$\epsilon$ (eV)</th>
<th colspan="3">Charge transfer excitation gap (eV)</th>
</tr>
<tr>
<th></th>
<th></th>
<th>$N=6$</th>
<th>$N=8$</th>
<th>$N=10$</th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>0.4</td>
<td>5.032</td>
<td>4.550</td>
<td>4.225</td>
</tr>
<tr>
<td>3</td>
<td>0.6</td>
<td>5.014</td>
<td>4.537</td>
<td>4.217</td>
</tr>
<tr>
<td>4</td>
<td>0.8</td>
<td>4.990</td>
<td>4.520</td>
<td>4.205</td>
</tr>
<tr>
<td>5</td>
<td>1.0</td>
<td>4.959</td>
<td>4.500</td>
<td>4.187</td>
</tr>
<tr>
<td>6</td>
<td>1.5</td>
<td>4.862</td>
<td>4.423</td>
<td>4.136</td>
</tr>
<tr>
<td>7</td>
<td>2.0</td>
<td>4.745</td>
<td>4.332</td>
<td>4.060</td>
</tr>
</tbody>
</table>

![](./images/811083529730392065_3.jpg)

Fig. 3. Log-log plot of $\beta_{x}$ versus chain length $(L)$ along $x$-axis for two different values of $\epsilon$ at the YAG excitation frequency of 1.167 eV.

### 3.3. Relative position of the push and the pull groups and its effect on $\beta$

In this study, we shift the positions of the substituents by changing the two sites at which we simulate the push and the pull groups. The calculations are restricted to the push-pull polyene of six carbon atoms. The $\beta^{\text{exact}}$ values are calculated for three different values of $\epsilon$ at the YAG excitation frequency of 1.167 eV. The results as a function of $\epsilon$, and the position of the substituents are displayed in table 2. We find that the SHG coefficients depend not merely on the distance separating the push and the pull groups but also on the relative locations. For instance if the push group is on the carbon atom one and the pull group is located on an even numbered carbon atom, then the

<table>
<caption>Table 2 Dependence of $\beta_x^{\text{exact}}$ on the relative positions of the push and pull groups in the disubstituted all-trans hexatriene at $\epsilon=2.0$ eV for laser excitation frequency of 1.167 eV. Also given are the ground and excited state dipole moments in debye</caption>
<thead>
<tr>
<th>Rel. pos.</th>
<th>$\beta_x^{\text{exact}}$ (au)</th>
<th>$|\mu|_{\text{gr.st.}}$</th>
<th>$|\mu|_{\text{ex.st.}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>(1, 2)</td>
<td>6.118</td>
<td>3.11</td>
<td>2.05</td>
</tr>
<tr>
<td>(1, 3)</td>
<td>179.8</td>
<td>0.51</td>
<td>3.98</td>
</tr>
<tr>
<td>(1, 4)</td>
<td>102.9</td>
<td>3.39</td>
<td>2.03</td>
</tr>
<tr>
<td>(1, 5)</td>
<td>243.1</td>
<td>0.83</td>
<td>4.74</td>
</tr>
<tr>
<td>(1, 6)</td>
<td>300.1</td>
<td>3.79</td>
<td>1.95</td>
</tr>
</tbody>
</table>

SHG response is weak, with the exception of the terminal substitutions. This is perhaps due to the fact that in polyene chains starting with a Kekulé structure, resonance places charges preferentially on even numbered carbon atoms. Having a positive site energy on even carbon atoms, therefore, suppresses charged states resulting in lower polarizabilities. However, in the case of 1, 3, and 1, 5 substitutions, such charged states are not suppressed. In the case of terminal substitutions, since the terminal carbon atoms do not provide a pathway for connecting different resonance structures the above argument is not applicable. In all cases, substituents at the terminal positions led to the highest value of $\beta^{\text{exact}}$.

The dipole moment in the ground state of a push-pull polyene with substituents at even numbered carbon positions is large, while the same in the case of substituents at odd carbon positions is small. The inverse is true for the dipole moment in the lowest excited state. This indicates that in the ground state the ionic structures are favoured for substitutions at even positions. Also for large SHG response, the charge separation in the ground state should be small but at the same time the charge separation in the excited state must be large. Again the only exception being the case of substitutions at the terminal positions.

### 3.4. Effect of the polyene backbone stereochemistry on $\beta$

Substituted polyenes may be designed and synthesized such that they deviate from planar geometry due to steric effects arising from the presence of bulky groups. The nonplanarity of the conjugated backbone results in reduced conjugation and hence a smaller transfer integral (Hückel resonance integral) for the bond about which the backbone is twisted. To explore the influence of this twist on the SHG response, we confine ourselves to the simple case of push-pull hexatriene, with 1, 6 substitutions, rotated about the central double bond. Based on our studies of sudden polarization in polyenes, we believe that the results are qualitatively correct for longer polyenes [37] as well as for rotation about any other C-C bond. The push-pull strength $\epsilon$ is fixed at 2.0 eV. When the polyene is rotated about the middle double bond, the resulting nonplanarity of the molecule manifests in terms of nonzero SHG components that also contain the z-coordinate. In this case the tumbling averaged $\beta_x$ is given by

$$\beta_{x}=\beta_{x x x}+\left(\beta_{x y y}+2 \beta_{y y x}\right) / 3+\left(\beta_{x z z}+2 \beta_{z z x}\right) / 3 \text {. (10)}$$

We concentrate only on $\beta_x$ since this is, by far, the largest component for all twist angles.

$\beta_x$ is plotted against $\boldsymbol{\theta}$ in fig. 4. We notice that $\beta_x$ increases gradually as the angle $\boldsymbol{\theta}$ is increased. This is in spite of the fact that the x-dimension of the mol-

![](./images/811083529730392065_4.jpg)

Fig. 4. $\beta_x$ versus twist angle, $\boldsymbol{\theta}$, for 1, 6 substituted all-trans hexatriene for push-pull strength, $\epsilon=2.0$ eV at the YAG excitation frequency.

ecule in the fixed coordinate system decreases as $\Theta$ is increased. Therefore, the SHG coefficient along the longest axis in the molecule for nonzero $\Theta$ would be larger than what is shown in the plot. The coefficient $\beta_x$ reaches a maximum near about $\Theta=75^{\circ}$. However, at $\Theta=90^{\circ}$, the value of $\beta_x$ falls suddenly to its minimum. It is also at this angle that the conjugation is broken completely. It is known from sudden polarization studies [37] of substituted twisted polyenes that in correlated models, the ground state continues to be predominantly of the diradical type while the excited state is a nearly ionic state with unequal number of electrons on either side of the segment. One consequence of this result is the nearly vanishing transition dipole to the lowest energy excited state. On the other side of $90^{\circ}$, the SHG coefficient is maximum at $105^{\circ}$ and decreases gradually to a value lower than in the all-trans configuration. This can be attributed to the smaller $x$-dimension $(L)$ of the polyene at $180^{\circ}$ than that in the all-trans case. We find that the initial increase in $\beta_x$ when $\Theta$ is changed form $0^{\circ}$ or $180^{\circ}$ is due to smaller excitation gaps to the low-lying excited states (table 3). However, there is no direct experimental evidence for this fact. At $\Theta=75^{\circ}$ or $105^{\circ}$ the lowest energy excitation is close to two-photon resonance and a sharp increase in $\beta_x$ results at these geometries. However, at $\Theta=90^{\circ}$, though the optical gap is near the two-photon resonance (for the laser excitation at $1.167 \mathrm{eV}$ ) the SHG coefficient drops to its lowest value since the transition dipole moment between the ground state and the first excited state nearly vanishes. To understand this effect in greater detail, we have calculated the energies of a few low-lying states and the dipole matrix elements amongst these states for hexatriene. Using these data, we calculate the SHG coefficients within two-, three- and four-level schemes for every $\Theta$. Fig. 5 shows the plot of $\beta_x$ as a function of $\Theta$ in these schemes. We note that in all the cases $\beta_x$ drops to its lowest value for $\Theta=90^{\circ}$. The value of $\beta_x$ itself is close to $\beta_x^{\text {exact }}$ only in three- and four-level schemes because in the two level scheme the dominant contribution due to the charge transfer excitation is not taken into account. This $\beta_x$ versus $\Theta$ dependence resembles the dependence of static polarizability on $\Theta$ in the ground state of the PPP models [37].

In the above studies we have shown that deviation from planarity of the conjugation backbone is desirable for large $\beta$. It is well known that highly twisted polyenes are quite stable in their ground states [17]. The present calculations should be appropriate even in twisted geometries for long-chain polyenes since $\sigma-\pi$ separability is only aided as the $\pi$ excitation energies decrease in magnitude and the $\sigma$ framework remains almost undisturbed. The magnitude of this increase depends on factors such as how close the excitation frequency or its multiple is to the resonances of the model.

Table 3
Energies of a few of the low-lying states (in eV) of hexatriene with $\epsilon=2.0 \mathrm{eV}$ at different $\Theta$ values (in degree). The zero of the energy for each $\Theta$ corresponds to the energy of the ground state at that twist angle

<table>
<thead>
<tr>
<th>$\Theta$</th>
<th>$E_2$</th>
<th>$E_3$</th>
<th>$E_4$</th>
<th>$E_5$</th>
<th>$E_6$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>4.632</td>
<td>4.745</td>
<td>5.506</td>
<td>7.255</td>
<td>7.255</td>
</tr>
<tr>
<td>15</td>
<td>4.535</td>
<td>4.685</td>
<td>5.387</td>
<td>6.442</td>
<td>7.206</td>
</tr>
<tr>
<td>30</td>
<td>4.243</td>
<td>4.503</td>
<td>5.036</td>
<td>6.386</td>
<td>7.053</td>
</tr>
<tr>
<td>45</td>
<td>3.769</td>
<td>4.188</td>
<td>4.485</td>
<td>6.390</td>
<td>6.740</td>
</tr>
<tr>
<td>60</td>
<td>3.162</td>
<td>3.730</td>
<td>3.812</td>
<td>5.558</td>
<td>6.144</td>
</tr>
<tr>
<td>75</td>
<td>2.566</td>
<td>3.183</td>
<td>4.625</td>
<td>4.625</td>
<td>5.602</td>
</tr>
<tr>
<td>90</td>
<td>2.286</td>
<td>2.878</td>
<td>2.891</td>
<td>5.379</td>
<td>5.379</td>
</tr>
<tr>
<td>105</td>
<td>2.564</td>
<td>3.180</td>
<td>4.629</td>
<td>4.621</td>
<td>5.594</td>
</tr>
<tr>
<td>120</td>
<td>3.155</td>
<td>3.724</td>
<td>3.821</td>
<td>5.550</td>
<td>6.121</td>
</tr>
<tr>
<td>135</td>
<td>3.754</td>
<td>4.178</td>
<td>4.501</td>
<td>6.370</td>
<td>6.714</td>
</tr>
<tr>
<td>150</td>
<td>4.217</td>
<td>4.488</td>
<td>5.057</td>
<td>6.414</td>
<td>6.890</td>
</tr>
<tr>
<td>165</td>
<td>4.498</td>
<td>4.665</td>
<td>5.413</td>
<td>6.478</td>
<td>7.164</td>
</tr>
<tr>
<td>180</td>
<td>4.591</td>
<td>4.722</td>
<td>5.533</td>
<td>6.501</td>
<td>7.219</td>
</tr>
</tbody>
</table>

![](./images/811083529730392065_5.jpg)

Fig. 5. Plot of $\beta_x$ in the (a) two-level, (b) three-level, and (c) four-level schemes as a function of $\theta$. While the scale of $\beta_x$ is the same in all three cases, the zero is shifted suitably to fit the curves on a single plot.

### 3.5. Comparison of $\beta^{exact}$ with $\beta^{CT}$

The two-state model for estimating the SHG coefficients in conjugated organic systems with electron donor and acceptor groups has been widely used to provide guide lines to synthetic chemists. The states considered in this model are the ground and the charge transfer excited states. In the unsubstituted all-trans long-chain polyenes, it is well known that the lowest excited state is a diradical (covalent) singlet state and it is not connected with the ground state by the electric dipole operator [38,39]. Occurrence of this state is attributed to the presence of strong interelectron interactions among the $\pi$ electrons. However, by introducing push and pull groups, we break the electron-hole as well as the inversion symmetries of the polyene and the diradical state becomes a weakly dipole allowed state. This state, however, is not the charge transfer state that should be considered in the two-state model. The second excited state in these push-pull polyenes is derived from the dipole allowed excited state of the unsubstituted all-trans polyenes. This, in fact, is the charge transfer state identified from a large difference in the dipole moment between this state and the ground state.

In the two-level model, the SHG coefficient is given by

$$
\begin{aligned}
& \beta_{i j k}^{\mathrm{CT}}\left(\Omega_{1}, \Omega_{2}\right) \\
& =\frac{1}{8 h^{2}} \frac{\mathrm{P}\left\langle\mathrm{G}\left|\hat{\mu}_{i}\right| \mathrm{CT}\right\rangle\left\langle\mathrm{CT}\left|\hat{\mu}_{j}\right| \mathrm{CT}\right\rangle\left\langle\mathrm{CT}\left|\hat{\mu}_{k}\right| \mathrm{G}\right\rangle}{\left(E_{\mathrm{CT}}-\Omega_{1}-\Omega_{2}\right)\left(E_{\mathrm{CT}}-\Omega_{2}\right)},
\end{aligned}
$$

where $P$ is again the permutation operator and $E_{\mathrm{CT}}$ is the charge transfer excitation energy. The diagonal matrix element of the dipole displacement operator involving the charge transfer state $|\mathrm{CT}\rangle$ gives the difference in dipole moment between the ground state and the charge transfer state. The off-diagonal matrix elements of this operator multiplied by $E_{\mathrm{CT}}$ give the oscillator strength for the charge transfer excitation and hence we get the familiar equation for $\beta^{\mathrm{CT}}$ due to Oudar et al. [8].

In our calculations, we obtain model exact $|\mathrm{G}\rangle$, $|\mathrm{CT}\rangle$, and $E_{\mathrm{CT}}$. The charge transfer state $|\mathrm{CT}\rangle$ in all the cases we have studied happens to be the second excited singlet state. From the eigenstates we calculate the dipole moments in these states as well as the transition dipoles. Using eq. (11) we calculate $\beta_{x x x}$, $\beta_{x y y}$ and $\beta_{y y x}$ and the tumbling averaged $\beta_{x}^{\mathrm{CT}}$ at an excitation frequency of $1.167 \mathrm{eV}$ for two different $\epsilon$ values for chain lengths of $4,6,8$ and 10 carbon atoms. We find that (table 4 ) in all these cases the $\beta^{\mathrm{CT}}$ values are consistently higher than the $\beta^{\text {exact }}$ values. Furthermore, the SHG response calculated on the basis of the two-state model increases more rapidly with chain length than the exact value for higher push-pull strength. Our results show that Oudar's formula on a two-level model is a reasonable approximation for small system sizes and large push-pull strengths. Another interesting feature that emerges from our calculation is that the charge transfer excitation energy as well as the transition dipole matrix elements do not vary significantly with $\epsilon$ (table 5). However, the

**Table 4**
Comparison of $\beta_x^{\text{exact}}$ and $\beta_x^{\text{CT}}$ (in au) for all-trans polyenes of 4 to 10 carbon atoms for two different push-pull strengths $\epsilon$ at an excitation frequency of 1.167 eV

<table>
  <thead>
    <tr>
      <th>$N$</th>
      <th colspan="2">$\epsilon$=0.6 eV</th>
      <th colspan="2">$\epsilon$=2.0 eV</th>
    </tr>
    <tr>
      <th></th>
      <th>$\beta^{\text{exact}}$</th>
      <th>$\beta^{\text{CT}}$</th>
      <th>$\beta^{\text{exact}}$</th>
      <th>$\beta^{\text{CT}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>4</td>
      <td>28.94</td>
      <td>58.45</td>
      <td>75.53</td>
      <td>107.2</td>
    </tr>
    <tr>
      <td>6</td>
      <td>89.95</td>
      <td>463.5</td>
      <td>300.1</td>
      <td>513.6</td>
    </tr>
    <tr>
      <td>8</td>
      <td>195.0</td>
      <td>336.9</td>
      <td>703.1</td>
      <td>1063</td>
    </tr>
    <tr>
      <td>10</td>
      <td>344.0</td>
      <td>597.7</td>
      <td>1275</td>
      <td>1950</td>
    </tr>
  </tbody>
</table>

**Table 5**
The charge transfer excitation energy $E_{\text{CT}}$, the difference in the ground and excited state dipole moments $|\Delta\omega|$ and the $x$- and $y$-components of the transition dipoles as a function of the push-pull strength $\epsilon$ for all-trans 1,8-octatetraene

<table>
  <thead>
    <tr>
      <th>$\epsilon$ (eV)</th>
      <th>$E_{\text{CT}}$ (eV)</th>
      <th>$\mu_x^{\text{CT}}$ (D)</th>
      <th>$\mu_y^{\text{CT}}$ (d)</th>
      <th>$|\Delta\mu|$ (D)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.4</td>
      <td>4.550</td>
      <td>8.453</td>
      <td>2.026</td>
      <td>1.272</td>
    </tr>
    <tr>
      <td>0.6</td>
      <td>4.537</td>
      <td>8.458</td>
      <td>2.026</td>
      <td>1.906</td>
    </tr>
    <tr>
      <td>0.8</td>
      <td>4.519</td>
      <td>8.462</td>
      <td>2.026</td>
      <td>2.496</td>
    </tr>
    <tr>
      <td>1.0</td>
      <td>4.497</td>
      <td>8.472</td>
      <td>2.021</td>
      <td>3.067</td>
    </tr>
    <tr>
      <td>1.5</td>
      <td>4.423</td>
      <td>8.491</td>
      <td>2.011</td>
      <td>4.330</td>
    </tr>
    <tr>
      <td>2.0</td>
      <td>4.332</td>
      <td>8.496</td>
      <td>2.002</td>
      <td>5.213</td>
    </tr>
  </tbody>
</table>

![](./images/811083529730392065_6.jpg)

difference in dipole moments between the ground and the excited states varies linearly with $\epsilon$ and accounts for most of the variation in $\beta^{\text{CT}}$ with $\epsilon$. Therefore, for a given push-pull polyene system, we need to concentrate on maximizing $\mu$ to maximize $\beta$. Indeed, $\beta^{\text{exact}}$ also shows a similar dependence on $\mu$ giving more credence to the above postulate (fig. 6). The rapid rise in $\beta^{\text{exact}}$ near $\mu$=5 D is partly due to dispersion effects and partly due to a rapid increase in the transition dipole moments to the low-lying excited states (from the ground state) at large push-pull strengths.

### 4. Summary
In this paper we have utilized the correlated PPP model for treating the interacting $\pi$ electrons in conjugated all-trans di-substituted polyenes of 4 to 10

Fig. 6. $\beta_x$ versus $\mu$ for 1, 8 substituted all-trans octatetraene at an excitation frequency of 1.167 eV.

carbon atoms. The SHG coefficients calculated are model exact and hence more reliable than any that were previously reported. We have shown for the first time that $\beta^{\text{CT}}$ calculated by a two-state model where the excited state is the charge transfer state, gives al- ways an overestimate for $\beta$. However, the basic fea- tures remain unaltered insofar as the dependence of $\beta$ on different quantities like the strength of the sub- stituent push-pull capacity, the length of the mole- cule and the laser excitation frequency is concerned. $\beta_{x}^{\text{exact}}$ varies linearly with the push-pull strength $(\epsilon)$ at lower values of $\epsilon$ and has a stronger dependence for higher values of $\epsilon$. Also the dependence of $\beta_{x}$ on the push-pull strength is stronger at higher excitation frequencies. The change in $\beta_{x}$ as a function of length of the molecule is smaller than that predicted by a two-state model, but tends to become larger as the push-pull strength is increased. The strongest SHG response is noticed when the push-pull substituents are on the terminal carbon atoms. The calculation for the SHG coefficients on relative positions of the sub- stituents shows that substitutions on odd numbered carbon atoms produce larger $\beta_{x}$. Further in all these cases the ground state dipole moment is smaller than the excited state dipole moment. We find that non- planarity of the conjugated backbone, without com- pletely breaking the conjugation, leads to higher SHG response. At large $\Theta$ values this increase is mainly due to the excitation frequency coming close to the two photon resonance for that frequency. However, at smaller values of $\Theta$ the increase may be completely attributed to the rotational twist around the central bond.

What follows from above is that the strategy for synthesizing conjugated push-pull polyenes with large SHG response should be the following. (i) The length of the conjugation must be large. (ii) The push and the pull strengths must also be large. In other words, the groups that can donate and/or withdraw elec- trons easily to the backbone are desired. (iii) Suffi- ciently bulky groups that force a nonplanar geometry on the backbone for the stable molecule should be in- troduced. (iv) The push/pull substituents may be at- tached to the terminal carbon atoms.

Our calculations have been restricted to just one push and one pull groups attached to the conjugation backbone and both the push and the pull strengths are assumed to be equal in magnitude. It will be in- teresting to extend this study to poly substituted push- pull polyenes in order to particularly understand where exactly these substitutions be made along the backbone to maximize the SHG response. In a way this implies that we are introducing an inhomoge- neous electric field along the polyene chain to obtain a nonzero SHG response. It would, therefore, be worthwhile in this context, to study the electric field induced second harmonic (EFISH) generation coef- ficients [40] in polyenes. Some preliminary calcula- tions of this nature are already under way in our group. We are also investigating the effect of static electric fields on the SHG coefficients of push-pull polyenes. It is hoped that with all these theoretical calculations a clear picture will emerge for under- standing nonlinear optical properties at the molecu- lar level. That, in turn, will provide guidelines re- garding design, synthesis, and characterization of novel molecules.

## References

[1] J. Zyss, in: Nonlinear Optical and Electroactive Polymers, eds. P.N. Prasad and D.J. UIrich (Plenum Press, New York, 1988).

[2] R.N. DeMartino, E.W. Choe, G. Kharian, D. Haas, T. Leslie, G. Nelson, J. Stamatoff, D. Stuetz, C.C. Tang and H. Yoon, in: Nonlinear Optical and Electroactive Polymers, eds. P.N. Prasad and D. Ulrich (Plenum Press, New York, 1988).

[3] P.F. Gordon and P. Gregory, in: Organic Chemistry in Coulor (Springer, Berlin, 1983).

[4] R.J. Twieg and K. Jain, in: Nonlinear Optical Properties of Organic and Polymeric Materials, ACS Symp. Ser. 233, ed. D.J. Williams (American Chemical Society, Washington, 1983).

[5] D. Pugh and J.N. Sherwood, Chem. Britain (1988) 544.

[6] Y. Wang, W. Tam, S.H. Stevenson, R.A. Clement and J. Calabrese, Chem. Phys. Letters 148 (1988) 136.

[7] S.J. Lalama, K.D. Singer, A.F. Garito and K.N. Desai, Appl. Phys. Letters 39 (1981) 940.

[8] J.L. Oudar and D.S. Chemla, J. Chem. Phys. 66 (1977) 2664.

[9] D.F. Eaton, A.G. Anderson, W. Tam and Y. Wang, J. Am. Chem. Soc. 109 (1987) 1886.

[10] A.M. Glass, Science 226 (1984) 657.

[11] D.J. Williams, Angew. Chem. Intern. Ed. 23 (1984) 690.

[12] T. Kobayashi, H. Ohtani and K. Kurokawa, Chem. Phys. Letters 121 (1985) 356.

[13] M. Blanchard-Desce, I. Ledoux, J-M. Lehn, J. Malthete and J. Zyss, J. Chem. Soc. Chem. Commun. (1987) 737.

[14] C. Foquency, J-M. Lehn and J. Malthete, J. Chem. Soc. Chem. Commun. (1988) 1424.

[15] L.M. Loew, L. Simpson, A. Hassner and V. Alexanian, J. Am. Chem. Soc. 101 (1979) 5439.

[16] J.F. Nicoud and R.J. Twieg, in: Nonliear Optical Properties of Organic Molecules and Crystals, Vol. 1, eds. D.S. Chemla and J. Zyss (Academic Press, New York, 1987).

[17] J. Sundstrom, Topics Stereochem. 14 (1983) 84.

[18] A.G. Anderson, J.C. Calabrese, W. Tam and D.I. Williams, Chem. Phys. Letters 134 (1987) 392.

[19] I.C.K. Hoo and Y.R. Shen, Opt. Eng. 25 (1985) 579.

[20] D. Pugh and J.O. Morley, in: Nonlinear Optical Properties of Organic Molecules and Crystals, Vol. 1, eds. D.S. Chemla and J. Zyss (Academic Press, New York, 1987).

[21] A. Ulman, J. Phys. Chem. 92 (1988) 2385.

[22] J.O. Morley, V.J. Docherty and D. Pugh, J. Chem. Soc. Perkin Trans. II 6 (1987) 1351.

[23] S. Ramasesha and Z.G. Soos, J. Chem. Phys. 80 (1984) 3278.

[24] Z.G. Soos and S. Ramasesha, Phys. Rev. B 29 (1984) 5410.

[25] Z.G. Soos and S. Ramasesha, Phys. Rev. Letters 51 (1983) 2374.

[26] S. Ramasesha and Z.G. Soos, Chem. Phys. 91 (1984) 35.

[27] R. Pariser and R.G. Parr, J. Chem. Phys. 21 (1953) 466.

[28] J.A. Pople, Trans. Faraday Soc. 49 (1953) 1375.

[29] S. Ramasesha and Z.G. Soos, Chem. Phys. Letters 153 (1988) 171.

[30] Z.G. Soos and S. Ramasesha, J. Chem. Phys. 90 (1989) 1067.

[31] H.D. Cohen and C.C.J. Roothan, J. Chem. Phys. 43 (1965) 534.

[32] S. Ramasesha and I.D.L. Albert, Chem. Phys. Letters 154 (1989) 501.

[33] J. Hubbard, Proc. Roy. Soc. A 276 (1963) 238.

[34] K. Ohno, Theoret. Chim. Acta 2 (1964) 219.

[35] Z.G. Soos and S. Ramasesha, in: Valence Bond Theory and Chemical Structure, eds. D.J. Klein and N. Trinajstic (Elsevier, Amsterdam, 1989).

[36] S. Kuwajima and Z.G. Soos, J. Am. Chem. Soc. 109 (1987) 107.

[37] S. Ramasesha and I.D.L. Albert, Chem. Phys. 142 (1990) 395.

[38] B.S. Hudson, B.E. Kohler and K. Schulten, in: Excited States, Vol. 6, ed. E.C. Lim (Academic Press, New York, 1982).

[39] S. Ramasesha, J. Mol. Struct. 194 (1989) 149.

[40] R.A. Huijts and G.L.J. Hesselink, Chem. Phys. Letters 156 (1989) 209.