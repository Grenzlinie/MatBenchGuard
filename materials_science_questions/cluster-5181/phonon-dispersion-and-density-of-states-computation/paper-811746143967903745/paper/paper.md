# Lattice dynamics with indirect ionic interactions

G. D. Mahan
Solid State Division, Oak Ridge National Laboratory, P.O. Box 2008, Oak Ridge, Tennessee 37831-6032
and Department of Physics and Astronomy, University of Tennessee, Knoxville, Tennessee 37996-1200

M. Mostoller
Solid State Division, Oak Ridge National Laboratory, P.O. Box 2008, Oak Ridge, Tennessee 37831-6032

(Received 7 August 1989; revised manuscript received 29 November 1989)

Lattice dynamics are calculated for KCl, KBr, RbCl, and AgBr. The following short-range forces are included: first-neighbor direct, deformation dipole, and indirect ionic interactions. The indirect ionic interactions are a model of three-body forces. A least-squares fit of the theory to the experimental results provides numerical values for the three-body forces. They are quite large for the $Ag^{+}$ ion.

We report calculations of phonon frequencies for KCl, KBr, RbCl, and AgBr. The theory of lattice dynamics in insulators, particularly alkali halides, is a well-developed subject with a long history. $^{1-6}$ All theories contain the long-range Coulomb force plus several short-range forces. Two popular models are the shell model $^{1,2}$ and the deformation-dipole model. $^{3-6}$ Several models have also been proposed to account for three-body forces. $^{7-12}$

Recently we introduced a new model for the three-body forces. $^{10,11}$ It is not really a model but an exact description of the indirect interaction between two ions that have a third ion as a common neighbor. It is called the indirect ionic interaction $(I^{3})$. We showed that this indirect interaction could be represented by a force tensor. Symmetry relations reduced the number of parameters in the tensor down to a small number. These parameters were calculated using the local-density approximation (LDA), which showed that some of the parameters were negligibly small and could be ignored. $^{12}$

Here, we have combined the deformation-dipole $(D^{2})$ model with the $I^{3}$ model to calculate the lattice dynamics of four crystals with the rocksalt structure. Experimental values of the vibrational frequencies are available from neutron scattering. We have used these data to obtain a least-squares fit of the $D^{2}I^{3}$ model to the data. In this fashion we have found experimental values for the parameters, which are compared with those calculated previously using LDA.

Our calculation includes the long-range Coulomb interaction between ions plus the following short-range forces: first-neighbor central forces, first-neighbor deformation dipoles, and $I^{3}$. The deformation-dipole model and $I^{3}$ are linked together in a natural way. $^{13}$ The deformation dipole model includes the short-range polarization between neighboring pairs of ions. The $I^{3}$ interaction includes the forces between two ions that have a common first neighbor which is polarizable.

The relationship between the shell model and the deformation-dipole model is discussed in Refs. 2 and 6. They are similar for phonons at long wavelength, but differ at short wavelength. We also considered whether the $I^{3}$ interactions could be added to the shell model. Here the problem is that the shell model already includes some three-body forces. It proved difficult to decide which three-body forces were in $I^{3}$ and which were in the shell model.

Bilz and co-workers $^{8,9}$ introduced the concept of ion deformability. This is similar in spirit to $I^{3}$, although the mathematical formalism is different. They suggested that the ions $Ag^{+}$ and $Cu^{+}$ are particularly deformable, which would account for the peculiar lattice dynamics of their halides. We have used LDA to calculate the $I^{3}$ parameters for these two ions and find that they are indeed large. In some cases they are a factor of 10 larger than the similar parameters for alkali ions. Of the eight silver and copper halides, only three have the rocksalt structure. Of these, only AgBr has had the phonon spectra measured well enough to attempt a least-squares fit of our model to the data. Here we also find that the fitted $I^{3}$ parameters and deformation-dipole parameters for $Ag^{+}$ are large. Our calculations, both the ab initio LDA calculations and the least-squares fits to the data, support the hypothesis that the three-body forces are large for $Ag^{+}$.

## LATTICE DYNAMICS

Rocksalt lattices have two ions per unit cell: a cation of valence $Z$ and an anion of $-Z$. The dynamical matrix is real and has dimension six. Below we list the terms that are included in the dynamical matrix. They are listed in the order they were introduced historically. As we explain later, in the end we did not use them all.

(1) Short-range central forces between first and second neighbors. If $R$ is the vector between two neighbors, this term has the form

$$
V_{\mu v}=B \delta_{\mu v}+(A-B) R_{\mu} R_{v} / R^{2},
$$

$$
A=\frac{d^{2} V(R)}{d R^{2}}, \quad B=\frac{1}{R} \frac{d V(R)}{D r}.
$$

There are six parameters: $A_{+-}$ and $B_{+-}$ for first-neighbor interactions and $A_{++}, B_{++}, A_{--}$, and $B_{--}$ for second-neighbor interactions.

(2) Dipole-dipole interactions and dipole-induced-dipole interactions. Since the ions are charged, their vi- brations create oscillating dipoles that cause long-range forces. We take the ion charges to be integers. We also included the polarizability of individual ions. In Table I we provide a semiempirical table of polarizabilities. This is obtained by fixing the cation polarizability at its known value and then deducing the anion polarizability from the refractive index. $^{14}$ These values are similar to our earlier tabulation. $^{15}$ Lattice dynamics with forces (1) and (2) is commonly known as the "rigid-ion model."

(3) Deformation dipoles were introduced by Hardy and Karo (Refs. 4 and 5). An ion displacement will cause di- pole polarization on its neighboring ions. This phenomenon can be included as a term in the Hamiltoni- an that contains the local electric field $E$,

$$
H_{d d}=-e \sum_{j, \delta} \mathbf{E}_{j} \cdot \gamma_{j} \cdot\left(\mathbf{Q}_{j+\delta}-\mathbf{Q}_{j}\right) Z_{j+\delta}.
$$

The deformation-dipole tensor $\gamma$ is diagonal and has lon gitudinal $\gamma_{l}$ and transverse $\gamma_{t}$ terms. We have written this expression to include all forces between the neigh- bors. However, in (2) above we already included the dipole-dipole interactions resulting from ion displace-ments. One part of $\gamma$ is due to this dipolar interaction: The ion displaces $Q_{j+\delta}$ which makes a dipole $Z e Q$. There is an induced moment on ion $R_{j}$ from dipole in teractions of the form $\alpha \cdot \phi \cdot Q Z e$, where $\alpha$ is the polariza bility of ion $j$ and

$$
\phi_{\mu v}=\delta_{\mu v} / R^{3}-3 R_{\mu} R_{v} / R^{5}
$$

is the dipole tensor. In order to avoid double counting, we subtract this dipolar part out of the deformation di- pole. We call this process renormalization. Effectivelywe replace the deformation dipole by the quantity $\bar{\gamma}$  defined as

$$
\bar{\gamma}=\gamma-\alpha \cdot \phi,
$$

$$
\bar{\gamma}_{t}=\gamma_{t}-\alpha / R^{3},
$$

$$
\bar{\gamma}_{l}=\gamma_{l}+2 \alpha / R^{3},
$$

where $R$ is the first-neighbor distance. This definition of y brings us into accord with Hardy and Karo. Their definition of the deformation dipole is actually $e \bar{\gamma}$. Lat tice dynamics with interactions (1)-(3) is called the "deformation-dipole model."

<table>
<caption>TABLE I. Semiempirical polarizabilities.</caption>
<thead>
<tr>
<th>Salt</th>
<th>$\alpha_{+}$ (Å$^{3}$)</th>
<th>$\alpha_{-}$ (Å$^{3}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>LiF</td>
<td>0.03</td>
<td>0.91</td>
</tr>
<tr>
<td>NaF</td>
<td>0.15</td>
<td>0.9611</td>
</tr>
<tr>
<td>KF</td>
<td>0.81</td>
<td>0.97</td>
</tr>
<tr>
<td>RbF</td>
<td>1.35</td>
<td>1.14</td>
</tr>
<tr>
<td>LiCl</td>
<td>0.03</td>
<td>2.94</td>
</tr>
<tr>
<td>NaCl</td>
<td>0.15</td>
<td>3.09</td>
</tr>
<tr>
<td>KCl</td>
<td>0.81</td>
<td>3.34</td>
</tr>
<tr>
<td>RbCl</td>
<td>1.35</td>
<td>3.43</td>
</tr>
<tr>
<td>LiBr</td>
<td>0.03</td>
<td>4.06</td>
</tr>
<tr>
<td>NaBr</td>
<td>0.15</td>
<td>4.23</td>
</tr>
<tr>
<td>KBr</td>
<td>0.81</td>
<td>4.48</td>
</tr>
<tr>
<td>RbBr</td>
<td>1.35</td>
<td>4.61</td>
</tr>
</tbody>
</table>

In Table II we present our calculated values of the re- normalized deformation dipoles. They were calculated in Ref. 12 using the local-density approximation (LDA). For anions the longitudinal $\bar{\gamma}_{l}$ part has values that are positive and relatively large. These values are quite simi- lar to those obtained by Hardy and Karo by fitting pho- non spectra. We emphasize that our values are theoreti- cal ones obtained using LDA. The values for the trans- verse component for the anions are smaller and negative. This is also in good accord with Hardy and Karo. For the positive ions we find that the transverse component is effectively zero. That is, the total value we found before was just the dipolar part. $^{12}$ For cations the longitudinal part is small and negative. Here we also agree with Har-dy and Karo. They listed positive values, but defined $\gamma$  for cations with the opposite sign, so we agree. We are pleased that the $a b$ initio values calculated from LDA agree well with the values fitted to phonon spectra.

(4) Indirect ionic interactions. Earlier we introduced a type of three-body force called $I^{3}$ . It is related to the con cept of deformability. For the rocksalt structure there are six constants associated with each type of ion: $g_{1}, g_{2}$ , $g_{3}, g_{4}, h_{1}$ , and $h_{2}$ . They represent forces between two first neighbors of a central ion, which are caused by the induced polarization of the central ion. Figure 1 shows the motions associated with each parameter in rocksalt. We call lattice dynamics including $I^{3}$ plus the above con tributions the "deformation-dipole-indirect-ionic-inter- action" model $(D^{2} I^{3})$ .

These parameters must also be renormalized. They in- clude all interactions between these neighbors. In order to avoid double counting, one must also subtract the di- polar part. Furthermore, these ions also interact with deformation-dipole-induced-dipole forces, which must be subtracted also. Thus the $I^{3}$ matrix $M_{\mu v}$ is renormal ized to the new value $\bar{M}$ according to

$$
\overline{M}=M+Z^{2} e^{2}(\phi \cdot \alpha \cdot \phi+\phi \cdot \overline{\gamma}+\overline{\gamma} \cdot \phi).
$$

In binary lattices the usual geometry is that the two neighbors to the central ion are identical and equidistant from the central ion. If the two neighboring ions have a bond angle of $\beta$ , the renormalization is

$$
\overline{g}_{1}=g_{1}+8 \cos (\beta)\left(\alpha / R^{3}-\overline{\gamma}_{l}\right),
$$

$$
\overline{g}_{2}=g_{2}-2 \sin (\beta)\left(2 \alpha / R^{3}+2 \overline{\gamma}_{t}-\overline{\gamma}_{l}\right),
$$

$$
\overline{g}_{3}=g_{3}-2 \cos (\beta)\left(\alpha / R^{3}+2 \overline{\gamma}_{t}\right),
$$

$$
\overline{g}_{4}=g_{4}+2 \alpha / R^{3}+4 \overline{\gamma}_{t},
$$

$$
\overline{h}_{1}=h_{1}-8 \alpha / R^{3}+8 \overline{\gamma}_{l},
$$

$$
\overline{h}_{2}=h_{2}+2 \alpha / R^{3}+4 \overline{\gamma}_{t}.
$$

<table>
<caption>TABLE II. Theoretical renormalized $\text{I}^3$ parameters calculated using the local-density approximation. The central ion is the first one listed.</caption>
<thead>
<tr>
<th></th>
<th>$\bar{\gamma}_{l}$</th>
<th>$\bar{\gamma}_{t}$</th>
<th>$\bar{g}_{1}$</th>
<th>$\bar{g}_{2}$</th>
<th>$\bar{g}_{3}$</th>
<th>$\bar{g}_{4}$</th>
<th>$\bar{h}_{1}$</th>
<th>$\bar{h}_{2}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>NaF</td>
<td>$-0.002$</td>
<td>$0.000$</td>
<td>$0.014$</td>
<td>$-0.001$</td>
<td>$0.007$</td>
<td>$0.000$</td>
<td>$-0.018$</td>
<td>$0.005$</td>
</tr>
<tr>
<td>NaCl</td>
<td>$-0.014$</td>
<td>$0.001$</td>
<td>$0.028$</td>
<td>$-0.005$</td>
<td>$0.006$</td>
<td>$0.001$</td>
<td>$-0.030$</td>
<td>$0.005$</td>
</tr>
<tr>
<td>NaBr</td>
<td>$-0.017$</td>
<td>$0.001$</td>
<td>$0.033$</td>
<td>$-0.003$</td>
<td>$0.005$</td>
<td>$0.002$</td>
<td>$-0.023$</td>
<td>$0.005$</td>
</tr>
<tr>
<td>KF</td>
<td>$-0.012$</td>
<td>$0.001$</td>
<td>$0.064$</td>
<td>$-0.019$</td>
<td>$0.032$</td>
<td>$0.004$</td>
<td>$-0.088$</td>
<td>$0.023$</td>
</tr>
<tr>
<td>KCl</td>
<td>$-0.046$</td>
<td>$0.003$</td>
<td>$0.120$</td>
<td>$-0.020$</td>
<td>$0.024$</td>
<td>$0.002$</td>
<td>$-0.078$</td>
<td>$0.016$</td>
</tr>
<tr>
<td>KBr</td>
<td>$-0.054$</td>
<td>$0.004$</td>
<td>$0.139$</td>
<td>$-0.021$</td>
<td>$0.023$</td>
<td>$0.004$</td>
<td>$-0.052$</td>
<td>$0.016$</td>
</tr>
<tr>
<td>RbF</td>
<td>$-0.019$</td>
<td>$0.002$</td>
<td>$0.102$</td>
<td>$-0.039$</td>
<td>$0.051$</td>
<td>$0.011$</td>
<td>$-0.132$</td>
<td>$0.037$</td>
</tr>
<tr>
<td>RbCl</td>
<td>$-0.059$</td>
<td>$0.005$</td>
<td>$0.165$</td>
<td>$-0.034$</td>
<td>$0.039$</td>
<td>$0.006$</td>
<td>$-0.102$</td>
<td>$0.025$</td>
</tr>
<tr>
<td>RbBr</td>
<td>$-0.081$</td>
<td>$0.006$</td>
<td>$0.223$</td>
<td>$-0.042$</td>
<td>$0.038$</td>
<td>$0.008$</td>
<td>$-0.043$</td>
<td>$0.026$</td>
</tr>
<tr>
<td>FNa</td>
<td>$0.167$</td>
<td>$-0.024$</td>
<td>$-0.143$</td>
<td>$0.124$</td>
<td>$0.020$</td>
<td>$-0.020$</td>
<td>$0.532$</td>
<td>$0.006$</td>
</tr>
<tr>
<td>FK</td>
<td>$0.135$</td>
<td>$-0.017$</td>
<td>$-0.124$</td>
<td>$0.093$</td>
<td>$0.005$</td>
<td>$-0.013$</td>
<td>$0.450$</td>
<td>$0.000$</td>
</tr>
<tr>
<td>FRb</td>
<td>$0.117$</td>
<td>$-0.014$</td>
<td>$-0.109$</td>
<td>$0.076$</td>
<td>$0.005$</td>
<td>$-0.010$</td>
<td>$0.373$</td>
<td>$0.001$</td>
</tr>
<tr>
<td>ClNa</td>
<td>$0.160$</td>
<td>$-0.018$</td>
<td>$-0.106$</td>
<td>$0.086$</td>
<td>$0.073$</td>
<td>$-0.003$</td>
<td>$0.353$</td>
<td>$0.054$</td>
</tr>
<tr>
<td>ClK</td>
<td>$0.149$</td>
<td>$-0.016$</td>
<td>$-0.122$</td>
<td>$0.092$</td>
<td>$0.043$</td>
<td>$-0.008$</td>
<td>$0.391$</td>
<td>$0.033$</td>
</tr>
<tr>
<td>ClRb</td>
<td>$0.130$</td>
<td>$-0.014$</td>
<td>$-0.108$</td>
<td>$0.077$</td>
<td>$0.039$</td>
<td>$-0.007$</td>
<td>$0.331$</td>
<td>$0.027$</td>
</tr>
<tr>
<td>BrNa</td>
<td>$0.160$</td>
<td>$-0.018$</td>
<td>$-0.089$</td>
<td>$0.075$</td>
<td>$0.090$</td>
<td>$-0.002$</td>
<td>$0.298$</td>
<td>$0.062$</td>
</tr>
<tr>
<td>BrK</td>
<td>$0.151$</td>
<td>$-0.017$</td>
<td>$-0.110$</td>
<td>$0.091$</td>
<td>$0.057$</td>
<td>$-0.009$</td>
<td>$0.356$</td>
<td>$0.040$</td>
</tr>
<tr>
<td>BrRb</td>
<td>$0.139$</td>
<td>$-0.016$</td>
<td>$-0.102$</td>
<td>$0.083$</td>
<td>$0.052$</td>
<td>$-0.009$</td>
<td>$0.322$</td>
<td>$0.034$</td>
</tr>
<tr>
<td>AgF</td>
<td>$0.062$</td>
<td>$-0.009$</td>
<td>$0.092$</td>
<td>$0.003$</td>
<td>$0.150$</td>
<td>$0.009$</td>
<td>$-0.095$</td>
<td>$0.101$</td>
</tr>
<tr>
<td>AgCl</td>
<td>$-0.094$</td>
<td>$0.014$</td>
<td>$0.493$</td>
<td>$-0.045$</td>
<td>$0.179$</td>
<td>$0.018$</td>
<td>$-0.512$</td>
<td>$0.102$</td>
</tr>
<tr>
<td>AgBr</td>
<td>$-0.135$</td>
<td>$0.019$</td>
<td>$0.493$</td>
<td>$-0.028$</td>
<td>$0.199$</td>
<td>$0.017$</td>
<td>$-0.548$</td>
<td>$0.101$</td>
</tr>
<tr>
<td colspan="5">Zinc blende</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>AgI</td>
<td>$-0.229$</td>
<td>$0.051$</td>
<td>$1.941$</td>
<td>$-0.071$</td>
<td>$0.512$</td>
<td>$0.129$</td>
<td></td>
<td></td>
</tr>
<tr>
<td>CuF</td>
<td>$0.741$</td>
<td>$-0.162$</td>
<td>$0.147$</td>
<td>$0.711$</td>
<td>$0.990$</td>
<td>$0.068$</td>
<td></td>
<td></td>
</tr>
<tr>
<td>CuCl</td>
<td>$-0.035$</td>
<td>$-0.029$</td>
<td>$0.512$</td>
<td>$-0.174$</td>
<td>$0.614$</td>
<td>$0.274$</td>
<td></td>
<td></td>
</tr>
<tr>
<td>CuBr</td>
<td>$-0.105$</td>
<td>$0.038$</td>
<td>$0.811$</td>
<td>$-0.131$</td>
<td>$0.630$</td>
<td>$0.173$</td>
<td></td>
<td></td>
</tr>
<tr>
<td>CuI</td>
<td>$-0.143$</td>
<td>$0.057$</td>
<td>$0.366$</td>
<td>$0.432$</td>
<td>$0.893$</td>
<td>$0.164$</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

![](./images/811746143967903745_1.jpg)

FIG. 1. The six coupling constants that occur in rocksalt due to indirect ionic interactions. Polarization of the central ion induces forces between two of its first neighbors.

The parameters $h_1$ and $h_2$ have a bond angle of $\beta=\pi$ and are renormalized according to the prescription for $g_1$ and $g_4$, respectively. Table II provides some values for the renormalized $\text{I}^3$ parameters, as calculated by LDA.¹² The rocksalt lattices have $\beta=\pi/2$ so that $g_1$ and $g_3$ are unchanged. The zinc-blende lattice has $\cos(\beta)=-\frac{1}{3}$ for the tetrahedral bond. These force constants have units of $e^2/V_0$, where $V_0$ is the volume of the unit cell. The table includes previous values for the alkali halides, which are now renormalized, plus some new values for copper and silver halides. The values are small for those constants involving shear motions, particularly for $g_4$. The radial forces $g_1$ and $h_1$ usually have the largest value. Below we will try to compare these values with those obtained by fitting the phonon spectra to the lattice dynamics.

The LDA values for the $\text{I}^3$ parameters for the copper and silver ions are larger than for the alkali and halide ions. Copper and silver are particularly deformable. Our LDA results provide support for the conjecture of Bilz and co-workers that deformability is large for these ions.

From now on we will only use the renormalized param-

eters for the deformation dipoles and $I^{3}$.

We divide the dynamical matrix into a short- and a long-range part. The long-range part includes the dipolar terms plus the deformation dipoles. In symbolic notation it has the form
$$
D=(1-\bar{\gamma}) \cdot \phi \cdot(1+\alpha \cdot \phi)^{-1} \cdot(1-\bar{\gamma}).
$$

This form of the long-range part is identical to that of Hardy and $Karo^{3}$ and other standard references on the deformation dipole model. $^{6}$

The short-range part of the dynamical matrix needs to be discussed in more detail. It contains the pairwise direct interactions plus the renormalized $I^{3}$ interactions. So far we have introduced 18 physical parameters for these terms: six short-range parameters $A_{j}$ and $B_{j}$ and six $I^{3}$ parameters for each type of ion. However, for the rocksalt lattice we now show that the dynamical matrix only has 12 different parameters. So if we try to fit experimental data to the dynamical matrix, we can only obtain 12 short-range parameters. The fitting procedure cannot obtain all 16 physical parameters. The short-range part of the $6 \times 6$ dynamical matrix can be written in terms of $3 \times 3$ matrices $M$ and $N$ as
$$
D=\left(\begin{array}{cc}
M(+) & N \\
N & M(-)
\end{array}\right),
$$
where $M( \pm)$ are the forces between like ions, while $N$ are the forces between unlike ions. Typical elements can be expressed in terms of angles $\theta_{j}=k_{j} a / 2$:
$$
\begin{aligned}
M_{x x}(+)= & -b_{0}+b_{1} \cos \theta_{y} \cos \theta_{z}+b_{2} \cos \theta_{x}\left(\cos \theta_{y}+\cos \theta_{z}\right) \\
& +b_{3} \cos \left(2 \theta_{x}\right)+b_{4}\left[\cos \left(2 \theta_{y}\right)+\cos \left(2 \theta_{z}\right)\right],
\end{aligned}
$$
$$
M_{x y}(+)=b_{5} \sin \theta_{x} \sin \theta_{y},
$$
$$
N_{x x}=c_{1} \cos \theta_{x}+c_{2}\left(\cos \theta_{y}+\cos \theta_{z}\right),
$$
$$
N_{x y}=0.
$$

The coefficient $b_{0}$ is not independent. The constraint that the acoustical phonon frequencies vanish at $k=0$ forces $b_{0}$ to equal a combination of the other parameters. Thus there are 12 independent constants: $b_{j}(j=1-5)$ for the $(+)$ ions, $b_{j}^{\prime}(j=1-5)$ for the $(-)$ ions, $c_{1}$, and $c_{2}$. In terms of the physical parameters they are given by
$$
b_{1}=8 \bar{g}_{4}^{\prime}-4 B_{++},
$$
$$
b_{2}=8 \bar{g}_{2}^{\prime}-2\left(A_{++}+B_{++}\right),
$$
$$
b_{3}=-2 \bar{h}_{1}^{\prime},
$$
$$
b_{4}=2 \bar{h}_{2}^{\prime},
$$
$$
b_{5}=4\left(\bar{g}_{1}^{\prime}-\bar{g}_{3}^{\prime}\right)+2\left(A_{++}-B_{++}\right),
$$
$$
c_{1}=2\left(\bar{h}_{1}+\bar{h}_{1}^{\prime}\right)-8\left(\bar{g}_{2}+\bar{g}_{2}^{\prime}\right)-2 A_{+-},
$$
$$
c_{2}=-2\left(\bar{h}_{2}+\bar{h}_{2}^{\prime}\right)-4\left(\bar{g}_{2}+\bar{g}_{2}^{\prime}\right)-4\left(\bar{g}_{4}+\bar{g}_{4}^{\prime}\right)-2 B_{+-},
$$
where primed values are for negative ions. The $b_{j}^{\prime}$ are found by interchanging primed and unprimed symbols in these equations, while using $A_{--}$and $B_{--}$for the short-range terms. The direct interaction between two positive ions ( $A_{++}$and $B_{++}$) contributes in a similar way to the indirect interaction through the negative ions that are their common neighbors. Only $\bar{h}_{1}$ and $\bar{h}_{2}$ are obtained directly from the fitted parameters.

Since there are only 12 parameters that can be deduced by fitting the phonon spectra, we must reduce the number of parameters in our model down to that number. In order to estimate which terms are large or small, we also calculated the direct interactions. We took the potentials from Kim and Gordon. $^{16}$ These results for second nearest neighbors are shown in Table III. These parameters, as well as all other force constants, are in units of $e^{2} / V_{0}$, where $V_{0}$ is the cell volume. The second-neighbor direct interactions are small for most alkali halides. We decided to fit only the phonon spectra for the larger cations. Then the second neighbors are all far apart, and the direct interactions are small. We assumed in our fitting scheme that $A_{++}=B_{++}=A_{--}=B_{--}$ $=0$. Some prior fits have found larger values for these second-neighbor interactions, but we now regard those values as evidence for the presence of indirect ionic interactions. Setting to zero the second-neighbor interactions reduced the number of physical parameters down to 14. Furthermore, in rocksalt, $\bar{g}_{1}$ and $\bar{g}_{3}$ always appear in the combination of $\bar{g}_{13}=\bar{g}_{1}-\bar{g}_{3}$ so they can never be obtained separately. This reduces the number of physical parameters down to the 12 parameters in the dynamical matrix.

## FITTING THE PHONON DATA

The theoretical model was fitted to the neutron data for $\mathrm{KCl}, \mathrm{KBr},{ }^{18} \mathrm{RbCl},{ }^{19}$ and $\mathrm{AgBr} .{ }^{20}$ The latter case was included in order to investigate the hypothesis that $I^{3}$ parameters are large for $\mathrm{Ag}^{+}$ions. A least-squares fit was done by comparing the calculated phonon frequencies $\left[\omega(q)_{\text {calc }}\right.$ with the experimental phonon frequencies $[\omega(q)]_{\text {expt }}$ weighted by the error uncertainty $\Delta(q)$,
$$
\chi^{2}=\frac{1}{N-K} \sum_{i}\left|\frac{\left[\omega\left(\mathbf{q}_{i}\right)\right]_{\text {calc }}-\left[\omega\left(\mathbf{q}_{i}\right)\right]_{\text {expt }}}{\Delta\left(\mathbf{q}_{i}\right)}\right|^{2},
$$
where $N$ is the number of measured phonon points. This was always much larger than the number of fitting parameters. Usually we obtained values of $\chi$ of order unity,

<table>
<caption>TABLE III. Short-range force constants (in units $e^{2} / V_{0}$ ) obtained from the interionic potential of Kim and Gordon (Ref. 16).</caption>
<thead>
<tr>
<th>
</th>
<th>
$r_{2}$
</th>
<th>
$A_{--}$
</th>
<th>
$B_{--}$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
AgCl
</td>
<td>
7.41
</td>
<td>
0.089
</td>
<td>
0.029
</td>
</tr>
<tr>
<td>
NaCl
</td>
<td>
7.54
</td>
<td>
0.052
</td>
<td>
0.031
</td>
</tr>
<tr>
<td>
KCl
</td>
<td>
8.41
</td>
<td>
$-$0.106
</td>
<td>
0.035
</td>
</tr>
<tr>
<td>
RbCl
</td>
<td>
8.79
</td>
<td>
$-$0.200
</td>
<td>
0.030
</td>
</tr>
<tr>
<td>
AgBr
</td>
<td>
7.72
</td>
<td>
0.025
</td>
<td>
0.047
</td>
</tr>
<tr>
<td>
NaBr
</td>
<td>
7.78
</td>
<td>
$-$0.048
</td>
<td>
0.050
</td>
</tr>
<tr>
<td>
KBr
</td>
<td>
8.82
</td>
<td>
$-$0.200
</td>
<td>
0.050
</td>
</tr>
</tbody>
</table>

so that the theory and experiment were fitted to within their uncertainty in the data. Theoretical curves, in fact, look just like the experimental ones.

Lattice constants, ion masses, and ion polarizabilities were fixed at the outset. The first step in fitting the alkali halides was to start with a simple model of few parameters: $A_{+-}$, $B_{+-}$, $\gamma_{l}^{(-)}$, $g_{1}^{(-)}$, $h_{1}^{(-)}$. (Note that for $g_1-g_3$ we set $g_3=0$.) These were expected to be the largest parameters. This set is small in number, so a fit was obtained easily. Then the other parameters were added one at a time. Each was tested to see which gave the biggest reduction in $\chi$, and then it was added to the parameter set, and the entire set was varied to reduce $\chi$. Some parameters did not decrease $\chi$ and so were omitted entirely. Parameters whose fitted value was smaller than 0.01 were set equal to zero. For AgBr the procedure was different since the parameters of the cation were larger than those of the halide. The results are shown in Table IV. Generally it was found that the following parameters are negligible: $\gamma_{t}$, $g_2$, $g_4$, and $h_2$. Only for AgBr did these parameters have significant values. In some cases over a hundred runs were needed to obtain the final fitting.

Figures 2 and 3 show the comparison between theory and experiment for KBr and AgBr. The solid lines are the theoretical fit, while the triangles are data points from neutron scattering. The experimental error bar is about the size of the triangle. The LO phonon in KBr is typical of alkali halides, in that the frequency is highest at the $\Gamma$ point. The frequencies decline in value for increasing values of $k$ and are similar to TO frequencies at the zone edge. This dependence arises from the $k$ dependence of the long-range Coulomb interactions. The LO phonon in AgBr has a different behavior. Its frequency has a higher value at the zone edge than at the zone center. This behavior is caused by the strong $I^3$ interactions.

<table>
<caption>TABLE IV. Parameters were obtained by fitting to phonon data. Omitted parameters had negligible values.</caption>
<thead>
<tr>
<th></th>
<th>KCl</th>
<th>KBr</th>
<th>RbCl</th>
<th>AgBr</th>
</tr>
</thead>
<tbody>
<tr>
<td>$A_{\pm}$</td>
<td>6.29</td>
<td>6.30</td>
<td>6.81</td>
<td>6.69</td>
</tr>
<tr>
<td>$B_{\pm}$</td>
<td>$-0.59$</td>
<td>$-0.62$</td>
<td>$-0.68$</td>
<td>$-0.73$</td>
</tr>
<tr>
<td>$\bar{\gamma}_{l}^{(+)}$</td>
<td>0</td>
<td>0</td>
<td>$-0.04$</td>
<td>0.18</td>
</tr>
<tr>
<td>$\bar{\gamma}_{t}^{(+)}$</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0.01</td>
</tr>
<tr>
<td>$\bar{\gamma}_{l}^{(-)}$</td>
<td>0.12</td>
<td>0.14</td>
<td>0.16</td>
<td>0</td>
</tr>
<tr>
<td>$\bar{\gamma}_{t}^{(-)}$</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>$-0.02$</td>
</tr>
<tr>
<td>$\bar{g}_{1}^{(+)}$</td>
<td>0.11</td>
<td>0.01</td>
<td>0.08</td>
<td>0.31</td>
</tr>
<tr>
<td>$\bar{g}_{2}^{(+)}$</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0.09</td>
</tr>
<tr>
<td>$\bar{g}_{4}^{(+)}$</td>
<td>0</td>
<td>0.03</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>$\bar{h}_{1}^{(+)}$</td>
<td>$-0.12$</td>
<td>0.09</td>
<td>0.21</td>
<td>1.03</td>
</tr>
<tr>
<td>$\bar{h}_{2}^{(+)}$</td>
<td>0.01</td>
<td>0</td>
<td>0.04</td>
<td>0</td>
</tr>
<tr>
<td>$\bar{g}_{1}^{(-)}$</td>
<td>$-0.26$</td>
<td>$-0.20$</td>
<td>$-0.18$</td>
<td>0.29</td>
</tr>
<tr>
<td>$\bar{g}_{2}^{(-)}$</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>$-0.21$</td>
</tr>
<tr>
<td>$\bar{h}_{1}^{(-)}$</td>
<td>0.36</td>
<td>0.16</td>
<td>0.22</td>
<td>$-0.90$</td>
</tr>
<tr>
<td>$\bar{h}_{2}^{(-)}$</td>
<td>0.03</td>
<td>0.04</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>

![](./images/811746143967903745_2.jpg)

FIG. 2. The phonon frequencies of KBr. Frequencies are given in terahertz. The solid line is the theoretical fit. The triangles are the data points from neutron scattering (Ref. 18).

## CONCLUSIONS

Here we have presented a detailed theory of the lattice dynamics of rocksalt lattices using the deformation-dipole model and the indirect-ionic-interaction model ($D^2I^3$). After deriving the dynamical matrix, we wrote a computer code for the lattice dynamics. It was used to fit the measured phonon spectra of four lattices. This fitting provides the first "experimental" values for the $I^3$ parameters.

Earlier we$^{12}$ showed that these parameters could also be calculated using the local-density approximation (LDA). Here we present theoretical values using LDA

![](./images/811746143967903745_3.jpg)

FIG. 3. The phonon frequencies of AgBr. Frequencies are given in terahertz. The solid line is the theoretical fit. The triangles are the data points from neutron scattering (Ref. 20).

for the $D^2I^3$ parameters of the copper and silver halides. The $I^3$ parameters are large for the copper and silver ion. Thus three-body forces are large for the copper and silver halides, which explains why their lattice dynamics are different than for the alkali halides. The existence of large three-body forces had been conjectured by Bilz and co-workers, but the present work is the first real proof of this phenomenon.

The numerical values of the fitted parameters are quali- tatively similar to the ab initio parameters calculated by LDA and shown in Table III. Those that are predicted to be small usually are small, while those that are large are found to be larger, and usually with the correct sign. The LDA calculations gave a qualitative guide to the values obtained by fitting to the phonon spectra.

Elsewhere we show $^{13}$ that $D^2$ and $I^3$ provide a descrip- tion of the first-neighbor polarization forces in insulators. They occur naturally in the formalism, since deformation dipoles are an exact parametrization of pair interactions, while $I^3$ is an exact parametrization of three-body forces. There are also four-, five-, and higher-body forces. The largest part of these contribute to the dielectric screening, which is also included in the present theory. So the present model is an accurate description of the lattice dy- namics for insulators within the approximation that nearest-neighbor forces are included exactly, while far- ther neighbors are approximated by the dipolar model. We view the present model as an alternative to, and an improvement over, the shell model.

## ACKNOWLEDGMENTS

Research support for one of us (G.D.M.) from the Na- tional Science Foundation (Grant No. DMR-87-04210), from the University of Tennessee, and from the U.S. Department of Energy (through Contract No. DE- AC05-84OR21400, administered by Martin Marietta En- ergy Systems) is gratefully acknowledged.

$^{1}$A. D. B. Woods, W. Cochran, and B. N. Brockhouse, Phys. Rev. 119, 980 (1960).
$^{2}$W. Cochran, CRC Crit. Rev. Solid State Sci. 2, 1 (1971).
$^{3}$J. R. Hardy and A. M. Karo, The Lattice Dynamics and Statics of Alkali Halide Crystals (Plenum, New York, 1979).
$^{4}$J. R. Hardy, Philos. Mag. 7, 315 (1962).
$^{5}$A. M. Karo and J. R. Hardy, Phys. Rev. 129, 2024 (1963).
$^{6}$K. Kunc, M. Balkanski, and M. A. Nusimovici, Phys. Rev. B 12, 4346 (1975).
$^{7}$M. P. Verma and S. K. Agarwal, Phys. Rev. B 8, 4880 (1973).
$^{8}$K. Fischer, H. Bilz, R. Haberkorn, and W. Weber, Phys. Status Solidi B 54, 285 (1972).
$^{9}$W. G. Kleppmann and H. Bilz, Commun. Phys. 1, 105 (1976).
$^{10}$G. D. Mahan and M. Mostoller, Phys. Rev. Lett. 57, 357 (1986).
$^{11}$G. D. Mahan and M. Mostoller, Phys. Rev. B 34, 5726 (1986).
$^{12}$G. D. Mahan, Phys. Rev. B 34, 4235 (1986), 38, 7841(E) (1988).
$^{13}$G. D. Mahan, Phys. Rev. B (to be published).
$^{14}$R. P. Lowndes and D. H. Martin, Proc. R. Soc. London Ser. A 208, 473 (1969).
$^{15}$G. D. Mahan, Solid State Ionics 1, 29 (1980).
$^{16}$Y. S. Kim and R. G. Gordon, J. Chem. Phys. 60, 4332 (1974).
$^{17}$G. Raunio, L. Almqvist, and R. Stedman, Phys. Status Solidi 33, 209 (1969).
$^{18}$A. D. B. Woods, B. N. Brockhouse, R. A. Cowley, and W. Cochran, Phys. Rev. 131, 1025 (1963).
$^{19}$G. Raunio and S. Rolandson, J. Phys. C 3, 1013 (1970).
$^{20}$Y. Fujii, S. Hoshino, S. Sakuragi, H. Kanzaki, J. W. Lynn, and G. Shirane, Phys. Rev. B 15, 385 (1977).