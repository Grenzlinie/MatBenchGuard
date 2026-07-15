Electrochimica Acta 54 (2009) 3011-3019

![](./images/811885237607858176_1.jpg)

Contents lists available at ScienceDirect

# Electrochemical deposition on surface nanometric defects: Thermodynamics and grand canonical Monte Carlo simulations

Noelia B. Luque $^{a}$ , Luis Reinaudi $^{a}$ , Pablo Serra $^{b}$ , Ezequiel P.M. Leiva $^{a, *, 1}$

$^{a}$ Unidad de Matemática y Física, Facultad de Ciencias Químicas, INFIQC, Universidad Nacional de Córdoba, Córdoba 5000, Argentina
$^{b}$ Facultad de Matemática, Astronomía y Física, Universidad Nacional de Córdoba, Córdoba 5000, Argentina

---

## ARTICLE INFO

**Article history:**
Received 25 September 2008
Accepted 6 December 2008
Available online 13 December 2008

**Keywords:**
Electrochemical nanostructuring
Monte Carlo simulations
Cavity filling

## ABSTRACT

A thermodynamic analysis is performed on electrochemical metal deposition in the cavity of a foreign substrate. In particular, the deposition of Cu and Ag in nanometer-sized holes on $Au(111)$ is studied by means of off-lattice atomistic Grand Canonical Monte Carlo simulations, using embedded atom method potentials. The present simulation conditions emulate experiments of electrochemical metal deposition in nanocavities, as performed in the literature. Depending on the system, remarkable differences are found in the way in which the defects are decorated, as well as in their energetics. When the interaction of the adsorbate atoms with the substrate is less favorable than the bulk interaction of the adsorbate, clusters are found that grow stepwise over the level of the surface. In the opposite case, the filling of the cavity occurs stepwise, without the occurrence of cluster growth above the surface level. The results of the simulations present a good qualitative agreement with experimental results from the literature.

© 2008 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Thanks to the advent of different scanning probe microscopy (SPM) techniques, the perspective of matter manipulation at the atomic scale has become a reality in the last two decades. This is also true in electrochemistry, where the control of the potential difference applied to the electrochemical interface may provide control on the chemical potential of species adsorbed at this interface. A status report on this topic has been given by Kolb and Simeone recently [1], and related theoretical aspects have been discussed by Luque and Leiva [2] and in recent reviews [3,4]. Generally speaking, the large variety of electrochemical nanostructuring techniques may involve different ways of transferring matter from a SPM tip to a surface generating its decoration, the generation of defects on the surface of a substrate, or both. Pioneering work in the latter direction was undertaken by Li et al. [5]. These authors managed to create an Ag nanostructure on a graphite basal plane surface by the following procedure: They deposited first Ag at underpotentials on the Pt STM tip. Then, a double potential pulse was used to create a pit on the surface of graphite, and subsequently dissolve the Ag from the tip that deposited selectively into the newly created cavity. Further research on defect nanostructuring was undertaken by Xia et al. [6], who managed to create defects on a $Au(111)$ surface by the application of ultrashort (10 ns) voltage pulses to the tip of an electrochemical STM arrangement. The electrochemical cell composed of the tip and the sample within nanometer distance was small enough that the double layers may be polarized within nanoseconds. This lead to local confinement of the reactions and to the formation of nanostructures, so that for every pulse applied just one hole is created directly under the tip. The holes generated in this way were then filled with Cu by an accurate potentiostatic control. Some relevant findings of these experiments were as follows:

- It is possible to generate holes on the surface of the substrate through the application of very short negative voltage pulses to the STM tip. This procedure succeeds only using highly concentrated electrolytes.
- If the potential applied to the substrate is controlled carefully, it is possible to confine the deposition of Cu from the solution to the volume inside the hole. This is so because metal deposition on the $(1×1)$ Cu structure outside the hole is disfavored with respect to metal deposition on the hole, where the lattice parameter of Cu should be close to that of the bulk metal.
- Cluster growth above the surface level of the substrate was found to be layer by layer. This is due to the lower binding energy of the atoms at the border of the hole. For each layer growing over the surface level, an extra free energy cost must be paid to generate this border.
- The size of the deposit depends on the size of the hole and not on polarization time, denoting a certain balance between electrochemical energy and the surface energy of the cluster.

---

* Corresponding author. Tel.: +54 351 4344972; fax: +54 351 4344972.
E-mail address: eleiva@fcq.unc.edu.ar (E.P.M. Leiva).
$^{1}$ ISE member.

0013-4686/$ - see front matter © 2008 Elsevier Ltd. All rights reserved.
doi:10.1016/j.electacta.2008.12.013

![](./images/811885237607858176_2.jpg)

This technique has been also employed by Solomun and Kautek [7] to study the filling of cavities on Au(111) by Bi and Ag. In this work, the behavior of Bi was contrasted with that of Ag. While the holes are filled at underpotentials in the first case, the Au holes are only filled by Ag during the layer-by-layer growth of Ag at overpotentials.

It is the aim of the present work to develop a thermodynamic framework to analyze nanocavity decoration and to perform computer simulation for two systems where the interactions lead to two distinct behaviors: on one side, to the growth of a cluster over the surface level when the interaction of the deposited atoms prevails over the interaction with the substrate. On the other side, to the filling of the nanocavity without the occurrence of cluster growth when the interaction of the adsorbates with the substrate is stronger that the interaction between adsorbate atoms. While the approximate nature of the interaction potentials employed allows only for a qualitative description of this process, the physical picture coming out of the present modeling promises to be useful its future understanding and control.

## 2. Thermodynamic considerations

In order to analyze the thermodynamic aspects of the deposition of a metal in a nanocavity of a foreign substrate, it is useful to draw a thermodynamic cycle as shown in Fig. 1.

A similar analysis has been performed to consider the thermodynamics of underpotential deposition (upd) [8]. We show there a hypothetical working (w) electrode made of the metal S, with a cavity in which atoms of type M have been deposited. The potential of this electrode is measured with respect to a reference electrode (r) made of the metal M immersed in the same solution containing ions of the type $M^{+z}$. The counter electrode is not shown in the figure. On the other hand, the reference electrode could have such a large area so as to serve itself as a counter electrode. A piece of metal $M_2$ has been attached to the end of both w and r electrodes. In our first analysis we assume that the potential difference measured corresponds to an equilibrium state at which no current flows in the system.

Since equilibrium has been established, the ion cores $M^{+z}$ of the deposit in the cavity are in equilibrium with the ion cores in the bulk metal of the electrode r. Thus, the free energy change for the transfer of a $M^{+z}$ ion from the cavity to the bulk metal, say $\Delta G_T$, must be equal to zero. An alternative pathway for the same ion is shown in Fig. 1 involving the corresponding free energy changes, say $\Delta G_i$.

![](./images/811885237607858176_3.jpg)

Fig. 1. Scheme of part of an electrochemical cell with a working electrode with a decorated nanocavity and a reference electrode made of the same metal M being deposited.

These can be summarized in the following set of equations:

$$
\begin{aligned}
& \Delta G_{1}=-\mu_{M / S}, \quad \Delta G_{2}=I_{+z}, \quad \Delta G_{3}=-z e \Phi_{M_{2}}, \\
& \Delta G_{4}=z e\left(\Psi_{M}-\Psi_{S}\right), \quad \Delta G_{5}=z e \Phi_{M_{2}}, \\
& \Delta G_{6}=-I_{+z}, \quad \Delta G_{7}=\mu_{M}
\end{aligned} \tag{1}
$$

where $e$ represents the elemental charge, $\mu_{M / S}$ is the chemical potential of the $M$ type atoms in the nanocavity, $I_{+z}$ is the energy required to remove $z$ electrons from the atom $M$, $\Psi_{M}$ and $\Psi_{S}$ are the outer potentials of the w and the r electrodes, respectively, $\Phi_{M_{2}}$ is the work function of metal $M_2$ and $\mu_{M}$ is the chemical potential of the $M$ type atoms in bulk $M$.

Similarly to the case of the upd problem, the equality:

$$
\Delta G_{T}=\sum_{i=1}^{7} \Delta G_{i}=0 \tag{2}
$$

leads to the equality:

$$
\eta=\left(\Psi_{S}-\Psi_{M}\right)=\frac{\mu_{M}-\mu_{M / S}}{z e} \tag{3}
$$

where $\eta$ is the potential difference measured between the w and the r electrodes. If $\eta>0$ for some type of atomic arrangement of the M atoms on the S surface, we are in the presence of the so-called underpotential deposition phenomenon. That is, adsorbate atoms may occur a potential that are positive with respect to the underpotential deposition phenomenon. On the other hand, if $\eta<0$, this means that the atomic arrangement with the chemical potential $\mu_{M / S}$ is less stable than the bulk metal and could only be observed at overpotentials, constituting a metastable state. We come to this point in the discussion below.

There is however an important difference with respect to the upd problem that must be discussed if theoretical calculations of $\eta$ are sought.

Let us consider the upd case first. In this case, $\eta$ defines the so-called underpotential shift $\eta^{\text {upd }}$, a measure for the stability of the adatoms in the monolayer with respect to the bulk. In order to discuss in energetic terms, let us neglect for the moment entropic and volume effects, considering the case $T=0$ and $p=0$. This is not a severe approximation for the present condensed phase systems, as we have discussed previously [9], where entropic and volume changes were found to deliver a very small contribution to the underpotential shift. In this limit $\eta^{\text {upd }}$ can be calculated from the binding energy of the adatoms in the monolayer and the bulk binding energy of the metal $u_{\text {bind }}^{M}$:

$$
\eta^{\text {upd }} \approx \frac{u_{\text {bind }}^{M}-\left(\left(U^{M+S}-U_{S}\right) / N_{M}\right)}{z e}=\frac{u_{\text {bind }}^{M}-\left(U^{M / S} / N_{M}\right)}{z e} \tag{4}
$$

where $U^{M+S}$ is the energy of the adatoms + substrate system and $U_S$ is the energy of the naked substrate. In the second equality, we have defined the quantity $U^{M+S}=(U^{M+S}-U_{S})$ to have more compact notation. Note that we have replaced the differential quantity $\mu_{M / S}$ by $(U^{M / S}/N_{M})$. In fact, neglecting entropic effects $\mu_{M / S}$ would be given by

$$
\mu_{M / S} \approx\left(\frac{\partial U^{M / S}}{\partial N_{M}}\right)_{P, T} \tag{5}
$$

If we model the upd monolayer as an infinite system, $U^{M+S}$ can be considered to be an extensive quantity:

$$
U^{M / S}=N_{M} u_{M / S} \tag{6}
$$

where $u_{M / S}$ is the binding energy per atom $(U^{M / S}/N_{M})$, a quantity that in principle is independent from the system size due to the absence of border effects.

Thus, differentiation of Eq. (6) yields:

$$
\left(\frac{\partial U^{M / S}}{\partial N_{M}}\right)_{P, T}=u_{M / S}=\frac{U^{M / S}}{N_{M}}
\tag{7}
$$

The physical meaning of Eq. (7) is that if we assembled a monolayer atom by atom we would obtain most of the time the same energy as the binding energy of an adatom in the monolayer. This is analogous to the considerations that are made concerning the disassemblement of a bulk metal removing atoms in a kink position [10].

In the case of a nanostructure, the binding energy is no longer an extensive quantity like the proposal in Eq. (6), and an equation like that given in (4) can no longer be employed. However, for a nanostructure, Eq. (3) still holds, and the correct approximation to $\eta$ would be

$$
\eta=\frac{\mu_{M}-\left(\left(U^{M / S}-T S^{M / S}+p V^{M / S}-\varepsilon\right) / N_{M}\right)}{z e}
\tag{8}
$$

where $S^{M / S}$ is the entropy of the adatoms in the nanostructure, $V^{M / S}$ is the corresponding volume and $\varepsilon$ is the so-called subdivision potential [11]. It is a kind of system chemical potential, and it corresponds to the change of the energy of the thermodynamic ensemble when a system is added to it. While it is negligible for macroscopic systems it becomes a finite positive quantity for a system with an interface as those considered in the present work. Thus, even in the limit $T \rightarrow 0, p \rightarrow 0$ we have:

$$
\eta \rightarrow \frac{\mu_{M}-\left(U^{M / S} / N_{M}\right)+\left(\varepsilon / N_{M}\right)}{z e}
\tag{9}
$$

so that in addition to the binding energy per atom an extra contribution must be taken into account.

Note that in the derivation of Eq. (3) no current flow through an external circuit was considered. In fact, in step 3 the electrons of the adatom were brought back to the w electrode and only the transfer of an ion was taken into account. For this reason, the free energy $G$ of the system was employed as equilibrium criterion, since no exchange of matter was assumed between the system (cell plus electrodes) and its environment. In other words, we have considered what we usually denominate an $N, P, T$ system. An alternative derivation, that is useful for the further discussion given below, can be made taking into account electron exchange between the system and the environment. Let us now assume that the w and r electrodes are connected to two infinite electronic reservoirs with electrochemical potentials $\tilde{\mu}_{e}^{\mathrm{w}}$ and $\tilde{\mu}_{e}^{\mathrm{r}}$, respectively, thus providing a Volta potential difference $\Psi_{S}-\Psi_{M}=\left(\tilde{\mu}_{e}^{\mathrm{r}}-\tilde{\mu}_{e}^{\mathrm{w}} / e\right)$ (the contacts are made of the same material $M_{2}$ so that the chemical part of the electrochemical potential is the same). These reservoirs may remove electrons from (inject into) the system keeping $\Psi_{S}-\Psi_{M}$ constant. With these boundary conditions, the proper thermodynamic function to study the system is the Legendre transform:

$$
\tilde{G}=G-N_{e}^{\mathrm{w}} \tilde{\mu}_{e}^{\mathrm{w}}-N_{e}^{\mathrm{r}} \tilde{\mu}_{e}^{\mathrm{r}}
\tag{10}
$$

where $N_{e}^{\mathrm{w}}$ and $N_{e}^{\mathrm{r}}$ are the number of electrons in the w and the r electrodes, respectively. In thermodynamic terms, this defines a $\tilde{\mu}_{e}^{\mathrm{r}}$, $\tilde{\mu}_{e}^{\mathrm{w}}, P, T$ system. Since we are considering the filling of a nanocavity (nanosystem), the contributions to the thermodynamic functions will in turn be divided into two parts. One due to the contribution of the nanostructure itself, called "nano", and another one due to the rest of the macroscopic system, that we will label with the term "macro". Besides the deposited atoms, we include as a part of the nanostructure those substrate atoms affected by the presence of the deposit (via electronic, stress effects, etc.). The usefulness of this division will become obvious below. Thus, we have

$$
G=G_{\text {nano }}+G_{\text {macro }}
\tag{11}
$$

The macro term contains contribution from r and the w electrodes, that we will denote with $G_{\text {macro }}^{\mathrm{r}}$ and $G_{\text {macro }}^{\mathrm{w}}$, respectively, while the term $G_{\text {nano }}$ corresponds exclusively to the w electrode. Thus, we have

$$
G=G_{\text {nano }}+G_{\text {macro }}^{\mathrm{r}}+G_{\text {macro }}^{\mathrm{w}}
\tag{12}
$$

Using standard thermodynamics (see for example Ref. [12]) the term $G_{\text {macro }}^{\mathrm{r}}$ can be written as

$$
G_{\text {macro }}^{\mathrm{r}}=U_{\text {macro }}^{\mathrm{r}}+p V_{\text {macro }}^{\mathrm{r}}-T S_{\text {macro }}^{\mathrm{r}}
\tag{13}
$$

where $U_{\text {macro }}^{\mathrm{r}}$ is given by

$$
U_{\text {macro }}^{\mathrm{r}}=T S_{\text {macro }}^{\mathrm{r}}-P V_{\text {macro }}^{\mathrm{r}}+N_{e}^{\mathrm{r}} \tilde{\mu}_{e}^{\mathrm{r}}+N_{M}^{\mathrm{r}} \tilde{\mu}_{M}^{\mathrm{r}}
\tag{14}
$$

where $N_{M}^{\mathrm{r}}$ is the number of $M$ core ions in the r electrode and $\tilde{\mu}_{M}^{\mathrm{r}}$ is their corresponding electrochemical potential. Thus, adding (14) to (13) results in:

$$
G_{\text {macro }}^{\mathrm{r}}=N_{e}^{\mathrm{r}} \tilde{\mu}_{e}^{\mathrm{r}}+N_{M}^{\mathrm{r}} \tilde{\mu}_{M}^{\mathrm{r}}
\tag{15}
$$

The term $G_{\text {macro }}^{\mathrm{w}}$ can be in turn written as

$$
G_{\text {macro }}^{\mathrm{w}}=U_{\text {macro }}^{\mathrm{w}}+P V_{\text {macro }}^{\mathrm{w}}-T S_{\text {macro }}^{\mathrm{w}}
\tag{16}
$$

where now $U_{\text {macro }}^{\mathrm{w}}$ is given by

$$
U_{\text {macro }}^{\mathrm{w}}=T S_{\text {macro }}^{\mathrm{w}}-P V_{\text {macro }}^{\mathrm{w}}+N_{e, \text { macro }}^{\mathrm{w}} \tilde{\mu}_{e}^{\mathrm{w}}+N_{S}^{\mathrm{w}} \tilde{\mu}_{S}^{\mathrm{w}}
\tag{17}
$$

Here, $N_{e, \text { macro }}^{\mathrm{w}}$ is the number of electrons in the w electrode not belonging to the nanostructure, that added to the number of electrons belonging to the nanostructure, say, $N_{e, \text { nano }}^{\mathrm{w}}$, yields the total number of electrons in the w electrode:

$$
N_{e}^{\mathrm{w}}=N_{e, \text { macro }}^{\mathrm{w}}+N_{e, \text { nano }}^{\mathrm{w}}
\tag{18}
$$

$N_{S}^{\mathrm{w}}$ is the number of $S$ core ions in the w electrode and $\tilde{\mu}_{S}^{\mathrm{w}}$ is the corresponding electrochemical potential.

Adding (17) to (16) results in:

$$
G_{\text {macro }}^{\mathrm{w}}=N_{e, \text { macro }}^{\mathrm{w}} \tilde{\mu}_{e}^{\mathrm{w}}+N_{S}^{\mathrm{w}} \tilde{\mu}_{S}^{\mathrm{w}}
\tag{19}
$$

note that an analog of Eqs. (15) and (19) cannot be written for $G_{\text {nano }}$, since Eqs. (14) and (17) rely on the fact that the energy is a first-order homogeneous function of the entropy, the volume and the number of constituent particles, something that is no longer valid for a nanostructure, because of edge effects. The Legendre transform (10) can be now written using (15), (19) and (12) to replace in (10)

$$
\begin{aligned}
\tilde{G}= & G_{\text {nano }}+N_{S}^{\mathrm{w}} \tilde{\mu}_{S}^{\mathrm{w}}+N_{M}^{\mathrm{r}} \tilde{\mu}_{M}^{\mathrm{r}}+\left(N_{e, \text { macro }}^{\mathrm{w}}-N_{e}^{\mathrm{w}}\right) \tilde{\mu}_{e}^{\mathrm{w}}=G_{\text {nano }}+N_{S}^{\mathrm{w}} \tilde{\mu}_{S}^{\mathrm{w}} \\
& +N_{M}^{\mathrm{r}} \tilde{\mu}_{M}^{\mathrm{r}}-N_{e, \text { nano }}^{\mathrm{w}} \tilde{\mu}_{e}^{\mathrm{w}}
\end{aligned}
\tag{20}
$$

where we have used Eq. (17) to obtain the second equality. In the latter equation, the electrochemical potential of the core $M$ ions, $\tilde{\mu}_{M}^{\mathrm{r}}$, can be replaced in terms of the chemical potential of the atoms of type $M, \mu_{M}$, and the electrochemical potential of the electrons in the r electrode taking into account that:

$$
\mu_{M}=\tilde{\mu}_{M}^{\mathrm{r}}+z \tilde{\mu}_{e}^{\mathrm{r}}
\tag{21}
$$

so that (20) turns into:

$$
\tilde{G}=G_{\text {nano }}+N_{S}^{\mathrm{w}} \tilde{\mu}_{S}^{\mathrm{w}}+N_{M}^{\mathrm{r}} \mu_{M}-z N_{M}^{\mathrm{r}} \tilde{\mu}_{e}^{\mathrm{r}}-N_{e, \text { nano }}^{\mathrm{w}} \tilde{\mu}_{e}^{\mathrm{w}}
\tag{22}
$$

Let us now consider the transfer of $N_{M}$ atoms of type $M$ from the r to the w electrode generating a nanostructure. The change of the transform (20) can be written as

$$
\Delta \tilde{G}=\Delta G_{\text {nano }}+\Delta N_{M}^{\mathrm{r}} \mu_{M}-z \Delta N_{M}^{\mathrm{r}} \tilde{\mu}_{e}^{\mathrm{r}}-\Delta N_{e, \text { nano }}^{\mathrm{w}} \tilde{\mu}_{e}^{\mathrm{w}}
\tag{23}
$$

where we have assumed that the substrate $S$ is a bulk piece of metal, so that the electrochemical potential of their core ions, $\tilde{\mu}_{S}^{\mathrm{w}}$, remains unchanged upon formation of the nanostructure.

![](./images/811885237607858176_4.jpg)

Fig. 2. Scheme of the excess of free energy of a metal cluster as function of the number of atoms at two different overpotentials.

Since we will assume that neutral atoms are transferred, we have that $\Delta N_{M}^{\mathrm{r}}=-N_{M}$, $\Delta N_{e}^{\mathrm{r}}=-zN_{M}$ and $\Delta N_{e,\mathrm{nano}}^{\mathrm{w}}=zN_{M}$ so that the change in the transform $\tilde{G}$ will be given by

$$
\Delta \tilde{G}=\Delta G_{\mathrm{nano}}-N_{M} \mu_{M}+z N_{M}\left(\tilde{\mu}_{e}^{\mathrm{r}}-\tilde{\mu}_{e}^{\mathrm{w}}\right) \tag{24}
$$

where $\Delta G_{\text{nano}}$ is the free energy change of the system, given by $\Delta G_{\text{nano}}=\Delta U_{\text{nano}}+p \Delta V_{\text{nano}}-T \Delta S_{\text{nano}}$ and the term $(\tilde{\mu}_{e}^{\mathrm{r}}-\tilde{\mu}_{e}^{\mathrm{w}})$ defines the potential difference between the w and r electrode $e(\Psi_{S}-\Psi_{M})$, as long as a piece of the same metal $M_{2}$ is attached at the ends of both electrodes. As pointed out above, since the r electrode is made of the same material $M$ being deposited on $S$, we will denote $(\Psi_{S}-\Psi_{M})$ as an overpotential $\eta$.

If a single $M$ atom is transferred between r and s $(N_{M}=1)$, $\Delta G_{\text{nano}}$ corresponds to the chemical potential of the $M$ atoms on $S$, $\mu_{M/S}$ and we get:

$$
\Delta \tilde{G}=\mu_{M/S}-\mu_{M}+z e \eta \tag{25}
$$

The equilibrium condition $\Delta \tilde{G}=0$ leads as before to Eq. (3).

This second procedure employed to derive the relationship between free energy and potential difference may be easily applied to calculate the free energy change related to the transfer of the $N$ adatoms building the nanostructure from the w to the r electrode at a constant potential difference. In this case, the free energy change related to cluster formation at a constant overpotential $\eta$ will be given by

$$
\Delta G(N)=\left[\left(G^{M/S}-G_{S}\right)-N_{M} \mu_{M}\right]+N z e \eta \tag{26}
$$

where $G^{M/S}$ is the free energy of the nanostructure and it closest environment and $G_{S}$ is the free energy of this environment previous to the formation of the nanostructure.

Eq. (26) is the one currently used to analyze cluster formation. The quantity in the parenthesis, $[(G^{M/S}-G_{S})-N_{M} \mu_{M}]$ is an excess of free energy, say $\Phi(N)$, that in the case of a cluster on a surface of its same nature (say a Cu cluster on a Cu surface) is always positive. This is no longer the case for nanostructures in defects. To understand this, we must remember that $\Phi(N)$ is connected to the occurrence of interface boundaries. In the case of a growing cluster on a surface of its same nature, cluster growth is accompanied by the increase of its boundaries with an empty environment, with the concomitant increase of $\Phi(N)$. Being $\Phi(N)$ a monotonic growing function of $N$, the function in Eq. (26) is only employed when $\eta<0$ to find critical nucleus sizes. The situation is depicted qualitatively in Fig. 2, where $\Delta G(N)$ is plotted.

![](./images/811885237607858176_5.jpg)

Fig. 3. Scheme of the excess of free energy as function of the number of deposited atoms for the case of metal growth in a nanocavity. It is assumed that the interaction of the deposited atoms with the concave substrate is stronger than the interaction of the adsorbate atoms among themselves. It is also assumed that further wetting of the flat substrate is less favorable than the interaction between adatoms, so that cluster growth occurs.

However, in the case of nanostructures $\Phi(N)$ may be negative in those cases where the interaction with the substrate is more suitable than the interactions between the atoms of the deposit. Thus, in these cases an analysis of Eq. (26) will also make sense for $\eta>0$.

Let us consider first the hypothetical case where the atoms in the nanocavity interact with the substrate more strongly than with each other. At low coverages, we can assume that the atoms behave independently and the energy excess can be written as

$$
\Phi(N) \approx-\sigma_{\mathrm{exc}} N \tag{27}
$$

where $\sigma_{\mathrm{exc}}$ is a positive quantity representing the absolute value of the excess of binding energy per atom.

If we insert the latter equation into Eq. (26) we get:

$$
\Delta G(N) \approx \Phi(N)+N z e \eta=\left(z e \eta-\sigma_{\mathrm{exc}}\right) N \tag{28}
$$

Thus, depending on the sign of the terms in the parenthesis this function predicts a linear increase or decrease of $\Delta G(N)$. If the overpotential is such that $\eta>(\sigma_{\mathrm{exc}}/ze)$, it predicts that all the $M$-type atoms should disappear from the surface. On the other hand, if $\eta<(\sigma_{\mathrm{exc}}/ze)$, further atom deposition is predicted. The latter situation will of course change for some $N$, since Eq. (27) is an approximation valid only at low coverage degrees, but the main point we want to stress is that nanocavity decoration can in principle be analyzed via (26) with positive overpotentials. The situation for metal growth in a nanocavity where the interaction of the adsorbate with the concave substrate is stronger than the interaction of the adsorbate with itself, is illustrated qualitatively in Fig. 3. It is also assumed that further wetting of the flat substrate is less favorable than the interaction between adatoms, so that cluster growth takes place as found in experiments [6].

### 3. Computer simulations

In order to investigate by means of computer simulations how the holes generated by the potential pulses described in Section 1 are decorated by foreign adatoms, an atomistic model was employed.

The interaction between the particles of the system was calculated according to the Embedded Atom Method (EAM). In the case of the decoration of nanoholes on $\mathrm{Au}(111)$, the parameterization was that of Barrera et al. [13]. This reproduces adequately the $(1 \times 1)$ structure of the $\mathrm{Cu}$ monolayer (upd) on $\mathrm{Au}(111)$ observed experimentally [14]. In the case of the deposition of $\mathrm{Ag}$ on $\mathrm{Au}(111)$, the potential employed was that of Foiles et al. [15]. We will show

![](./images/811885237607858176_6.jpg)
![](./images/811885237607858176_7.jpg)

Fig. 4. Cavity filling on Au(1 1 1) with different adsorbates. (a) Shows the height of the cavity and the decoration of a Au(1 1 1) cavity with Cu atoms as a function of their chemical potential. (b) Shows the cavity height and the decoration of a Au(1 1 1) cavity with Ag atoms as a function of their chemical potential.

that this potential reproduces a number of important features of the experimental system, like the formation of mono and bi layers previous to the deposition of the bulk metal.

A set of simulations were accomplished by means of a Grand Canonical Monte Carlo method [5]. In this approach, the chemical potential $\mu$ of the adsorbate atoms (Cu or Ag), the volume of the simulation box $V$ and the temperature $T$ were fixed as parameters. With this setup, we attempt to simulate electrochemical deposition conditions, where the chemical potential of the deposited atoms are varied by changing the electrochemical potential of the electrons in the working electrode. The energy of the system and the number of adsorbate atoms fluctuated according to the different types of events allowed:

(1) Particle displacement (Cu, Ag or Au), using as acceptance ratio:
$$
W_{i \rightarrow j}=\min \left(1, \exp \left(-v_{i j} / k T\right)\right) \tag{29}
$$
where $v_{i j}$ is the change of potential energy related to the configuration change $i \rightarrow j$.

(2) Insertion of an adsorbate atom. A particle is inserted in the simulation box at a random position and the new configuration is accepted according to
$$
W_{N \rightarrow N+1}=\min \left(1, \frac{V}{\Lambda^{3}(N+1)} \exp \left(\left(\mu-\Delta v_{N+1, N}\right) / k T\right)\right) \tag{30}
$$
$V$ is the volume that can be accessed by the particles created, $\Lambda=\sqrt{\left(h^{2} / 2 \pi m k T\right)}$ is the de Broglie thermal wavelength and $\Delta v_{N+1, N}=v_{N+1}-v_{N}$ is the potential energy difference related to the creation attempt of a particle.

(3) Removal of an adsorbate atom. An adsorbate atom chosen at random is removed from the system and the new configuration is accepted according to
$$
W_{N \rightarrow N-1}=\min \left(1, \frac{\Lambda^{3} N}{V} \exp \left(\left(-\mu-\Delta v_{N-1, N}\right) / k T\right)\right) \tag{31}
$$
with $\Delta v_{N-1, N}=v_{N-1}-v_{N}$.

The surface of the substrate was represented by a six atomic layers thick slab, four of which were mobile. The remaining two were fixed to the bulk atomic positions. The remaining dimensions of the system were $L_{x}=49.96 \AA$ and $L_{y}=57.69 \AA$. Periodic boundary conditions were applied in the $x-y$ direction. The hole was $22 \AA$ wide, with a depth of three atomic layers. Other comparative studies considered $33 \AA$ and $40 \AA$ wide holes.

The systems considered were the filling of a cavity on a Au(1 1 1) surface by Cu and Ag atoms respectively, with the results shown in Fig. 4. The height of the defect is given there as a function of the chemical potential, along with some snapshots showing some sample configurations of the simulations. In the early stages of the simulation, both systems present a decoration of the cavity that starts at the highly coordinated sites. This will be discussed in more detail below.

The first system is similar to one considered previously [16], and is revisited here in order to make a straightforward comparison with the Ag/Au(1 1 1) system. Important differences are evident between both systems in the way in which defects are decorated, as well as in the corresponding energetics. To gain a proper understanding of the processes found upon the filling of the nanocavity, it is interesting to analyze first how is the interaction of the deposited metal monolayer with the substrate in comparison with the interaction of the same metal in the bulk. A measure for the stability of an adlayer relative to the bulk metal can be obtained in terms of the excess of binding energy per adatom of the adatoms in the monolayer $\Delta u^{M / S}$, that can be defined as
$$
\Delta u^{M / S}=\frac{U^{M / S}}{N_{M}}-u_{M}^{\text {bulk }} \tag{32}
$$
where $U^{M / S}$ is the binding energy of the adatoms in the monolayer defined above (see Eq. (4)) and $U_{M}^{\text {bulk }}$ is the binding energy of bulk $M$ atoms. Since $U^{M / S}$ and $U_{M}^{\text {bulk }}$ are usually defined as the energy of the atoms in the solid system minus the energy of the free atoms, they are negative quantities. Thus, a negative value of $\Delta u^{M / S}$ indicates that the atoms are more stable in the monolayer than in its own bulk metal lattice, while a positive value indicates that they are less stable in the monolayer.

Table 1 shows $\Delta u^{M / S}$ values for adatoms in a monolayer for the two metal systems analyzed in the present work, using EAM potentials in different simulation methods, as can be found in the literature [9,17]. The second and the fourth columns correspond to

<table>
<caption>Table 1
Excess of binding energy $\Delta u^{M / S}$ and binding energies $U^{M / S}$ for adatoms in a monolayer for the systems considered in the present work. The cohesive energies of Cu and Ag are $u_{\mathrm{Cu}}^{\text {bulk }}=-3.54 \mathrm{eV}$ and $u_{\mathrm{Ag}}^{\text {bulk }}=-2.85 \mathrm{eV}$, respectively.</caption>
<thead>
<tr>
<th>System</th>
<th>$\Delta u^{M / S}(eV)^{a}$</th>
<th>$\Delta u^{M / S}(eV)^{b}$</th>
<th>$U^{M / S}/N(eV)^{a}$</th>
<th>$U^{M / S}/N(eV)^{b}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cu/Au(1 1 1)</td>
<td>0.23</td>
<td>0.14</td>
<td>−3.22</td>
<td>−3.35</td>
</tr>
<tr>
<td>Ag/Au(1 1 1)</td>
<td>−0.10</td>
<td>−0.11</td>
<td>−2.87</td>
<td>−2.92</td>
</tr>
</tbody>
</table>

$^{a}$ Lattice dynamics, six lattice planes relaxation, according to Oviedo et al. [9].
$^{b}$ Off-Lattice Monte Carlo simulation, according to Rojas [17].

lattice dynamics simulations, where the positions of the six surface lattice planes are relaxed, but a $1 \times 1$ structure is assumed for the adlayer [9]. The third and the fifth columns correspond to off-lattice Monte Carlo (MC) simulations, where atoms may take arbitrary positions in space [17]. These results should be the most accurate ones. For Ag/Au(1 1 1) the results are practically the same for all the simulation methods employed, pointing out that the Ag monolayer on Au(1 1 1) should be more stable than bulk Ag. This is in rule with the experimental fact that Ag presents underpotential deposition on Au(1 1 1) [18]. On the other hand, for the Cu/Au(1 1 1) system, always positive values are obtained, indicating that the Cu monolayer on Au(1 1 1) should be less stable than bulk Cu. This is in rule with first principle predictions [19,20], but in contrast with the experimental observation of Cu on Au(1 1 1). The reason for this apparent contradiction can be explained by the determining role played by anions in the Cu upd phenomenon, as found experimentally [21,22] and discussed in previous theoretical work [20]. From the third and the fourth rows in Table 1, it is evident that the off-lattice MC results yield the less positive results, denoting that an additional stabilization is allowed by the off-lattice simulations with respect to the imposition of a $1 \times 1$ structure. In fact, these simulations show that the Cu overlayer becomes more compact than the $1 \times 1$ structure, with the concomitant decrease in its binding energy.

In summary, from the previous discussion it can be stated that the Cu atoms interact with each other more strongly than with the Au(1 1 1) surface, while the opposite is true for the Ag atoms. Thus, according to the knowledge than we have from metal growth [23], we expect a "Volmer-Weber growth" in the first case, with the formation of clusters, and a "Frank-van der Merwe" or layer-by-layer growth in the second, since the misfit between Ag and Au atoms is practically negligible. Going back to Fig. 4, we see that the two systems analyzed behave as expected.

It must be taken into account that besides the differences in the energetics of both systems, there is also an important crystallographic difference, since while the Cu/Au system presents a negative misfit, in the Ag/Au system the misfit is negligible. The size difference between the substrate and adsorbate in the first of these systems allows that the adsorbate atoms present a high coordination with those of the substrate, with smaller steric hindrances at the deposition process. On the other hand, in the system Ag/Au the atomic sizes are similar, the coordination of Ag atoms with the substrate is smaller, so that in the deposition process it is not expected that the Ag atoms would have a high coordination with the Au atoms unless an Ag atom displaces or replaces an Au atom.

Turning now to the particular features observed for each system, in the Cu/Au(1 1 1) system we find that after the decoration of the bottom of the cavity, the cavity is filled at once in the vicinity of the bulk Cu binding energy, which is $-3.61$ eV for the present EAM potentials. A canonical simulation of Cu deposition on Cu surfaces performed by Rojas [17] yielded an average value of $-3.581$ eV for the Cu binding energy at 300 K.

Fig. 5 shows the number of deposited Cu atoms as a function of the chemical potential of the Cu atoms.

A number of arrest and shoulders is observed in the curve, indicating that some structures are particularly stable as deposition proceeds. In order to visualize different stages of hole decoration, numbered arrows denote points in the plot that correspond to snapshots of the simulation shown in Fig. 5a. The point labeled with 1 corresponds to the decoration of the border of the bottom part of the cavity. Point 2 indicates the situation where the bottom of the cavity is covered by a Cu layer. Point 3 corresponds to the filling of the cavity up to the surface level. Points 4 and 5 indicate the formation of the first and second layer over the surface level.

![](./images/811885237607858176_8.jpg)

It is also interesting to analyze the average binding energy per atom of our GCMC simulations:

$$
u^{M / S}=\frac{\overline{U^{M / S}-U_{S}}}{\bar{N}} \quad (33)
$$

as a function of the chemical potential, as shown in Fig. 6. When the decoration of the cavity starts, the high coordination of the deposited Cu atoms yields structures that are energetically more stable than the bulk Cu deposit. The binding energy per atom then increases, with a subsequent decrease in the region where the cavity becomes filled (point 3). At this point, $u^{M / S}=-3.57 \pm 0.01$ eV, in good agreement with the results of Rojas in a canonical simulation [17] ($-3.581$ eV). Two steps are later evident, corresponding to points 4 and 5, when one or two layers are formed above the level of the surface.

The phenomenon of Cu electrodeposition in a Au(1 1 1) nanocavity is particularly suited to perform an analysis of cluster growth as discussed in Section 2. Returning to Eq. (26):

$$
\Delta G(N)=\Phi+N z e \eta \quad (34)
$$

This equation tells us that once the excess quantity $\Phi=(G^{M / S}-$ $G_{S})-N G_{\text {bind }}^{M}$ is known, the relative stability of different structures at different overpotentials could be analyzed from its extrema. The

![](./images/811885237607858176_9.jpg)

Fig. 6. Average binding energy per atom as a function of the chemical potential for the simulation of Cu deposition in a Au(1 1 1) nanocavity.

quality of this prediction may then be contrasted with the results of the simulations that are thermodynamically "exact", in the sense that they contain both energetic and entropic contributions. The term $\Phi$ may be written as

$$
\Phi=\Delta U^{M / S}-T \Delta S^{M / S}
\tag{35}
$$

where $\Delta U^{M / S}=N \Delta u^{M / S}=\left(U^{M / S}-U_{S}\right)-N U_{M}^{\text {bulk }}$ is the excess of binding energy of the metal on the substrate $S$ with respect to the bulk binding energy of the metal $M$ and $\Delta S^{M / S}$ is the corresponding excess of entropy. As we stated above, the bulk binding energy is close to $-3.581 \mathrm{eV}$. Both quantities are a function of $N$, the number of atoms in the nanostructure. Since the entropic contribution $\Delta S^{M / S}$ is not known, $\Phi$ cannot be calculated exactly, so that we approximate this quantity by $\Delta U^{M / S}$. Thus, what we can construct are not $\Delta G(N)$ but $\Delta U^{M+S}+N z e \eta$ vs. $N$ curves, as presented in Fig. 7. These curves are shown for the deposition of the Cu adatoms in the $\operatorname{Au}(111)$ nanocavity in Fig. 7 at $\eta=0$ and other overpotentials. Comparison of these curves with the results of the Grand Canonical simulation presented in Fig. 5 show that this analysis slightly underestimates the effect of overpotential. In fact, the results of $4 \mathrm{a}$ and 5 clearly show that an excess chemical potential of $0.04 \mathrm{eV}$ $(\Delta \mu=0.04 \mathrm{eV})$ is enough to make the cluster grow up to the first overlayer (state 4). However, it is apparent from Fig. 7 that at a value of $z e \eta$ of $-0.04 \mathrm{~V}$ with respect to bulk deposition, the most stable structure is that of the filled nanocavity (state 3). Similarly, the curve for $z e \eta=-0.10 \mathrm{eV}$ in Fig. 7 shows a local minimum around $N \approx 220$, which corresponds to the formation of the first overlayer (snapshot 4 in Fig. 5). However, all GCMC simulations performed at an excess chemical potential of $0.10 \mathrm{eV}$ lead to the growth of the bulk Cu deposit. In other words, although the purely energetic analysis yields the correct qualitative picture concerning the sequential formation of the structures 3,4 and 5, it underestimates the effect of the application of an overpotential.

![](./images/811885237607858176_10.jpg)

Fig. 7. Excess energy vs. number of adatoms for the adsorption of Cu atoms in a $\mathrm{Au}(111)$ nanocavity at different overpotentials $\eta$. The number close to the curves denote the value of $z e \eta$ in $\mathrm{eV}$, with $z=2$, and $e$ the electronic charge.

![](./images/811885237607858176_11.jpg)

Fig. 8. Number of deposited Ag atoms as a function of the chemical potential for decoration of a nanocavity on a $\mathrm{Au}(111)$ surface. (b) Snapshots of the simulation showing the different stages of hole decoration, corresponding to the numbers of part (a). The chemical potentials were $1-\mu_{\mathrm{Ag}}=-3.155 \mathrm{eV}, 2-\mu_{\mathrm{Ag}}=-3.12 \mathrm{eV}$, $3-\mu_{\mathrm{Ag}}=-3.03 \mathrm{eV}, 4-\mu_{\mathrm{Ag}}=-3.00 \mathrm{eV}, 5-\mu_{\mathrm{Ag}}=-2.87 \mathrm{eV}$.

### 4. Ag/Au(111) system

The number of Ag atoms in the system as a function of the chemical potential of $\mathrm{Ag}$ atoms, $\mu_{\mathrm{Ag}}$, is shown in Fig. 8. A number of steps become evident, which are characteristic for the occurrence of different surface structures. Some typical points of the simulation were selected, whose snapshots are shown in Fig. 8. Point 1 corresponds to a situation where the decoration takes places along steps, yielding 1-d structures. Point 2 corresponds to the formation of a first overlayer at the bottom of the cavity. Point 3 corresponds to the formation of a second overlayer at the bottom of the cavity. Point 4 corresponds to a point where the cavity has been filled, along with the formation of an Ag monolayer on the $\operatorname{Au}(111)$ surface. Point 5 corresponds to the formation of a second monolayer on the $\operatorname{Au}(111)$ surface.

The occurrence of a fraction of an Ag monolayer at the bottom of the cavity on $\operatorname{Au}(111)$ in point $2\left(\mu_{\mathrm{Ag}}=-3.125 \mathrm{eV}\right)$ is a unique feature of a nanosystem. That is, a finite deposit of $\mathrm{Ag}$ is obtained, at

![](./images/811885237607858176_12.jpg)

Fig. 9. Average binding energy per atom as a function of the chemical potential for the simulation of Ag deposition in a Au(1 1 1) nanocavity.

chemical potentials where the Ag monolayer is unstable, it appears yet at -3.015 eV. Thus, the existence of the nanocavity allows a shift of -0.11 eV in the chemical potential at which an Ag layer occurs on the surface.

The binding energy per Ag atom is shown as a function of $\mu_{\text{Ag}}$ in Fig. 9. As in the case of the cavity filled with Cu, the binding energy of the first Ag atoms decorating the cavity lay well below the bulk binding energy of the metal ($U_{\text{Ag}}^{\text{bulk}}=-2.85$ eV). However, in this case the excess energy is considerably larger, reaching values as large as -0.35 eV. It is interesting to analyze this information in the light of some previous calculations for the binding energy of an Ag monolayer on Au(1 1 1), as reported in Table 1. We presented there results of lattice dynamics [9] and Monte Carlo canonical simulations. The latter results should be the most comparable with the present ones, since they were obtained allowing for relaxation of the whole substrate. Since the results of Table 1 were obtained for a monolayer, they should be compared with the energies of the structures occurring between $\mu_{\text{Ag}}=-3.0151$ eV and $\mu_{\text{Ag}}=-2.875$ eV, where an Ag overlayer occurs on the metal surface. We obtained in this region an average value of $\overline{(U^{M/S}-U_{S})/N}=-2.9211\pm 0.0004$ eV, in good agreement with Rojas [17]. Going back to the nanostructure originated at point 2 of Fig. 8, an average between $\mu_{\text{Ag}}=-3.090$ eV and $\mu_{\text{Ag}}=-3.035$ eV yields a binding energy of $\overline{(U^{M/S}-U_{S})/N}=-3.058\pm 0.002$ eV. That is, the binding energy per Ag atom in the nanocavity shows an excess of -0.14 eV with respect to the Ag monolayer. Comparison of this value with the shift of chemical potential of -0.11 eV suggests that the reason for the additional stability of the Ag layer in the nanocavity is mainly energetic.

Concerning the formation of the Ag monolayer, in the present simulations it is found to be stable between $\mu_{\text{Ag}}=-3.015$ and $\mu_{\text{Ag}}=-2.875$ eV, previous to the formation of the second Ag monolayer. This result would suggest in a first analysis that the monolayer is -0.14 eV more stable than the bilayer. However, the analysis of the data in Fig. 9 shows an energy difference of ca. -0.06 eV between both structures in favor of the monolayer. Since the entropic status of the monolayer is not very different from that of the bilayer, another explanation must be sought for the delayed formation of the monolayer. Analogously to 3-d nucleation and growth phenomena, the formation of the bilayer on the top of a perfect monolayer involves the formation of a critical nucleus, with the concomitant overpotential. In the 2-d case, the critical nucleus size $N_{\text{crit}}$ can be shown to be related to the overpotential $|\eta|$ according to the equation [23]:

$$
N_{\text{crit}}=\frac{b\Omega \zeta^{2}}{(ze|\eta|)^{2}} \tag{36}
$$

where $b$ is a geometrical factor relating the perimeter of the nucleus to its area ($b=\pi$ for a circular cluster, $b=4$ for a square cluster, $b=3.46...$ for an hexagonal one), $\Omega$ is the atomic area, and $\zeta$ is the specific edge energy. For the present system, $\Omega=7.24\mathring{\text{A}}^{2}$/atom and $\zeta$ can be estimated from the step formation energy of Ag islands on Ag(1 1 1), yielding $\zeta=0.0809$ eV/$\mathring{\text{A}}$, so that for an excess of chemical potential $\Delta \mu=ze|\eta|=0.08$ eV in Eq. (36) we get $N_{\text{crit}}=23-30$. This estimation indicates that an important fluctuation in the number of particles of the system is required in order to overcome the free energy barrier required for the growth of the second Ag overlayer on the surface.

## 5. Energy distribution

In a Grand Canonical simulation both the number of particles $N$ and the energy of the system $U$ fluctuate. Thus, it is illustrative to analyze the distribution of energy per particle $u^{M/S}$ along the simulation, since this gives an idea of the energy of the species involved at each stage of the simulation. With this purpose, histograms were constructed with the frequencies $f_{\text{u}}$ with which a given value of $u^{M/S}$ was observed. Two types of histograms were constructed. A first type, that we will call global histograms, where constructed by sampling the whole simulation between the upper and lower values of chemical potential, say $\mu_{\text{up}}$ and $\mu_{\text{low}}$. One of these histograms is shown in Fig. 10 for Cu deposition in Au(1 1 1) cavities as a full line. The others were partial histograms, where the sampling was made in a restricted region of chemical potential where a particular decoration of the cavity was found. These are also reported in Fig. 10.

The global histogram, shown in full line in Fig. 10, presents four peaks.

Seven partial histograms where constructed, where each region was chosen according to the following phenomena taking place:

![](./images/811885237607858176_13.jpg)

Fig. 10. Energy histograms for Cu deposition inside a Au(1 1 1) cavity. The thick full line shows the global histogram, while the remaining ones show the partial contributions in different ranges. (——) Wall decoration of the defect ($-3.7$ eV$<\mu_{\text{Cu}}<-3.64$ eV); ($\cdots\cdots$) decoration of the bottom of the defect ($-3.635$ eV$<\mu_{\text{Cu}}<-3.610$ eV); ($\cdots\cdots$) filling of the defect ($-3.605$ eV$<\mu_{\text{Cu}}<-3.600$ eV); ($\cdots\cdots$) first layer on the defect over the Au surface ($-3.595$ eV$<\mu_{\text{Cu}}<-3.570$ eV); ($\cdots\cdots$) second layer on the defect over the Au surface ($-3.565$ eV$<\mu_{\text{Cu}}<-3.550$ eV); ($\cdots\cdots$) third layer on the defect over the Au surface ($-3.545$ eV$<\mu_{\text{Cu}}<-3.535$ eV); ($\cdots$) fourth layer on the defect over the Au surface ($\mu_{\text{Cu}}<-3.530$ eV).

![](./images/811885237607858176_14.jpg)

Fig. 11. Energy histograms for Ag deposition inside a Au(111) cavity. The grey full line shows the global histogram, while the remaining ones show the partial contributions in different $\mu_{\text{Ag}}$ ranges. (--- ---) Wall decoration of the defect $(-3.35\,\text{eV}<\mu_{\text{Cu}}<-3.12\,\text{eV})$; $(\boldsymbol{\cdot \cdot \cdot})$ formation of the first Ag layer covering the bottom of the cavity $(-3.155\,\text{eV}<\mu_{\text{Ag}}<-3.01\,\text{eV})$; $(\boldsymbol{\cdot - \cdot - \cdot})$ formation of the first Ag layer covering the bottom of the cavity $(-3.005\,\text{eV}<\mu_{\text{Ag}}<-2.985\,\text{eV})$; $(\boldsymbol{\cdot - \cdot - \cdot -})$ formation of the first Ag monolayer outside the cavity $(-2.98\,\text{eV}<\mu_{\text{Ag}}<-2.87\,\text{eV})$; $(---)$ formation of the second Ag monolayer outside the cavity $(-2.865\,\text{eV}<\mu_{\text{Ag}}<-2.855\,\text{eV})$.

- Wall decoration of the defect. From $\mu_{\text{Cu}}=-3.7\,\text{eV}$ to $\mu_{\text{Cu}}=-3.64\,\text{eV}$.
- Decoration of the bottom of the defect. From $\mu_{\text{Cu}}=-3.635\,\text{eV}$ to $\mu_{\text{Cu}}=3.610\,\text{eV}$.
- Filling of the defect. From $\mu_{\text{Cu}}=-3.605\,\text{eV}$ to $\mu_{\text{Cu}}=-3.600\,\text{eV}$.
- First layer on the defect over the Au surface. From $\mu_{\text{Cu}}=-3.595$ to $\mu_{\text{Cu}}=-3.57\,\text{eV}$.
- Second layer on the defect over the Au surface. From $\mu_{\text{Cu}}=-3.565$ to $\mu_{\text{Cu}}=-3.550\,\text{eV}$.
- Third layer on the defect over the Au surface. $\mu_{\text{Cu}}=-3.545\,\text{eV}$ to $\mu_{\text{Cu}}=-3.535\,\text{eV}$.
- Fourth layer on the defect over the Au surface. Just at $\mu_{\text{Cu}}=-3.530\,\text{eV}$.

On the other hand, the histograms for Ag deposition inside the Au(111) cavity presented a much more well defined structure, as shown in Fig. 11.

The global histogram presents four well defined peaks (at $\mu_{\text{Ag}}=-3.06\,\text{eV}, -2.92\,\text{eV}, -2.87\,\text{eV}$ and $-2.84\,\text{eV}$), while partial histograms were constructed on the basis of five regions, depending on the characteristics of the deposit:

- Decoration of the walls of the cavity. From $\mu_{\text{Ag}}=-3.35$ to $\mu_{\text{Ag}}=-3.12\,\text{eV}$.
- Formation of the first Ag layer covering the bottom of the cavity. From $\mu_{\text{Ag}}=-3.115$ to $\mu_{\text{Ag}}=-3.01\,\text{eV}$.
- Formation of the second Ag layer covering the bottom of the cavity. From $\mu_{\text{Ag}}=-3.005$ to $\mu_{\text{Ag}}=-2.985\,\text{eV}$.
- Formation of the first Ag monolayer outside the cavity. From $\mu_{\text{Ag}}=-2.98$ to $\mu_{\text{Ag}}=-2.87\,\text{eV}$.
- Formation of the second Ag monolayer outside the cavity. From $\mu_{\text{Ag}}=-2.865$ to $\mu_{\text{Ag}}=-2.855\,\text{eV}$.

The most remarkable difference between the two systems considered here is the sharp peak observed in the case of the Ag/Au(111) system, corresponding to the formation of the monolayer. This is a clear indication for the formation of a new phase, where the binding energy should have exactly one value.

The general conclusion that can be drawn from the histogram analysis performed for the two systems considered here is that the different nanofeatures of defect decoration are reflected in the different contributions to the histograms. A more extensive statistical sampling of the different systems is desirable to gain more detailed information on them, and will be undertaken in the future with more powerful computational tools.

## 6. Conclusions

We have developed a thermodynamic framework for the analysis of electrochemical nanocavity decoration that leads to a qualitative understanding of the processes taking place in terms of the interactions of the metals involved in this process.

We then studied comparatively the decoration of nanocavities on Au(111) by Cu and Ag atoms using Grand Canonical Monte Carlo simulations. Depending on the interaction between the adsorbate and the substrate as compared with the adsorbate-adsorbate interactions, the deposit may grow defining a cluster over the surface level (Cu/Au(111)) or heal the damage on the surface with the subsequent formation of a monolayer(Ag/Au(111)). In the former case, Cu deposition remains confined to the defects generated on the surface, since the formation of clusters on the Au(111) is disfavored. On the contrary, Ag deposition on the flat Au(111) surface occurs after the filling of the nanocavity.

## Acknowledgements

Financial support from CONICET, Secyt UNC, and Program BID 1728/OC-AR PICT No. 946 are gratefully acknowledged. N.L. thanks CONICET for a fellowship.

## Appendix A. Supplementary data

Supplementary data associated with this article can be found, in the online version, at doi:10.1016/j.electacta.2008.12.013.

## References

[1] D.M. Kolb, F.C. Simeone, Electrochim. Acta 20 (2005) 2989.
[2] N.B. Luque, E.P.M. Leiva, Electrochim. Acta 20 (2005) 3161.
[3] D.M. Kolb, F.C. Simeone, Curr. Opin. Solid State Mater. Sci. 9 (2005) 91.
[4] M.M. Mariscal, E.P.M. Leiva, Chapter 2: Computer Simulations of Electrochemical Low-dimensional Metal Phase Formation, in: Electrocrystallization in Nanotechnology, 1st ed., Wiley-VCH, Weinheim, 2006, p. 30.
[5] W. Li, G.S. Hsiao, D. Harris, R.M. Nyffenegger, J.A. Virtanen, R.M. Penner, J. Phys. Chem. 100 (1996) 20103.
[6] X.H. Xia, R. Schuster, V. Kirchner, G. Ertl, J. Electroanal. Chem. 461 (1999) 102.
[7] T. Solomun, W. Kautek, Electrochim. Acta 47 (2001) 679.
[8] E.P.M. Leiva, Electrochim. Acta 41 (1996) 2185.
[9] O.A. Oviedo, E.P.M. Leiva, M.I. Rojas, Electrochim. Acta 51 (2006) 3526.
[10] See for example discussion in chapter 2 of E. Budevski, G. Staikov, W.J. Lorenz, Electrochemical Phase Formation and Growth, VCH, Federal Republic of Germany, 1996.
[11] T.L. Hill, Nano Lett. 1 (2001) 273.
[12] H.B. Callen, Thermodynamics and an Introduction to Thermostatistics, 2nd ed., John Wiley and Sons, New York, 1985.
[13] G.D. Barrera, R.H. Tendler, E.P. Isoardi, Model. Simul. Mater. Sci. Eng. 8 (2000) 389.
[14] M.G. Del Pópolo, E.P.M. Leiva, W. Schmickler, J. Electroanal. Chem. 518 (2002) 84.
[15] S.M. Foiles, M.I. Baskes y, M.S. Daw, Phys. Rev. B 33 (1986) 7983.
[16] N.B. Luque, M.G. Del Pópulo, E.P.M. Leiva, Surf. Sci. 571 (2004) L319.
[17] M.I. Rojas, Surf. Sci. 569 (2004) 76.
[18] M.J. Esplandiu, M.A. Schneeweiss, D.M. Kolb, Phys. Chem. Chem. Phys. 1 (1999) 4847.
[19] C. Sánchez, E.P.M. Leiva, Electrochim. Acta 45 (1999) 691.
[20] C.G. Sánchez, E.P.M. Leiva, J. Kohanoff, Langmuir 17 (2001) 2217.
[21] Z. Shi, S. Wu, J. Lipkowski, Electrochim. Acta 40 (1995) 9.
[22] J. Hotlos, O.M. Magnussen, W.J. Behm, Surf. Sci. 335 (1995) 129.
[23] E. Budevski, G. Staikov, W.J. Lorenz, Electrochemical Phase Formation and Growth, VCH, Federal Republic of Germany, 1996.