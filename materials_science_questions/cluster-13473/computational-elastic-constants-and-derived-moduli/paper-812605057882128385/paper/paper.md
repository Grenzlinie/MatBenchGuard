# Elastic moduli in nano-size samples of amorphous solids: System size dependence

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2012 EPL 99 46002

(http://iopscience.iop.org/0295-5075/99/4/46002)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 128.189.203.83
This content was downloaded on 12/12/2014 at 07:34

Please note that terms and conditions apply.

# Elastic moduli in nano-size samples of amorphous solids: System size dependence

YOSSI COHEN and ITAMAR PROCACCIA(a)

Department of Chemical Physics, The Weizmann Institute of Science - Rehovot 76100, Israel

received 16 May 2012; accepted in final form 16 July 2012
published online 21 August 2012

PACS 62.25.-g – Mechanical properties of nanoscale systems
PACS 62.20.de – Elastic moduli
PACS 61.43.Dq – Amorphous semiconductors, metals, and alloys

**Abstract** – This letter is motivated by some recent experiments on pan-cake-shaped nano-samples of metallic glass that indicate a decline in the measured shear modulus upon decreasing the sample radius. Similar measurements on crystalline samples of the same dimensions showed a much more modest change. In this letter we offer a theory of this phenomenon; we argue that such results are generically expected for any amorphous solid, with the main effect being related to the increased contribution of surfaces with respect to the bulk when the samples get smaller. We employ exact relations between the shear modulus and the eigenvalues of the system's Hessian matrix to explore the role of surface modes in affecting the elastic moduli.

Copyright © EPLA, 2012

---

**Motivation.** – This letter is motivated by some experimental measurements of the elastic response of nano-samples of metallic glasses when the radius of cylindrically shaped samples was reduced [1]. In this letter we provide a theoretical explanation of this phenomenon. Since the experiments are performed at temperatures that are much lower than the glass-transition temperature, we can in the following disregard thermal effect, and study the phenomenon in athermal conditions.

**Mathematical background.** – For the sake of concreteness we study theoretically the shear modulus, stressing the difference in its exact calculation between a perfect crystalline sample and an amorphous solid sample of the same physical dimension. In both cases the calculation of the shear modulus starts with the potential energy which for a shear-strained solid can be written as $U(\{\boldsymbol{r}_i(\gamma_{\alpha\beta})\},\gamma_{\alpha\beta})$ where $\{\boldsymbol{r}_i\}_{i=1}^N$ are the positions of the $N$ particles and $\gamma_{\alpha\beta}$ is the applied strain. (When possible we treat $\gamma_{\alpha\beta}$ as a scalar $\gamma$; all the equations can be written in tensorial form if required.) In both cases we can consider the deformation under an infinitesimal shear strain via the parameterized transformation on the particles coordinates $\boldsymbol{J}(\gamma)=I+\gamma\boldsymbol{h}$ where $\boldsymbol{h}$ determines the imposed deformation. Here comes the important difference between crystalline and amorphous solids [2].

For the former
$$
\boldsymbol{r}_i \to \boldsymbol{J} \cdot \boldsymbol{r}_i, \quad \text{in a perfect crystalline solid}, \tag{1}
$$
since the particles remain in mechanical equilibrium also after the deformation, with all the forces $\boldsymbol{f}_i$ vanishing on each and every particle. In an amorphous solid, on the other hand, even an infinitesimal deformation gives rise to non-zero forces on the particles, resulting in non-affine displacements $\boldsymbol{u}_i$ that are necessary to restore mechanical equilibrium. Thus, for an amorphous solid
$$
\boldsymbol{r}_i \to \boldsymbol{J} \cdot \boldsymbol{r}_i + \boldsymbol{u}_i, \quad \text{in an amorphous solid}. \tag{2}
$$

This crucial difference translates to a different calculation of the mechanical moduli; in a perfect crystal we can write $\text{d}/\text{d}\gamma=\partial/\partial\gamma$. In an amorphous solid on the other hand
$$
\frac{\text{d}}{\text{d}\gamma} = \frac{\partial}{\partial\gamma} + \frac{\text{d}\boldsymbol{u}_i}{\text{d}\gamma} \cdot \frac{\partial}{\partial\boldsymbol{u}_i} = \frac{\partial}{\partial\gamma} + \frac{\text{d}\boldsymbol{u}_i}{\text{d}\gamma} \cdot \frac{\partial}{\partial\boldsymbol{r}_i}. \tag{3}
$$

Applying this to the definition of the shear modulus, $\mu=(1/V)\text{d}^2U/\text{d}\gamma^2$ (with $V$ being the volume) we find a different answer,
$$
\mu = \frac{1}{V} \frac{\partial^2U}{\partial\gamma^2}, \quad \text{perfect crystalline solid}, \tag{4}
$$

$$
\mu = \frac{1}{V} \left[ \frac{\partial^2U}{\partial\gamma^2} + \frac{\partial^2U}{\partial\gamma\partial\boldsymbol{r}_i} \cdot \frac{\text{d}\boldsymbol{u}_i}{\text{d}\gamma} \right], \quad \text{amorphous solid}. \tag{5}
$$

(a)E-mail: itamar.procaccia@gmail.com

46002-p1

Yossi Cohen and Itamar Procaccia

The shear modulus of the crystalline solid, which is the same as the first term in the shear modulus of the amorphous solid, is known as the Born approximation. This approximation is corrected by the second term which is due to the non-affine response of the amorphous solid.

Equation (5) is brought to final form using the mechanical equilibrium condition $\mathrm{d}\boldsymbol{f}_i/\mathrm{d}\gamma=0$, which, using eq. (3) becomes $\partial \boldsymbol{f}_i/\partial\gamma+(\partial \boldsymbol{f}_i/\partial \boldsymbol{r}_j)\cdot(\mathrm{d}\boldsymbol{u}_j/\mathrm{d}\gamma)=0$ [3]. Identifying the force on the $i$-th particle with $\boldsymbol{f}_i\equiv-\partial U/\partial \boldsymbol{r}_i$, we invert the last relation in favor of $\mathrm{d}\boldsymbol{u}_j/\mathrm{d}\gamma$ to write

$$
\frac{\mathrm{d}\boldsymbol{u}_i}{\mathrm{d}\gamma}=-H_{ij}^{-1}\Xi_j\ ;\quad H_{ij}\equiv\frac{\partial^2 U}{\partial \boldsymbol{r}_i\partial \boldsymbol{r}_j};\quad \Xi_i\equiv\frac{\partial^2 U}{\partial \boldsymbol{r}_i\partial\gamma}. \tag{6}
$$

Using eq. (6) in eq. (5) we get the final result

$$
\mu=\frac{1}{V}\frac{\partial^2 U}{\partial\gamma^2},\quad \text{perfect crystalline solid}, \tag{7}
$$

$$
\mu=\frac{1}{V}\left[\frac{\partial^2 U}{\partial\gamma^2}-\boldsymbol{\Xi}\cdot \boldsymbol{H}^{-1}\cdot\boldsymbol{\Xi}\right],\text{ amorphous solid}. \tag{8}
$$

Noticing that the Hessian matrix $\boldsymbol{H}$ is real and symmetric, the difference between the shear modulus of a crystalline and amorphous solid is negative definite, necessarily reducing the shear modulus in the case of the amorphous solid compared to the crystalline counterpart (with the same inter-particle potential). To understand the experimental observations of the mechanical softening of smaller and smaller samples we need to understand why the correction term increases in absolute magnitude compared to the Born term which is system size independent to a very good approximation. We start by computing eq. (8) using numerical simulations.

Numerical simulations. - Glassy amorphous samples were achieved by using a binary mixture of point particles interacting via modified Lennard-Jones potential with three different characteristic interaction lengths $\sigma_{ss}=1$ and $\sigma_{\ell\ell}=1.4$ and $\sigma_{s\ell}=1.18$. Details of the potentials can be found for example in refs. [4,5]. Cuboid samples of fixed height ($\approx$ 15 particles) and square cross-section with varying edges (from 50 to 15 particles) were prepared by quenching from the melt using a gradient energy method to cool the system to $T=0$ with zero pressure. The boundary conditions were free on all the edges except the two edges that were clamped to produce infinitesimal shear strain. Clamping the upper and lower edges we obtain a strain $\gamma_{xz}$ to measure $\mu_{xz}$ while clamping two opposite side walls resulted in measuring $\mu_{xy}$ (cf. fig. 1). For any given system the Born term was computed directly from the partial derivatives [6,7]. The correction term was obtained by computing the Hessian matrix and the vector $\boldsymbol{\Xi}$, again directly from their definitions, inverting the Hessian we compute $\boldsymbol{\Xi}\cdot \boldsymbol{H}^{-1}\cdot\boldsymbol{\Xi}$ exactly. Results for both shear moduli as a function of the ratio of width to height are shown in fig. 2.

![](./images/812605057882128385_1.jpg)

Fig. 1: (Color online) A cuboid shape. The top and bottom surfaces (green) were clamped to measure $\mu_{xz}$, and the opposite side wall (red) for $\mu_{xy}$.

![](./images/812605057882128385_2.jpg)

Fig. 2: (Color online) The dependence of the shear moduli $\mu_{xz}$ and $\mu_{xy}$ on the ratio of the edge size over the height for systems varying by a factor of 3.5 in this ratio. One observes a change of about $50\%$ in $\mu_{xz}$ and about $15\%$ in $\mu_{xy}$.

We observe a much larger change in $\mu_{xz}$ (about $50\%$) than in $\mu_{xy}$ (about $15\%$). We will argue below that this difference stems from the contribution of free surfaces. In order to emphasize the role of the free surfaces, we performed the same measurements of the shear modulus in an infinite system made of finite cells which repeat by applying periodic boundary conditions. In this case the shear modulus exhibits the value of the bulk modulus for both directions and for various cell size, cf. fig. 3.

![](./images/812605057882128385_3.jpg)

Fig. 3: (Color online) The same as in fig. 2, but with periodic boundary condition.

46002-p2

Elastic moduli in nano-size samples of amorphous solids: System size dependence

![](./images/812605057882128385_4.jpg)

Fig. 4: (Color online) The seven lowest eigenvalues of the Hessian matrix multiplied by the volume of the sample, including the zero eigenvalue which relates to the Goldstone mode. Note the strong decline as $Lx/Lz$ approaches 1.

Theoretical explanation. - Having observed a tendency towards softening that is very comparable in magnitude to the experimental one, we are now in a position to provide a theoretical explanation. Qualitatively speaking we expect that particles close to the free surfaces should have softer fluctuations in their positions, being less constrained than particles in the bulk. By lowering the volume of the samples we make the contribution of particles at and near the surface more dominant, resulting in an overall softening of the mechanical response. Being equipped with the theory presented above, we can prove this qualitative intuition by examining the eigenvalues and eigenfunctions of the Hessian matrix $\boldsymbol{H}$ and how they depend on the volume. The negative definite term in the amorphous shear modulus can be written in a way that makes the contribution of the eigenvalues of the Hessian explicit by expanding $\boldsymbol{\Xi}$ in the eigenfunctions $\boldsymbol{\Psi}^{(k)}$ of $\boldsymbol{H}$:

$$
\boldsymbol{\Xi}=\sum_{k} a_{k} \boldsymbol{\Psi}^{(k)} ; \quad a_{k} \equiv \boldsymbol{\Xi} \cdot \boldsymbol{\Psi}^{(k)}. \tag{9}
$$

With this in mind we can write the correction term to the Born approximation in the form

$$
-\frac{1}{V} \boldsymbol{\Xi} \cdot \boldsymbol{H}^{-1} \cdot \boldsymbol{\Xi}=\frac{1}{V} \sum_{k} \frac{\left|a_{k}\right|^{2}}{\lambda_{k}}, \tag{10}
$$

where $\lambda_{k}$ is the eigenvalue of the Hessian matrix associated with the eigenfunction $\boldsymbol{\Psi}^{(k)}$.

In ref. [8] it was shown that $|a_{k}|^{2}$ is roughly system size independent. This is not the case for the eigenvalues. In fig. 4 we show the seven lowest eigenvalues of the Hessian matrix (including the Goldstone mode [2]) multiplied by the volume, and observe the strong decline in these products when $L_{x}/L_{z}$ becomes smaller than, say, 1.6. This decline will increase the negative correction term and accordingly will reduce the moduli. It is also obvious why $\mu_{xz}$ is much more sensitive to this effect than $\mu_{xy}$ —in the former case, the large top and bottom surfaces are clamped and only the side walls are free to contribute. Upon increasing the ratio $Lx/Lz$ the contribution of the free surfaces decreases, and the shear modulus increases until we reach the value of the bulk. In the latter case, the large top and bottom surfaces are free, contributing to the softening of the system. Clearly, we need large free surfaces to observe a sizeable effect; when we reduce the volume the ratio of surface to volume increases, lowering the overall shear modulus. We can directly prove that the effect is strongly connected to the free surfaces by examining the eigenfunctions associated with the lowest lying eigenvalues. In figs. 5 and 6 we present the first and second eigenfunction by showing the magnitude of elements of the eigenfunctions in real space.

![](./images/812605057882128385_5.jpg)

Fig. 5: (Color online) Upper panel: an $xz$ projection by averaging over the $y$ position of the magnitude of the elements of the first nontrivial eigenfunction of the Hessian for the case $L_{x}/L_{z}=1.86$. Lower panel: the same but for an $xy$ projection, averaging over $z$. The color code is given on the right. Note the strong concentration on the surfaces.

We see that both eigenfunctions are strongly concentrated on the surfaces. This is a direct evidence that the lowest eigenvalues of the Hessian, which are responsible for the softest mechanical response, indeed belong to modes that live on the surfaces of our samples as proposed above.

At this point it is interesting to compare the simulation results to similar simulations on crystalline samples of the same range of sizes and the same geometry. We attempted to produce perfect crystalline samples by

46002-p3

![](./images/812605057882128385_6.jpg)

Fig. 6: (Color online) The same as in the previous figure, but for the second nontrivial eigenfunction of the Hessian. Again we see that the lowest eigenvalues belong to eigenfunctions that are strongly concentrated on the surfaces.

![](./images/812605057882128385_7.jpg)

Fig. 7: (Color online) An example of a crystalline solid in three dimensions. The order of the crystal is distorted due to free surface effect. Note that the blue particles are on the surface and as the color code tends to red we observe bulk crystalline order.

arranging either "small" or "large" particles on a lattice at zero temperature. We find that when we minimize the energy, surface tension effects destroy the crystalline order near the interfaces, leaving us with bulk crystals with amorphous interfaces, as seen for example in fig. 7.

![](./images/812605057882128385_8.jpg)

Fig. 8: (Color online) The dependence of the shear moduli on the ratio of the edge size over the height, for an amorphous solid (stars), and a crystalline solid (circles) contains either small or large particles, normalized to the value of the shear modulus of a cube.

![](./images/812605057882128385_9.jpg)

Fig. 9: (Color online) The same as in fig. 4 but for a crystalline solid. Here the decline is weaker than the case of an amorphous solid.

We thus expect to still see an effect of softening when the surface to bulk ratio is reduced, but the effect should be smaller compared to the completely amorphous samples. For the sake of comparison we show normalized values of $\mu_{xz}$ (normalized to the lowest value) for the three types of samples, amorphous and crystalline with small or large particles. In fig. 8 we see that the crystalline samples show very similar curves for $\mu_{xz}$, and the effect is considerably smaller than for the amorphous solid. The relative decrease in the size of the effect is also born out by the values of the lowest eigenvalues of the Hessian matrix (multiplied by the volume) as seen in fig. 9. The eigenvalues times the volume still have a reduction for the largest values of the surface to volume ratio, but the degree of reduction is considerably smaller, cf. fig. 4. We expect that for larger samples (as in the experiment) where the surface to bulk ratio is smaller than in our

simulations, the effect will be even smaller than in our present simulations.

In summary, we have shown that the main reason that is responsible for the softening of the mechanical response of nano-samples as a function of their size comes from the softer normal modes of the Hessian matrix that are concentrated near the boundaries. These reflect the physics of increased freedom of particles near the surfaces compared to the highly constrained particles in the bulk.

***

This work had been supported in part by an advanced "ideas" grant of the European Research Council, the Israel Science Foundation and the German Israeli Foundation.

## REFERENCES

[1] SAMWER K., private communication (2012).

[2] CHAIKIN P. M. and LUBENSKY T. C., *Principles of Condensed Matter Physics* (Cambridge University Press) 1995.

[3] MALONEY C. and LEMAÎTRE A., *Phys. Rev. Lett.*, **93** (2004) 016001.

[4] KOB W. and ANDERSEN H. C., *Phys. Rev. E*, **51** (1995) 4626.

[5] KARMAKAR S., LERNER E., PROCACCIA I. and ZYLBERG J., *Phys. Rev. E*, **83** (2011) 046106.

[6] KARMAKAR S., LERNER E. and PROCACCIA I., *Phys. Rev. E*, **82** (2010) 026105.

[7] MALONEY C. and LEMAÎTRE A., *Phys. Rev. E*, **74** (2006) 016118.

[8] HENTSCHEL H. G. E., KARMAKAR S., LERNER E. and PROCACCIA I., *Phys. Rev. E*, **83** (2011) 061101.