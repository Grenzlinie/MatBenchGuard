An introduced effective-field approximation and Monte Carlo study of a spin-1 Blume–Capel model on a square lattice

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2009 Phys. Scr. 79 045009

(http://iopscience.iop.org/1402-4896/79/4/045009)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 129.130.252.222
This content was downloaded on 08/07/2014 at 13:23

Please note that terms and conditions apply.

# An introduced effective-field approximation and Monte Carlo study of a spin-1 Blume–Capel model on a square lattice

Yusuf Yüksel, Ümit Akıncı and Hamza Polat

Department of Physics, Dokuz Eylül University, Izmir, 35160/Buca, Turkey
E-mail: hamza.polat@deu.edu.tr

Received 26 January 2009
Accepted for publication 6 March 2009
Published 1 April 2009
Online at stacks.iop.org/PhysScr/79/045009

## Abstract
The magnetic properties of a spin-1 Blume–Capel (BC) model on a square lattice ($q=4$) with a ferromagnetic interaction have been examined here by the use of Monte Carlo (MC) simulation technique and an introduced effective-field approximation (IEFT), which includes the correlations between different spins that emerge when expanding the identities. The effects of the external magnetic field and crystal field on the magnetic properties of the spin system are discussed in detail. In order to obtain credible results, a detailed comparison of the results obtained by the two methods has been made with those of the other methods in the literature. A number of interesting phenomena originating from the temperature, crystal field and external field have been found.

PACS numbers: 05.50.+q, 75.10.Hk, 75.40.Cx, 75.40.Mg, 64.60.De

---

## 1. Introduction
The spin-$S$ ($S\geqslant1/2$) Blume–Capel (BC) model is one of the most extensively studied models in statistical mechanics and condensed matter physics. This is because the BC model is a very simple model and exhibits a variety of multicritical phenomena such as a phase diagram with ordered ferromagnetic and disordered paramagnetic phases separated by a transition line that changes from a continuous phase transition to a first-order transition at a tricritical point. This model is also a generalization of the standard Ising model. Indeed, its longitudinal crystal field or the single-ion anisotropy included version was introduced as a spin-1 Ising model by Blume [1] and independently by Capel [2] in the literature; therefore, it is called a Blume–Capel model. Furthermore, versions and extensions of the model can be applied to describe many different physical situations such as multicomponent fluids, ternary alloys, $^3$He–$^4$He mixtures, as well as various magnetic problems [3]. The spin-1 system was studied by a variety of methods such as the two-spin cluster [4], the Bethe lattice approximation (BLA) [5], the series expansion (SE) method [6], constant-coupling approximation (CCA) [7], the cluster variation method (CVM) [8], Monte Carlo (MC) simulations and Monte Carlo renormalization-group (MCRG) methods [9–11], finite-size scaling (FSS) [12–15], the renormalization-group (RG) method [16–18] and effective-field theory (EFT) [19–21].

Recently, in order to improve the statistical accuracy of EFT based on differential operator technique, Kaneyoshi introduced the correlated effective-field theory (CEFT) [22], a new type of cluster theory (CT) [23] and the extended decoupling approximation (DA) [24] in the spin-$S$ Ising ferromagnetic system. However, these approximations are not sufficient enough to improving the results much. The reason may be the usage of a decoupling approximation in EFT, because the decoupling approximation neglects the correlations between different spins that emerge when expanding the identities. The statistical accuracy of the studies mentioned above is essentially equivalent to the Zernike approximation [25]. Furthermore, a new approximation (the expanded Bethe–Peierls approximation (EBPA)) is introduced by Du *et al* [26] to improve the critical values (transition temperature $k_{\text{B}}T_{\text{c}}/J$ and value of $D_{\text{t}}/J$ at the tricritical point) for spin-1 Ising systems on two- and three-dimensional

lattices, but EBPA is not an application to study the phase diagram of a spin-$S$ transverse Ising ferromagnetic system. Most formulations in the studies mentioned above are based on the identities valid for the Ising spin systems.

In our introduced effective-field (IEFT) approximation [27–29], the effective field is determined from the condition that the expectation value of the central spin is equal to that of the perimeter spins. The IEFT approximation takes into account the correlations between different spins in the cluster of considered lattices. Namely, the hallmark of the IEFT is to consider the correlations between different spins that emerge when expanding the identities. Therefore, it is expected that the calculation result will be more accurate.

On the other hand, for many decades, MC simulation [30] has been one of the main tools for studying problems in many areas of physics such as continuous spin systems, fluids, polymers, disordered materials and lattice gauge theories. This method is a powerful numerical approach and it is widely used to study the problems mentioned above. By utilizing this tool, we can understand many complex systems, especially interesting phenomena, e.g. critical phenomena and phase transitions, which are otherwise almost impossible to comprehend. More specifically, in condensed matter physics, the MC simulation method was the primary method used to obtain concrete results even after the development of renormalization group techniques [31].

In this paper, we aimed to solve the ferromagnetic spin-1 BC model on a two-dimensional lattice with $q=4$, in the presence of longitudinal crystal and magnetic fields and study the effect of the longitudinal crystal field and magnetic field on the magnetic properties of the spin system by using the IEFT approximation. In addition, in order to compare the results of IEFT, we employed MC simulations as an alternative approach for the same model. The layout of this paper is as follows. In section 2, we present in brief the formulations of the IEFT and MC methods we used. The results and discussions are presented in section 3. Finally, section 4 contains our conclusions.

## 2. Formulation and simulation technique

At first, we discuss how the theory can be formulated within the framework of the EFT with correlations. In order to do this, we consider a two-dimensional lattice that has $N$ identical spins arranged. On the lattice, we select a system that consists of a central spin, labeled 0, and $q$ perimeter spins that are the nearest neighbors of the central spin. The system consists of $(q+1)$ spins, which are independent of the value of $S$. The nearest-neighbor spins are in an effective field produced by the outer spins, which can be determined by the condition that the thermal average of the central spin is equal to that of its nearest-neighbor spins. The Hamiltonian of the spin-1 BC model in a longitudinal magnetic field is given by

$$
H=-J \sum_{\langle i, j\rangle} S_{i}^{z} S_{j}^{z}-D \sum_{i}\left(S_{i}^{z}\right)^{2}-h \sum_{i} S_{i}^{z}, \tag{1}
$$

where the first summation is over the nearest-neighbor pair of spins and the operator $S_{i}^{z}$ takes the values $S_{i}^{z}=\pm 1,0$. $J$, $D$ and $h$ represent the exchange interaction, single-ion anisotropy (i.e. crystal field) and the longitudinal magnetic field, respectively. By the use of the exact Van der Waerden identity [32] for the spin-1 Ising ferromagnetic system with the coordination number $q$, the thermal average of the spin variables at the site $i$ is given by

$$
\left\langle\left\{f_{i}\right\} S_{i}^{z}\right\rangle=\left\langle\left\{f_{i}\right\} \exp \left(J \sum_{\delta}^{q} S_{\delta}^{z}\right) \nabla\right\rangle\left.F(x)\right|_{x=0}, \tag{2}
$$

where $\nabla=\partial / \partial x$ is a differential operator, $\delta$ expresses the nearest-neighbor sites of the central spin and $\{f_{i}\}$ can be any function of the Ising variables as long as it is not a function of the site. The function $F(x)$ depends on the spin value $S$. From equation (2) with $\{f_{i}\}=1$, the thermal average of a central spin can be represented for a square lattice ($q=4$) as

$$
\begin{aligned}
m_{0}= & \left\langle\prod_{\delta=1}^{4}\left[1+S_{\delta}^{z} \sinh (J \nabla)+\left(S_{\delta}^{z}\right)^{2}\{\cosh (J \nabla)-1\}\right]\right\rangle \\
& \left.\times F(x)\right|_{x=0} \tag{3} \\
= & l_{0}+4 k_{1}\left\langle S_{1}\right\rangle+4\left(l_{2}-l_{0}\right)\left\langle S_{1}^{2}\right\rangle+6 l_{1}\left\langle S_{1} S_{2}\right\rangle \\
& +12\left(k_{2}-k_{1}\right)\left\langle S_{1} S_{2}^{2}\right\rangle+6\left(l_{0}-2 l_{2}+l_{3}\right)\left\langle S_{1}^{2} S_{2}^{2}\right\rangle \\
& +4 k_{3}\left\langle S_{1} S_{2} S_{3}\right\rangle+12\left(l_{4}-l_{1}\right)\left\langle S_{1} S_{2} S_{3}^{2}\right\rangle \\
& +12\left(k_{4}-2 k_{2}+k_{1}\right)\left\langle S_{1} S_{2}^{2} S_{3}^{2}\right\rangle+4\left(l_{5}-3 l_{3}+3 l_{2}-l_{0}\right) \\
& \times\left\langle S_{1}^{2} S_{2}^{2} S_{3}^{2}\right\rangle+l_{8}\left\langle S_{1} S_{2} S_{3} S_{4}\right\rangle+4\left(k_{5}-k_{3}\right)\left\langle S_{1} S_{2} S_{3} S_{4}^{2}\right\rangle \\
& +6\left(l_{1}-2 l_{4}+l_{6}\right)\left\langle S_{1} S_{2} S_{3}^{2} S_{4}^{2}\right\rangle \\
& +4\left(k_{6}-3 k_{4}+3 k_{2}-k_{1}\right)\left\langle S_{1} S_{2}^{2} S_{3}^{2} S_{4}^{2}\right\rangle \\
& +\left(l_{0}-4 l_{2}+6 l_{3}-4 l_{5}+l_{7}\right)\left\langle S_{1}^{2} S_{2}^{2} S_{3}^{2} S_{4}^{2}\right\rangle, \tag{4}
\end{aligned}
$$

with the coefficients

$$
\begin{aligned}
& k_{1}=\left.\sinh (J \nabla) F(x)\right|_{x=0}, \\
& k_{2}=\left.\sinh (J \nabla) \cosh (J \nabla) F(x)\right|_{x=0}, \\
& k_{3}=\left.\sinh ^{3}(J \nabla) F(x)\right|_{x=0}, \\
& k_{4}=\left.\cosh ^{2}(J \nabla) \sinh (J \nabla) F(x)\right|_{x=0}, \\
& k_{5}=\left.\sinh ^{3}(J \nabla) \cosh (J \nabla) F(x)\right|_{x=0}, \\
& k_{6}=\left.\cosh ^{3}(J \nabla) \sinh (J \nabla) F(x)\right|_{x=0}, \\
& l_{0}=F(0), \\
& l_{1}=\left.\sinh ^{2}(J \nabla) F(x)\right|_{x=0}, \\
& l_{2}=\left.\cosh (J \nabla) F(x)\right|_{x=0}, \\
& l_{3}=\left.\cosh ^{2}(J \nabla) F(x)\right|_{x=0}, \\
& l_{4}=\left.\sinh ^{2}(J \nabla) \cosh (J \nabla) F(x)\right|_{x=0}, \\
& l_{5}=\left.\cosh ^{3}(J \nabla) F(x)\right|_{x=0}, \\
& l_{6}=\left.\sinh ^{2}(J \nabla) \cosh ^{2}(J \nabla) F(x)\right|_{x=0}, \\
& l_{7}=\left.\cosh ^{4}(J \nabla) F(x)\right|_{x=0}, \\
& l_{8}=\left.\sinh ^{4}(J \nabla) F(x)\right|_{x=0}.
\end{aligned}
$$

These coefficients can be derived from a mathematical identity $\exp (\alpha \nabla) F(x)=F(x+\alpha)$. The function $F(x)$ for the

spin-1 Ising system is given by
$$
F(x)=\frac{2 \sinh [\beta(x+h)]}{2 \cosh [\beta(x+h)]+\exp (-\beta D)}. \tag{5}
$$

Next, the average value of a perimeter spin in the system can be written as follows and it is found as
$$
\begin{aligned}
m_{1} & =\left\langle S_{\delta}^{z}\right\rangle \\
& =\left\langle\exp \left(J S_{0}^{z}+(q-1) A\right) \nabla\right) F(x)\left.\right|_{x=0} \\
& =\left\langle\left[1+S_{0}^{z} \sinh (J \nabla)+\left(S_{0}^{z}\right)^{2}\{\cosh (J \nabla)-1\}\right]\right\rangle \\
& \left.\times F(x+\gamma)\right|_{x=0}. \tag{6}
\end{aligned}
$$

$$
m_{1}=\left\langle S_{1}\right\rangle=a_{1}\left(1-\left\langle S_{0}^{2}\right\rangle\right)+a_{2}\left\langle S_{0}\right\rangle+a_{3}\left\langle S_{0}^{2}\right\rangle \tag{7}
$$

with
$$
\begin{aligned}
& a_{1}=F(\gamma), \\
& a_{2}=\left.\sinh (J \nabla) F(x+\gamma)\right|_{x=0}, \\
& a_{3}=\left.\cosh (J \nabla) F(x+\gamma)\right|_{x=0},
\end{aligned}
$$

where $\gamma=(q-1) A$ is the effective field produced by the $(q-1)$ spins outside the system and $A$ is an unknown parameter to be determined self-consistently.

In the effective-field approximation, the number of independent spin variables describes the considered system. This number is given by the relation $v=\left\langle\left\langle\left(S_{i}^{z}\right)^{2 S}\right\rangle\right.$. As an example for the spin-1 system, $2 S=2$, which means that we have to introduce the additional parameters, $\left\langle\left(S_{\delta}^{z}\right)^{2}\right\rangle$ and $\left\langle\left(S_{0}^{z}\right)^{2}\right\rangle$ resulting from the usage of the Van der Waerden identity for the spin-1 Ising system.
$$
\begin{aligned}
\left\langle\left(S_{0}^{z}\right)^{2}\right\rangle= & \left\langle\prod_{\delta=1}^{4}\left[1+S_{\delta}^{z} \sinh (J \nabla)+\left(S_{\delta}^{z}\right)^{2}\{\cosh (J \nabla)-1\}\right]\right. \\
& \left.\times G(x)\right|_{x=0}. \tag{8}
\end{aligned}
$$

$$
\begin{aligned}
\left\langle S_{0}^{2}\right\rangle= & p_{0}+4 n_{1}\left\langle S_{1}\right\rangle+4\left(p_{2}-p_{0}\right)\left\langle S_{1}^{2}\right\rangle \\
& +6 p_{1}\left\langle S_{1} S_{2}\right\rangle+12\left(n_{2}-n_{1}\right)\left\langle S_{1} S_{2}^{2}\right\rangle \\
& +6\left(p_{0}-2 p_{2}+p_{3}\right)\left\langle S_{1}^{2} S_{2}^{2}\right\rangle+4 n_{3}\left\langle S_{1} S_{2} S_{3}\right\rangle \\
& +12\left(p_{4}-p_{1}\right)\left\langle S_{1} S_{2} S_{3}^{2}\right\rangle \\
& +12\left(n_{1}-2 n_{2}+n_{4}\right)\left\langle S_{1} S_{2}^{2} S_{3}^{2}\right\rangle \\
& +4\left(p_{5}-3 p_{3}+3 p_{2}-p_{0}\right)\left\langle S_{1}^{2} S_{2}^{2} S_{3}^{2}\right\rangle \\
& +p_{8}\left\langle S_{1} S_{2} S_{3} S_{4}\right\rangle+4\left(n_{5}-n_{3}\right)\left\langle S_{1} S_{2} S_{3} S_{4}^{2}\right\rangle \\
& +6\left(p_{1}-2 p_{4}+p_{6}\right)\left\langle S_{1} S_{2} S_{3}^{2} S_{4}^{2}\right\rangle \\
& +4\left(n_{6}-3 n_{4}+3 n_{2}-n_{1}\right)\left\langle S_{1} S_{2}^{2} S_{3}^{2} S_{4}^{2}\right\rangle \\
& +\left(p_{0}-4 p_{2}+6 p_{3}-4 p_{5}+p_{7}\right)\left\langle S_{1}^{2} S_{2}^{2} S_{3}^{2} S_{4}^{2}\right\rangle \quad(9)
\end{aligned}
$$

with the coefficients
$$
\begin{aligned}
& n_{1}=\left.\sinh (J \nabla) G(x)\right|_{x=0}, \\
& n_{2}=\left.\sinh (J \nabla) \cosh (J \nabla) G(x)\right|_{x=0}, \\
& n_{3}=\left.\sinh ^{3}(J \nabla) G(x)\right|_{x=0}, \\
& n_{4}=\left.\cosh ^{2}(J \nabla) \sinh (J \nabla) G(x)\right|_{x=0},
\end{aligned}
$$

$$
\begin{aligned}
& n_{5}=\left.\sinh ^{3}(J \nabla) \cosh (J \nabla) G(x)\right|_{x=0}, \\
& n_{6}=\left.\cosh ^{3}(J \nabla) \sinh (J \nabla) G(x)\right|_{x=0}, \\
& p_{0}=G(0), \\
& p_{1}=\left.\sinh ^{2}(J \nabla) G(x)\right|_{x=0}, \\
& p_{2}=\left.\cosh (J \nabla) G(x)\right|_{x=0}, \\
& p_{3}=\left.\cosh ^{2}(J \nabla) G(x)\right|_{x=0}, \\
& p_{4}=\left.\sinh ^{2}(J \nabla) \cosh (J \nabla) G(x)\right|_{x=0}, \\
& p_{5}=\left.\cosh ^{3}(J \nabla) G(x)\right|_{x=0}, \\
& p_{6}=\left.\sinh ^{2}(J \nabla) \cosh ^{2}(J \nabla) G(x)\right|_{x=0}, \\
& p_{7}=\left.\cosh ^{4}(J \nabla) G(x)\right|_{x=0}, \\
& p_{8}=\left.\sinh ^{4}(J \nabla) G(x)\right|_{x=0},
\end{aligned}
$$

where the function $G(x)$ is defined by
$$
G(x)=\frac{2 \cosh [\beta(x+h)]}{2 \cosh [\beta(x+h)]+\exp (-\beta D)}. \tag{10}
$$

Corresponding to equation (6),
$$
\begin{aligned}
\left\langle\left(S_{\delta}^{z}\right)^{2}\right\rangle= & \left\langle\left[1+S_{0}^{z} \sinh (J \nabla)+\left(S_{0}^{z}\right)^{2}\{\cosh (J \nabla)-1\}\right]\right\rangle \\
& \left.\times G(x+\gamma)\right|_{x=0}, \tag{11}
\end{aligned}
$$

$$
\left\langle S_{1}^{2}\right\rangle=b_{1}+b_{2}\left\langle S_{0}\right\rangle+\left(b_{3}-b_{1}\right)\left\langle S_{0}^{2}\right\rangle, \tag{12}
$$

with
$$
\begin{aligned}
& b_{1}=G(\gamma), \\
& b_{2}=\left.\sinh (J \nabla) G(x+\gamma)\right|_{x=0}, \\
& b_{3}=\left.\cosh (J \nabla) G(x+\gamma)\right|_{x=0}.
\end{aligned}
$$

When the right-hand sides of equations (3), (6), (8) and (11) are expanded, the multispin correlation functions can be easily obtained. The simplest approximation, and one of the most frequently adopted ones, is to decouple these equations according to
$$
\left\langle S_{i}^{z}\left(S_{j}^{z}\right)^{2} \ldots S_{l}^{z}\right\rangle \cong\left\langle S_{i}^{z}\right\rangle\left\langle\left(S_{j}^{z}\right)^{2}\right\rangle \ldots\left\langle S_{l}^{z}\right\rangle, \tag{13}
$$

for $i \neq j \neq \ldots \neq l$ [33]. The main difference between the method used in this study and the other approximations in the literature emerges in comparison with any DA when expanding the right-hand sides of equations (3), (6), (8) and (11).

For the spin-1 Ising system with $q=4$, taking equations (4), (7), (9) and (12) as the basis, we have derived a set of linear equations of the spin correlation functions that interact in the system. At this point, it has been considered that (i) the correlations depend only on the distance between the spins, (ii) the average value of a central spin and its nearest-neighbor spin (it is labeled as the perimeter spin) is equal to each other and (iii) in the matrix representations of spin operator $\hat{S}$, the spin-1 system has the properties $\left(S_{\delta}^{z}\right)^{3}=S_{\delta}^{z}$ and $\left(S_{\delta}^{z}\right)^{4}=\left(S_{\delta}^{z}\right)^{2}$. Thus, the number of the set of linear equations obtained for the spin-1 Ising system with $q=4$ reduces to 34 linear equations. It would be sufficient to give only some of these equations in this paper, since a

detailed study has already been carried out in our previous works [27–29].

$$
\begin{aligned}
\left\langle S_{0}^{2}\right\rangle= & l_{0}+4 k_{1}\left\langle S_{1}\right\rangle+4\left(l_{2}-l_{0}\right)\left\langle S_{1}^{2}\right\rangle+6 l_{1}\left\langle S_{1} S_{2}\right\rangle \\
& +12\left(k_{2}-k_{1}\right)\left\langle S_{1} S_{2}^{2}\right\rangle+6\left(l_{0}-2 l_{2}+l_{3}\right)\left\langle S_{1}^{2} S_{2}^{2}\right\rangle \\
& +4 k_{3}\left\langle S_{1} S_{2} S_{3}\right\rangle+12\left(l_{4}-l_{1}\right)\left\langle S_{1} S_{2} S_{3}^{2}\right\rangle \\
& +12\left(k_{1}-2 k_{2}+k_{4}\right)\left\langle S_{1} S_{2}^{2} S_{3}^{2}\right\rangle \\
& +4\left(l_{5}-3 l_{3}+3 l_{2}-l_{0}\right)\left\langle S_{1}^{2} S_{2}^{2} S_{3}^{2}\right\rangle+l_{8}\left\langle S_{1} S_{2} S_{3} S_{4}\right\rangle \\
& +4\left(k_{5}-k_{3}\right)\left\langle S_{1} S_{2} S_{3} S_{4}^{2}\right\rangle \\
& +6\left(l_{1}-2 l_{4}+l_{6}\right)\left\langle S_{1} S_{2} S_{3}^{2} S_{4}^{2}\right\rangle \\
& +4\left(k_{6}-3 k_{4}+3 k_{2}-k_{1}\right)\left\langle S_{1} S_{2}^{2} S_{3}^{2} S_{4}^{2}\right\rangle \\
& +\left(l_{0}-4 l_{2}+6 l_{3}-4 l_{5}+l_{7}\right)\left\langle S_{1}^{2} S_{2}^{2} S_{3}^{2} S_{4}^{2}\right\rangle,
\end{aligned}
$$

$$
\begin{aligned}
\left\langle S_{1} S_{0}\right\rangle= & \left(4 l_{2}-3 l_{0}\right)\left\langle S_{1}\right\rangle+4 k_{1}\left\langle S_{1}^{2}\right\rangle+6\left(l_{0}+l_{1}-2 l_{2}+l_{3}\right) \\
& \times\left\langle S_{1} S_{2}^{2}\right\rangle+12\left(k_{2}-k_{1}\right)\left\langle S_{1}^{2} S_{2}^{2}\right\rangle+4 k_{3}\left\langle S_{1} S_{2} S_{3}^{2}\right\rangle \\
& +4\left(l_{5}+3 l_{4}-3 l_{3}+3 l_{2}-3 l_{1}-l_{0}\right) \\
& \times\left\langle S_{1} S_{2}^{2} S_{3}^{2}\right\rangle+12\left(k_{1}-2 k_{2}+k_{4}\right)\left\langle S_{1}^{2} S_{2}^{2} S_{3}^{2}\right\rangle \\
& +l_{8}\left\langle S_{1} S_{2} S_{3} S_{4}^{2}\right\rangle+4\left(k_{5}-k_{3}\right)\left\langle S_{1} S_{2} S_{3}^{2} S_{4}^{2}\right\rangle \\
& +\left(l_{0}+6 l_{1}-4 l_{2}+6 l_{3}-12 l_{4}-4 l_{5}+6 l_{6}+l_{7}\right) \\
& \times\left\langle S_{1} S_{2}^{2} S_{3}^{2} S_{4}^{2}\right\rangle+4\left(k_{6}-3 k_{4}+3 k_{2}-k_{1}\right) \\
& \times\left\langle S_{1}^{2} S_{2}^{2} S_{3}^{2} S_{4}^{2}\right\rangle,\left\langle S_{1} S_{2} S_{0}\right\rangle \\
= & \left(3 l_{0}+6 l_{1}-8 l_{2}+6 l_{3}\right)\left\langle S_{1} S_{2}\right\rangle+4\left(3 k_{2}-2 k_{1}\right) \\
& \times\left\langle S_{1} S_{2}^{2}\right\rangle+4\left(3 k_{1}-6 k_{2}+k_{3}+3 k_{4}\right)\left\langle S_{1} S_{2}^{2} S_{3}^{2}\right\rangle \\
& +4\left(l_{5}+3 l_{4}-3 l_{3}+3 l_{2}-3 l_{1}-l_{0}\right)\left\langle S_{1} S_{2} S_{3}^{2}\right\rangle \\
& +\left(l_{0}+6 l_{1}-4 l_{2}+6 l_{3}-12 l_{4}-4 l_{5}+6 l_{6}+l_{7}+l_{8}\right) \\
& \times\left\langle S_{1} S_{2} S_{3}^{2} S_{4}^{2}\right\rangle+4\left(k_{6}+k_{5}-3 k_{4}-k_{3}+3 k_{2}-k_{1}\right) \\
& \times\left\langle S_{1} S_{2}^{2} S_{3}^{2} S_{4}^{2}\right\rangle,\left\langle S_{1} S_{2} S_{3} S_{0}\right\rangle \\
= & \left(4 l_{5}+12 l_{4}-6 l_{3}+4 l_{2}-6 l_{1}-l_{0}\right)\left\langle S_{1} S_{2} S_{3}\right\rangle \\
& +4\left(k_{1}-3 k_{2}+k_{3}+3 k_{4}\right)\left\langle S_{1} S_{2} S_{3}^{2}\right\rangle \\
& +\left(l_{0}+6 l_{1}-4 l_{2}+6 l_{3}-12 l_{4}-4 l_{5}+6 l_{6}+l_{7}+l_{8}\right) \\
& \times\left\langle S_{1} S_{2} S_{3} S_{4}^{2}\right\rangle+4\left(k_{6}+k_{5}-3 k_{4}-k_{3}+3 k_{2}-k_{1}\right), \\
& \times\left\langle S_{1} S_{2} S_{3}^{2} S_{4}^{2}\right\rangle
\end{aligned}
$$

$$
\begin{aligned}
\left\langle S_{1}\right\rangle & =a_{1}+a_{2}\left\langle S_{0}\right\rangle+\left(a_{3}-a_{1}\right)\left\langle S_{0}^{2}\right\rangle,\left\langle S_{1} S_{2}\right\rangle \\
& =a_{1}\left\langle S_{1}\right\rangle+a_{2}\left\langle S_{1} S_{0}\right\rangle+\left(a_{3}-a_{1}\right)\left\langle S_{1} S_{0}^{2}\right\rangle, \\
\left\langle S_{1}^{2}\right\rangle & =b_{1}+b_{2}\left\langle S_{0}\right\rangle+\left(b_{3}-b_{1}\right)\left\langle S_{0}^{2}\right\rangle, \\
& \vdots \\
\left\langle S_{1}^{2} S_{2}^{2} S_{3}^{2} S_{0}^{2}\right\rangle= & 4\left(n_{1}-3 n_{2}+n_{3}+3 n_{4}\right) \\
& \times\left\langle S_{1} S_{2}^{2} S_{3}^{2}\right\rangle \\
& +\left(4 p_{5}+12 p_{4}-6 p_{3}+4 p_{2}-6 p_{1}-p_{0}\right) \\
& \times\left\langle S_{1}^{2} S_{2}^{2} S_{3}^{2}\right\rangle+4\left(n_{6}+n_{5}-3 n_{4}-n_{3}+3 n_{2}-n_{1}\right) \\
& \times\left\langle S_{1} S_{2}^{2} S_{3}^{2} S_{4}^{2}\right\rangle+\left(p_{0}+6 p_{1}-4 p_{2}+6 p_{3}-12 p_{4}\right. \\
& \left.-4 p_{5}+6 p_{6}+p_{7}+p_{8}\right)\left\langle S_{1}^{2} S_{2}^{2} S_{3}^{2} S_{4}^{2}\right\rangle. \quad(14)
\end{aligned}
$$

If equation (14) is written in the form of a $34 \times 34$ matrix and solved in terms of the variables $x_{i}(i=1,2, \ldots, 34)$ (e.g. $x_{1}=\left\langle S_{0}\right\rangle, x_{2}=\left\langle S_{1} S_{0}\right\rangle, \ldots, x_{34}=\left\langle S_{1}^{2} S_{2}^{2} S_{3}^{2} S_{0}^{2}\right\rangle$ ) of the linear equations, all of the spin correlation functions can be easily determined as functions of the temperature, effective field, crystal field and longitudinal magnetic field, which the other studies in the literature do not include. Since the thermal average of the central spin is equal to that of its nearest-neighbor spins within the present method, the unknown parameter $A$ can be numerically determined by the relation

$$
\left\langle S_{0}\right\rangle=\left\langle S_{1}\right\rangle \quad \text { or } \quad x_{1}=x_{5}. \quad(15)
$$

By solving equation (15) numerically at fixed values of $D / J$ and $h / J$, we have obtained the parameter $A$. Then, we used the numerical values of $A$ to obtain the spin correlation functions $\left\langle S_{0}\right\rangle,\left\langle S_{1} S_{0}\right\rangle,\left\langle S_{1} S_{2} S_{0}\right\rangle,\left\langle S_{0}^{2}\right\rangle$ (quadrupole moment), $\left\langle S_{1}^{2} S_{0}^{2}\right\rangle$ (biquadrupole moment) and so on, which can be found from equation (14). Note that $A=0$ is always the root of equation (15), corresponding to the disordered state of the system. The nonzero root of $A$ in equation (15) corresponds to the long-range order state of the system. Once the spin correlation functions have been evaluated, we can state how to calculate the thermodynamic parameters like the susceptibility, internal energy and specific heat of the spin-1 BC model on a square lattice.

The susceptibility curve can show the phase transition properties, particularly the critical temperature of the system. The longitudinal susceptibility for the system that describes the characteristics of the change of magnetization with magnetic field can be determined from the relation

$$
\chi=\frac{\partial\left\langle S_{0}\right\rangle}{\partial h}. \quad(16)
$$

The internal energy $U$ per site of the system can be obtained easily from the thermal average of the Hamiltonian in equation (1). Thus, the internal energy is given by

$$
-\frac{U}{N J}=q\left\langle S_{0} S_{1}\right\rangle+\frac{D}{J}\left\langle S_{0}^{2}\right\rangle+\frac{h}{J}\left\langle S_{0}\right\rangle, \quad(17)
$$

where the correlation functions $\left\langle S_{0}\right\rangle,\left\langle S_{0}^{2}\right\rangle$ and $\left\langle S_{1} S_{0}\right\rangle$ are obtained from equation (14) for the spin-1 system. With the use of equation (17), the specific heat of the system can be determined from the relation

$$
C_{h}=\left(\frac{\partial U}{\partial T}\right)_{h}. \quad(18)
$$

The formulations of EFT with correlations for the spin-1 BC model on a square lattice have been given above. For the same model, Monte Carlo simulations have also been carried out. We employed the standard single-spin-flip Monte Carlo algorithm of Metropolis et al [34] to simulate the system described by the Hamiltonian in equation (1) on an $L \times L$ square lattice with periodic boundary conditions and data were obtained with $L=64$. A number of additional simulations were performed for $L=128$, but no significant differences were found from the results presented here. We selected $J>0$, which means that the interaction between the nearest-neighbor spins is ferromagnetic. Configurations were generated by selecting the sites in a sequence through the lattice and making single-spin-flip attempts, which were accepted or rejected according to the Metropolis algorithm. Data were generated with 25000 Monte Carlo steps per

![](./images/811858742487285761_1.jpg)

![](./images/811858742487285761_2.jpg)

![](./images/811858742487285761_3.jpg)

Figure 1. Temperature dependence of magnetization for a spin-1 system with a crystal field on a square lattice: (a) IEFT approximation and (b) MC study. Dotted curves denote the magnetization curves in the absence of a magnetic field ($h/J=0$) with selected values of the crystal field $D/J$. Solid curves are plotted for $D/J=-0.5$. (c) Temperature dependence of the fourth order magnetization cumulant $V_L$ for the linear lattice sizes of $L=8, 16, 32, 64$ and 128. The dotted line refers to the transition temperature.

site after discarding the first 2500 steps. Ten independent MC runs of 25 000 MC steps per spin have been performed at each temperature. We tested the reliability of the data of our program by using a ground-state diagram that was investigated in previous studies [9].

The longitudinal magnetization per spin is a sum over each spin on the lattice and it can be determined from the relation

$$
m=\frac{1}{L^{2}}\left\langle\sum_{i=1}^{N} S_{i}^{z}\right\rangle, \tag{19}
$$

and the relationship of the magnetic susceptibility to the fluctuations of the magnetization can be written with the help of equation (19) as

$$
\chi=\frac{\left\langle m^{2}\right\rangle-\langle m\rangle^{2}}{k_{\mathrm{B}} T}. \tag{20}
$$

The internal energy $U$ per site of the system can be obtained easily by computing the average energy of each spin on the lattice. Thus, the internal energy of the system is the average of the Hamiltonian in equation (1).

$$
U=\frac{1}{L^{2}}\langle H\rangle, \tag{21}
$$

and finally, the specific heat of the system can be determined from equation (18).

In order to locate the transition temperature of the system more accurately, we computed the fourth order cumulant of magnetization $V_L(L, T)$ with various lattice sizes $L=8, 16, 32, 64$ and 128. The fourth order cumulant of the magnetization, i.e. the Binder cumulant [35], for a spin cluster is defined by

$$
V_{L}(L, T)=1-\frac{\left\langle M^{4}\right\rangle}{3\left\langle M^{2}\right\rangle^{2}}, \tag{22}
$$

where $\langle M^2\rangle$ and $\langle M^4\rangle$ denote the second and fourth moments of the magnetization in that cluster, respectively. The cumulant approaches the value $2/3$ in the thermodynamic limit at temperatures $T<T_{\rm c}$, while it tends to zero, reflecting a Gaussian distribution of the magnetization histogram, at $T>T_{\rm c}$. At $T=T_{\rm c}$, $V_L(L, T)$ acquires a nontrivial value, the critical Binder cumulant $V_L^*$.

### 3. Numerical results and discussions

In this section, we shall present the numerical results for the longitudinal magnetization, hysteresis loop, susceptibility,

![](./images/811858742487285761_4.jpg)

Figure 2. The hysteresis loops for a square lattice of the spin-1 system when the crystal field is selected as $D/J=-0.5$ with four values of temperature $k_{\text{B}}T/J$. (a) IEFT approximation; (b) MC study results. (c) IEFT and (d) MC simulation results for $k_{\text{B}}T/J=1$ with four values of $D/J$.

specific heat and phase diagram of the spin-1 system on a square lattice. In our effective-field theory approximation, equation (14) is written in the form of a $34\times34$ matrix and all of the spin correlation functions are obtained as a function of temperature, the longitudinal magnetic field and the effective field produced by outer spins in the cluster, respectively. Then, by solving the self-consistent relation (15), we obtain the numerical values of $A$. If we insert the numerical values of $A$ obtained from equation (15) at selected values of $h/J$ for a fixed value of $D/J$ into the spin correlation function $\langle S_{0}\rangle$ obtained from the $34\times34$ matrix, we can find the temperature dependence of $\langle S_{0}\rangle$ (it is labelled as the longitudinal magnetization $m(m_{0}=m_{1}=m)$) for the spin-1 system on a square lattice.

The temperature dependence of longitudinal magnetization within the framework of IEFT approximation and MC study is plotted in figures 1(a) and (b), respectively. The numbers on the solid and dotted curves are the values of the longitudinal magnetic field and the crystal field. It can be seen from both figures that in the case of $h/J=0$, the longitudinal magnetization $m$ falls rapidly from its saturation magnetization value $(m=1.0)$ to zero as the temperature increases and decreases continuously in the vicinity of the transition temperature and vanishes at $T=T_{\text{c}}$. This is the second-order phase transition. According to our introduced EFT approximation result, we clearly find that the transition temperature of the spin-1 system for the fixed values of $D/J=0$ and $h/J=0$ is $k_{\text{B}}T_{\text{c}}/J=1.9643$. This value is a new result not found in the literature. Our result of 1.9643 on a square lattice is much closer to those obtained by the BA [5], CVM [8], CEFT [22] and EBPA [26] than those obtained by the EFT [19], a new type of cluster theory [23] and the DA [24].

In our MC simulations, we estimated the transition temperature with the help of the fourth order magnetization cumulant $V_{L}$ curves. The crossing point of the curves with $L=8,16,32,64$ and 128 gives the value of the transition temperature as $k_{\text{B}}T_{\text{c}}/J=1.690$ as seen from figure 1(c). This result agrees with the SE analysis [36], but it is quite different from our introduced EFT approximation result. For comparison, the transition temperatures $k_{\text{B}}T_{\text{c}}/J$ at $D/J=0$ and $h/J=0$ obtained by several methods and the present work for the spin-1 BC model on a square lattice are given in table 1.

As can be seen from figures 1(a) and (b), when we apply a longitudinal magnetic field $(h>0$ or $h<0)$ to the system, the magnetization value decreases slowly from its saturation magnetization value as the temperature increases. Remaining magnetizations are getting bigger as the longitudinal magnetic field increases. In the presence of an external field (for

![](./images/811858742487285761_5.jpg)

Figure 3. The susceptibility for a square lattice of the spin-1 system when the crystal field is selected as $D/J=0$ and $-0.5$ with three values of the magnetic field $h/J$. (a) IEFT approximation; (b) MC simulation results. The effect of the crystal field on the susceptibility curves of the system by (c) IEFT, (d) MC simulation for $h/J=0$ with several values of $D/J$.

<table>
<caption>Table 1. Transition temperature $k_{\text{B}}T_{\text{c}}/J$ at $D/J=0$ and $h/J=0$ obtained by several methods and the present work for a square lattice.</caption>
<thead>
<tr>
<th>CVM</th>
<th>CEFT</th>
<th>CT</th>
<th>RG</th>
<th>SE</th>
<th>BA</th>
<th>EBPA</th>
<th>EFT</th>
<th>DA</th>
<th colspan="2">Present work</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>IEFT</th>
<th>MC</th>
</tr>
</thead>
<tbody>
<tr>
<td>2.065</td>
<td>2.056</td>
<td>2.1436</td>
<td>1.46</td>
<td>1.688</td>
<td>2.065</td>
<td>1.915</td>
<td>2.188</td>
<td>2.117</td>
<td>1.9643</td>
<td>1.690</td>
</tr>
</tbody>
</table>

example $h/J=1.0$ or $2.0)$ magnetization curves of IEFT and MC are in excellent agreement. From our calculation, we can also see that the longitudinal magnetization curves are symmetric for both positive and negative magnetic field values. These results are in a good agreement with those of previous works [28, 29, 37-40], but they are quite different from those of [27, 41, 42] without applying any longitudinal magnetic field. In figures 1(a) and (b), the effect of the crystal field $D/J$ on the magnetization process has also been shown. As the value of $D/J$ decreases then, the value of the transition temperature $k_{\text{B}}T_{\text{c}}/J$ also decreases. According to IEFT (see figure 1(a)), when the value of the crystal field is selected as $D/J<-1$, e.g. $D/J=-1.5$, the magnetization of the system shows a discontinuous behavior. We did not encounter this behavior in our MC simulation (figure 1(b)).

We have also investigated the influence of a longitudinal magnetic field $h$ on the longitudinal magnetization process at the fixed values of temperature and the crystal field for the spin-1 BC model [43] on a square lattice. In order to present hysteresis loops, we selected four typical temperatures and four crystal field values in figure 2. As we can see from figure 2, the details of the hysteresis loops depend on the temperature and crystal field. At the fixed value of $D/J=-0.5$, the hysteresis loops of a square lattice for the spin-1 system are shown in figures 2(a) and (b). From figures 2(a) and (b) we can see that the hysteresis loops do not occur at temperatures above the transition temperature $k_{\text{B}}T_{\text{c}}/J$ and the type of hysteresis loops becomes narrower as the temperature increases below the transition temperature. Then the hysteresis loop disappears when the temperature is higher than the transition temperature as in [28, 37-39]. When the temperature is fixed as $k_{\text{B}}T/J=1$, the hysteresis loops for a square lattice are plotted in figures 2(c) and (d). As seen from these figures, the type of hysteresis loops becomes narrower as the absolute value of the crystal field increases. Then the hysteresis loop disappears when the absolute value of the

![](./images/811858742487285761_6.jpg)

Figure 4. The specific heat for the spin-1 system when the crystal field is selected as $D/J=0$ with four values of the magnetic field $h/J$. (a) IEFT approximation and (b) MC simulation results. The effect of the crystal field on the specific heat curves of the system by (c) IEFT and (d) MC simulation for $h/J=0$ with several values of $D/J$.

crystal field is large enough. Namely, these results show that the hysteresis loops at low temperatures are considered to originate from the competing effects between the exchange interaction term of the nearest-neighbor pair of spins and the Zeeman energy term in the Hamiltonian of the spin-1 system.

In figures 3(a) and (b), the numerical results of the susceptibility for the spin-1 system on a square lattice are given in the $(\chi, k_{\rm B}T/J)$ plane for the three selected values of $h/J=0, 0.1$ and $0.5$ when the crystal field is selected as $D/J=0$ and $-0.5$. From figures 3(a) and (b), we can clearly see a peak at the critical temperature that corresponds to the divergence of the longitudinal susceptibility for $h/J=0$. Furthermore, as can be seen from the figures, in the absence of the longitudinal magnetic field $(h/J=0)$, the curve of the susceptibility rapidly increases and expresses a peak at the phase transition temperature and then rapidly decreases as the temperature increases. In the presence of a longitudinal magnetic field, the phase transition is not observed, and the stronger the longitudinal magnetic field, the smaller is the susceptibility, reflecting the fact that the longitudinal magnetization is weaker. In figures 3(c) and (d), the longitudinal susceptibility is plotted in the absence of a longitudinal magnetic field with selected values of $D/J$. We found that the critical temperatures obtained by MC are always lower than those obtained by IEFT for the common values of $D/J$. Here, it is also shown that the critical temperature value $k_{\rm B}T_{\rm c}/J$ decreases as the absolute value of the crystal field increases, and according to our IEFT approximation results, the critical temperature has a double valued form for $D/J<-1$. Such a behavior has not been observed in our MC simulations. This difference is analyzed in detail by investigating the phase diagram of the system in the $(k_{\rm B}T_{\rm c}/J, D/J)$ plane with $h/J=0$ (see figure 5).

In order to plot the specific heat curve of the system, we must know the internal energy. From the correlation functions in equation (14) and the definition (17), the internal energy can be calculated within the framework of the IEFT approximation. Furthermore, using the relation (21) one can easily obtain the internal energy of the system by applying MC simulations. Using the numerical derivative of the internal energy with respect to the temperature, we obtain the behavior of the specific heat with temperature for the selected values of the crystal field and the longitudinal magnetic field. The results are given in figure 4. We can see from figures 4(a) and (b) that in the case of $h/J=0$, the specific heat curve of the spin-1 system exhibits a second-order phase transition at the Curie temperature $k_{\rm B}T_{\rm c}/J$ and rapidly decreases as the temperature increases; on the other hand, in the case of

**Table 2.** The tricritical point $D_{\mathrm{t}}/J$ and the corresponding temperature $k_{\mathrm{B}}T_{\mathrm{t}}/J$ obtained by several methods and the methods used in the present work.

<table>
<thead>
<tr>
<th></th>
<th>RG</th>
<th>CVM</th>
<th>MCRG</th>
<th>FSS</th>
<th>EBPA</th>
<th>EFT</th>
<th colspan="2">Present work</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>IEFT</th>
<th>MC</th>
</tr>
</thead>
<tbody>
<tr>
<td>$D_{\mathrm{t}}/J$</td>
<td>−1.972</td>
<td>−1.903</td>
<td>−1.9655</td>
<td>−1.9655</td>
<td>−1.906</td>
<td>−1.880</td>
<td>−1.901</td>
<td>−1.974</td>
</tr>
<tr>
<td>$k_{\mathrm{B}}T_{\mathrm{t}}/J$</td>
<td>0.58</td>
<td>0.881</td>
<td>0.610</td>
<td>0.609</td>
<td>0.846</td>
<td>1.0</td>
<td>0.753</td>
<td>0.56</td>
</tr>
</tbody>
</table>

![](./images/811858742487285761_7.jpg)

**Figure 5.** Phase diagram ($k_{\mathrm{B}}T_{\mathrm{c}}/J$ versus $D/J$ plot) of the spin-1 Ising ferromagnetic system on a square lattice ($q=4$) was plotted by using the two methods used in the present work (IEFT and MC) and some other methods. The solid curves represent our results of the IEFT and MC simulations. The white circles on each curve denote the tricritical points.

$h/J\neq0$, there is no phase transition observed in the system. In order to investigate the crystal field dependence in the absence of any longitudinal magnetic field, the behavior of the specific heat is shown in figures 4(c) and (d) for several values of the crystal field $D/J$. For the selected values of $D/J$, the specific heat curves exhibit a second-order phase transition at the Curie temperature. When the $D/J$ value draws close to the value of the tricritical point $D_{\mathrm{t}}/J$, the discontinuity character of the specific heat begins to increase in height and a jumping in the specific heat curve at the transition point appears. This behavior can be interpreted as a competition between the exchange interaction, which tries to align the spins in the same direction, and the crystal field, which has the tendency to destroy this alignment.

IEFT and MC results are formally in good agreement with each other and some of the other methods [8, 19, 26, 39, 43, 44] in terms of the shapes of the longitudinal susceptibility and specific heat curves. As a result, by comparing the curves for both the susceptibility and specific heat for the nonzero values of $h/J$, we see that the phase transition has been removed in the system. All the calculated properties show the proper thermodynamic behavior over the whole range of temperatures, including the ground-state behavior ($\chi\rightarrow0$ and $C\rightarrow0$ for $T\rightarrow0$) and the thermal stability condition ($C_{h}\geqslant0$).

Finally, we have evaluated the phase diagram of the spin-1 BC model on the $(k_{\mathrm{B}}T_{\mathrm{c}}/J,D/J)$ plane and we have compared our results with those of the other methods in the literature. First, the phase diagram of the spin-1 system with the crystal field parameter $D/J$ is plotted within the framework of effective field theory with correlations. In order to plot this curve, we assumed $\langle S_{0}\rangle=\langle S_{1}\rangle$ and the effective field $\gamma$ is very small in the vicinity of $k_{\mathrm{B}}T_{\mathrm{c}}/J$ and solved the set of linear equations numerically in equation (14) using the self-consistent relation corresponding to equation (15). Then, MC results for the transition temperature $k_{\mathrm{B}}T_{\mathrm{c}}/J$ in the thermodynamic limit were estimated for each value of the anisotropy parameter $D/J$ by using the peaks of the longitudinal susceptibility.

Solid lines in figure 5 show the variation of the critical temperature $k_{\mathrm{B}}T_{\mathrm{c}}/J$ with the crystal field $D/J$ for the spin-1 Ising system with $q=4$ by using the IEFT method and the MC simulation. As shown in table 1, the IEFT result for the critical temperature value at $D/J=0$ is found to be $k_{\mathrm{B}}T_{\mathrm{c}}/J=1.9643$. On the other hand, according to our MC simulations the critical temperature value is estimated to be $k_{\mathrm{B}}T_{\mathrm{c}}/J=1.690$. Furthermore, the solid line related to the IEFT on the plot shows that, for the values of $D/J<-1$, the transition temperature $k_{\mathrm{B}}T_{\mathrm{c}}/J$ becomes doubles valued. This is an expected result as shown in figures 1(a) and 3(c). The point $D_{\mathrm{t}}/J,T_{\mathrm{t}}/J$ is the tricritical point that separates the first-order line from the continuous phase transition line. The value of the critical crystal field $D_{\mathrm{t}}/J$ of the IEFT is equal to $-1.901$. The lower solution of the double-valued region between $D_{\mathrm{t}}/J=-1.901$ and $D/J=-1$ just corresponds to the unstable solution, and below the point $D_{\mathrm{t}}/J$, the $k_{\mathrm{B}}T_{\mathrm{c}}/J$ curve for the spin-1 system does not have a physical meaning. But our MC simulations show that there is no double valued form of $k_{\mathrm{B}}T_{\mathrm{c}}/J$ for any value of $D/J$. At this point, one should notice that the solid line related to the IEFT in figure 5 is clearly different from those of [26]. Because the EBPA is a Bethe–Peierls-like approximation [20] and the double-valued region does not appear in the $k_{\mathrm{B}}T_{\mathrm{c}}/J$ curve of the spin-1 Ising system as we obtained from our MC simulations. In table 2, we compared the values of $D_{\mathrm{t}}/J$ and $k_{\mathrm{B}}T_{\mathrm{t}}/J$ at the tricritical point with the results obtained by some of the other methods in the literature. We can see from table 2 that the IEFT result $D_{\mathrm{t}}/J=-1.901$ is much closer to the results of the EBPA [26] and CVM [8] than those obtained by the other approximation methods in table 2. On the other hand, our MC simulation result $D_{\mathrm{t}}/J=-1.974$ is much closer to the results of RG [16], MCRG [9] and FSS [12] given in the same table.

It would be useful to denote that the critical single-ion anisotropy for the BC model is universally found to be $D_{\mathrm{t}}/qJ=-0.47$ [19, 23, 24]. The phenomenon comes from the fact that the spin state at $T=0$ K may change from the $S_{i}^{z}=\pm1$ state to the $S_{i}^{z}=0$ state at the critical value of $D/J=-q/2$. Our result $D_{\mathrm{t}}/qJ=-0.475$ of the IEFT on a square lattice shows just a small deflection from this value.

## 4. Conclusions

In this paper, we have applied an IEFT and MC simulation to study the spin-1 BC model on a square lattice. In the IEFT, we can easily obtain the multispin correlation functions as functions of the temperature, effective field, longitudinal crystal field and magnetic field without using any kind of DA. This method is superior to conventional mean field theory and the EFT theory in the literature. In order to obtain credible results, we have also performed MC simulations and we have discussed the influence of the longitudinal magnetic field on the magnetization, susceptibility and specific heat of the considered system. A number of interesting phenomena, originating from the temperature, crystal field and longitudinal magnetic field, were found. Furthermore, we have made a detailed comparison of the results obtained by the two methods with those of other methods in the literature.

The effects of the crystal field and the longitudinal magnetic field on the magnetization, susceptibility and specific heat have been investigated in detail. In this regard, the IEFT and MC methods give similar results. It was found that the critical temperatures obtained by MC are always lower than those obtained by the IEFT for the common values of $D/J$. The critical temperature of the system obtained by the IEFT is much closer to those obtained by the Bethe approximation, the cluster variational method, the CEFT and the EBPA than to those obtained by the EFT, a new type of cluster theory and the decoupling approximation. However, the MC result agrees with the SE analysis, but is quite different from the IEFT result.

In addition, in order to bring into sharp relief how the thermodynamic quantities change with the temperature and crystal field, we have also evaluated the phase diagram of the spin-1 system with $q=4$ in the $(k_{\text{B}}T_{\text{c}}/J, D/J)$ plane at $h/J=0$. In the negative crystal field range, the first-order phase transition occurs when the crystal field $D/J$ is sufficiently negative and this critical value obtained by the IEFT is larger than that obtained by MC simulation. On the other hand, the value of $D_{\text{t}}/J$ at the tricritical point of the IEFT is much closer to the results of the EBPA and the CVM than those obtained by the other approximation methods in table 2. MC results for $D_{\text{t}}/J$ are more or less equal to those obtained by the RG method, the FSS methods and the MCRG method.

We believe that the IEFT theory and the MC simulation method can also be applied to more complicated model systems, such as the Ising ferromagnetic systems in the presence of the biquadratic exchange interaction, crystal field and transverse fields. This should be done in a future work.

## References

[1] Blume M 1966 *Phys. Rev.* **141** 517
[2] Capel H W 1966 *Physica* **32** 966
[3] Lawrie I D and Sarback S 1988 *Phase Transitions and Critical Phenomena* vol 9 ed C Domb and J L Lebowitz (London: Academic Press)
[4] Lock S L and Lee B S 1984 *Phys. Status Solidi* b **124** 593
[5] Tanaka Y and Uryu N 1981 *J. Phys. Soc. Japan* **50** 1140
[6] Brankov J G, Przystawa J and Praveczki E 1972 *J. Phys. C: Solid State Phys.* **5** 3387
Saul D M, Wortis M and Stauffer D 1974 *Phys. Rev. B* **9** 4964
[7] Tanaka M and Takahashi K 1979 *Phys. Status Solidi* b **93** K85
[8] Ng W M and Barry J H 1978 *Phys. Rev. B* **17** 3675
Tucker J W, Balcerzak T, Gzik M and Sukiennicki A 1998 *J. Magn. Magn. Mater.* **187** 381
[9] Jain A K and Landau D P 1980 *Phys. Rev. B* **22** 445
Kimel J D, Rikvold P A and Wang Y L 1992 *Phys. Rev. B* **45** 7237
Selke W and Yeomans J 1983 *J. Phys. A: Math. Gen.* **16** 2789
Landau D P and Swendsen R H 1985 *Phys. Rev. B* **33** 7700
[10] de Alcantara Bonfim O F and Obcemea C H 1986 *Z. Phys. B: Condens. Matter* **64** 469
[11] Wilding N B and Nielaba P 1996 *Phys. Rev. E* **53** 926
Silva C J, Caparica A A and Plascak J A 2006 *Phys. Rev. E* **73** 036702
[12] Beale P D 1986 *Phys. Rev. B* **33** 1717
[13] Alcaraz F C, de Felicio J R D, Köberle R and Stilck J F 1985 *Phys. Rev. B* **32** 7469
[14] Balboa D B and de Felicio J R D 1987 *J. Phys. A: Math. Gen.* **20** L207
[15] Gehlen J V 1990 *J. Phys. A: Math. Gen.* **24** 5371
[16] Berker A N and Wortis M 1976 *Phys. Rev. B* **14** 4946
Burkhardt T W 1976 *Phys. Rev. B* **14** 1196
Burkhardt T W and Knops H J F 1977 *Phys. Rev. B* **15** 1602
[17] de Alcantara Bonfim O F 1985 *Physica* A **130** 367
[18] de Oliveria S M, de Oliveria P M C and de Sa Barreto F C 1995 *J. Stat. Phys.* **78** 1619
[19] Siqueira A E and Pittalidi I P 1986 *Physica* A **138** 592
[20] Chakraborty K G 1984 *Phys. Rev. B* **29** 1454
[21] Jiang X F, Li J L and Zhong J L 1993 *Phys. Rev. B* **47** 827
[22] Kaneyoshi T and Tamura I 1982 *Phys. Rev. B* **25** 4679
Honmura R 1984 *Phys. Rev. B* **30** 348
Kaneyoshi T 1993 *Acta Phys. Pol. A* **83** 703
Kaneyoshi T 1999 *Physica* A **269** 344
Kaneyoshi T 1999 *Physica* A **269** 357
Kaneyoshi T 2000 *Physica* A **286** 518
[23] Zernike F 1940 *Physica* **7** 597
[24] Du A, Yü Y Q and Liu H J 2003 *Physica* A **320** 387
Du A, Liu H J and Yü Y Q 2004 *Phys. Status Solidi* b **241** 175
Zhang Q, Wei G, Xin Z and Liang Y 2004 *J. Magn. Magn. Mater.* **280** 14
[25] Polat H, Akıncı Ü and Sökmen İ 2003 *Phys. Status Solidi* b **240** 189
[26] Canpolat Y, Torgürsül A and Polat H 2007 *Phys. Scr.* **76** 597
[27] Polat H, Kocakaplan Y and Kanbur U 2008 *Int. J. Mod. Phys. B* in press
[28] Binder K (ed) 1986 *Monte Carlo Methods in Statistical Physics* (Berlin: Springer)
Binder K (ed) 1992 *Monte Carlo Methods in Condensed Matter Physics* (Berlin: Springer)
Landau D P and Binder K (eds) 2000 *A Guide to Monte Carlo Simulations in Statistical Physics* (Cambridge: Cambridge University Press)
[29] Goldenfeld N 1992 *Lectures on Phase Transitions and the Renormalization Group* (Reading, MA: Addison-Wesley)
[30] Balcerzak T 2002 *J. Magn. Magn. Mater.* **246** 213
Callen H B 1963 *Phys. Lett.* **4** 161
Suzuki M 1965 *Phys. Lett.* **19** 267
[31] Tamura I and Kaneyoshi T 1981 *Prog. Theor. Phys.* **66** 1892
[32] Metropolis N, Rosenbluth A W, Rosenbluth M N, Teller A H and Teller E 1953 *J. Chem. Phys.* **21** 1087
[33] Binder K 1981 *Phys. Rev. Lett.* **47** 693
[34] Fox P F and Guttman A J 1973 *J. Phys. C: Math. Gen.* **6** 913
Adler J and Enting I G 1984 *J. Phys. A: Math. Gen.* **17** 2233
Blote H W J and Nightingale M P 1985 *Physica* A **134** 274
Burkhardt T W and Swendsen R H 1976 *Phys. Rev. B* **13** 3071
[35] Jiang W, Bai B D and Wei G Z 2005 *Physica* A **354** 301

[38] Jiang W and Bai B D 2005 *J. Appl. Phys.* **97** 10B307
Jiang W and Bai B D 2006 *Phys. Status Solidi* b **243** 2892

[39] Mancini F and Naddeo A 2006 *Phys. Rev. E* **74** 061108
Mancini F and Mancini F P 2008 *Condens. Matter Phys.* **11** 543

[40] Wei G Z, Liang Y Q, Zhang Q and Xin Z H 2004 *J. Magn. Magn. Mater.* **271** 246

[41] Jiang W, Guo L Q, Wei G Z and Du A 2001 *Physica* B **307** 15
Jiang W and Wei G Z 2000 *Physica* A **284** 215
Jiang W, Wei G Z and Xin Z H 2000 *J. Magn. Magn. Mater.* **217** 225

Jiang W, Wei G Z and Xin Z H 2000 *Phys. Status Solidi* b **221** 759

[42] Htoutou K, Benaboud A, Ainane A and Saber M 2004 *Physica* A **338** 479
Kaneyoshi T 1987 *J. Phys. Soc. Japan* **56** 2675
Kaneyoshi T 1988 *Physica* A **153** 556
Kaneyoshi T, Jascur M and Tomczak P 1992 *J. Phys. A: Condens. Matter* **4** L653
Bobak A and Jurcisin M 1997 *Physica* A **240** 647

[43] Balcerzak T 2003 *Physica* A **317** 213

[44] Kaneyoshi T and Jascur M 1992 *Phys. Rev. B* **46** 3374
Micnas R 1979 *Physica* A **98** 403