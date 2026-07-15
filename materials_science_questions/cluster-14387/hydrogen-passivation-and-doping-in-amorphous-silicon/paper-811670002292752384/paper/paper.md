# CALCULATION OF THE ELECTRONIC STRUCTURE OF SILICON NANOCRYSTALS

NICOLA A. HILL AND K. BIRGITTA WHALEY

Department of Chemistry, University of California, Berkeley, California 94720

## Abstract

The densities of states for Si nanocrystals with diameters between 15 and $35\ \text{\AA}$ are calculated using a time-dependent algorithm within the tight-binding approximation [1]. The calculated effects of surface termination and surface relaxation on the electronic properties of Si are shown. The variation in band-gap with cluster size is calculated for clusters up to $60\ \text{\AA}$ in diameter.

## 1. INTRODUCTION

Nanometer-sized silicon structures photoluminesce efficiently in the visible part of the spectrum[2]. This observation has prompted many theoretical[3] and experimental[4] studies, both exploring technological applications, and investigating the fundamental physical and electronic properties. The mechanism for the photoluminescence is still not clearly understood.

Recently, the synthesis of size-selective Si nanocrystals[5] has been achieved, which has allowed changes in band structure with the extent of spatial confinement to be measured systematically. In this paper we complement these experiments with a theoretical investigation of the electronic properties of Si nanocrystals.

This paper is organized as follows. Section 2 describes the theoretical technique used in our calculations. Section 3 illustrates the effect of surface termination on the cluster electronic structure. The calculated variation in band gap with cluster size is discussed in Section 4. Our on-going work is described in Section 5.

## 2. THEORETICAL TECHNIQUE

Recent theoretical studies have employed a number of different techniques including density functional theory, pseudopotentials and tight-binding calculations[3]. We have developed a time-dependent tight-binding method[1] which has two significant advantages over conventional tight-binding methods. First, the size of the cluster is less restricted by computer memory limitations than in methods which diagonalize the Hamiltonian matrix directly. We can calculate the electronic properties of clusters containing up to $10^6$ atoms, whereas other techniques are restricted to around 2,000 atoms. Second, the method can be extended to study excitonic states directly, allowing excited state properties such as absorption energies to be predicted accurately. Other workers have either dealt with the electron-hole interaction perturbatively, or used the effective mass approximation. Work on excited-state calculations is in progress. The technique is summarized below, and is described more completely in Ref. [1].

Mat. Res. Soc. Symp. Proc. Vol. 358 ©1995 Materials Research Society

Time-evolution of the electronic wavefunction, $\Psi$, is calculated using the time-dependent Schrödinger equation with a tight-binding Hamiltonian $\mathcal{H}$.

$$
\Psi(t)=e^{-i \mathcal{H} t} \Psi(0) \tag{1}
$$

The tight-binding parameters are obtained by fitting to the symmetry points of the bulk band structure using a basis of five atomic orbitals on each atom[6]. Hückel parameters between the semiconductor surface atoms and additional ligand atoms are used to simulate ligands attached to the cluster surface. The parameters for the cluster-ligand interactions are obtained using the Gaussian-92 program[7] and are listed in Table I.

Table 1: Hamiltonian matrix elements for Si-H, obtained using Gaussian-92.

$$
\begin{align*}
<H_{1 s}|\mathcal{H}| H_{1 s}> &= -13.6 eV \\
<H_{1 s}|\mathcal{H}| S i_{3 s}> &= -9.29 eV \\
<H_{1 s}|\mathcal{H}| S i_{3 p_{z}}> &= -4.76 eV
\end{align*}
$$

The eigenvalues and eigenfunctions are obtained from the time-evolved wavefunction by Fourier Transformation. The local density of states (DOS) on an orbital, $i$, is given by

$$
n_{i}(E)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{i E t}<\psi_{i}(0)\left|e^{-i H t}\right| \psi_{i}(0)>d t \tag{2}
$$

where $\psi_{i}(0)$ is the initial wavefunction, chosen to be localized on orbital $i$. The total DOS is obtained by summing the local DOS over all orbitals in the cluster.

## 3. EFFECT OF SURFACE TERMINATION

To investigate the effect of the cluster surface on the electronic properties of the cluster, we calculated the DOS for four clusters with different surface types. The calculations were performed for a small, $18\ \mathring{A}$ diameter cluster which has a large percentage of surface atoms. For the first calculation the surface orbitals were saturated by hydrogen atoms. Then the hydrogen saturated surface was allowed to relax to its lowest energy configuration. Next the hydrogens were removed leaving unsaturated Si dangling orbitals. Finally, the dangling orbitals were removed giving a truncated cluster.

### Hydrogen covered surfaces

The calculated densities of states for clusters covered with single layers of hydrogen atoms are shown in Figure 1. There are distinct valence and conduction bands separated by a band gap. The dotted line shows the DOS for an unrelaxed cluster with a Si-H distance of 1.5 $\mathring{A}$ and the DOS for a cluster with a relaxed surface is shown by the solid line. The relaxed atomic positions were taken from Ref. [8]. The deviation of the relaxed atoms from their bulk positions is not large in H-saturated Si surfaces and the change in DOS in the clusters is correspondingly small. In particular the band edge states, which are largely interior states, are unaffected by the inclusion of surface relaxation in the calculation.

![](./images/811670002292752384_1.jpg)

Figure 1: Densities of states for hydrogen saturated 18 Å diameter Si clusters with and without surface relaxation.

Surfaces without H atoms

The dotted line in Figure 2 shows the calculated DOS on a cluster with unsaturated dangling orbitals on the surface atoms. The bottom of the conduction band is obscured by an intense state, which is caused by the unsaturated dangling orbitals on the cluster surface. The solid line shows the local DOS on the surface atoms only (on the same scale) and illustrates that the surface atoms contribute to the band edge state.

![](./images/811670002292752384_2.jpg)

Figure 2: Density of states for an 18 Å diameter Si cluster with unsaturated dangling orbitals.

![](./images/811670002292752384_3.jpg)

Figure 3: Density of states for an 18 Å diameter Si cluster with the dangling orbitals removed

Figure 3 shows the calculated DOS for an 18 Å diameter cluster with the dangling orbitals removed. The intense surface state is not present and the band edges are now clearly visible. The DOS is qualitatively similar to those for the clusters with hydrogen saturated surfaces (Figure 1) especially around the band edges.

## 4. EFFECT OF CLUSTER SIZE

![](./images/811670002292752384_4.jpg)

Figure 4: Calculated densities of states for a range of cluster sizes.

The DOS for hydrogen-covered clusters was calculated over a range of cluster sizes. The results for three cluster sizes are plotted in Figure 4. As the cluster size is increased, the valence band shifts to higher energy and the conduction band to lower energy. The fundamental cluster band gap was measured from the difference between the highest energy peak in the valence band and the lowest energy peak in the conduction band. The results are presented in Figure 5. The band gap approaches the bulk value of 1.17eV as the cluster size is increased.

![](./images/811670002292752384_5.jpg)

Figure 5: Calculated band gaps for Si nanocrystals.

The shifts in the conduction band ($\Delta E_{CB}$) and the valence band ($\Delta E_{VB}$) with size can be compared with experimental photoluminescence data. In Figure 6, the calculated position of the visible photoluminescence band (given by $E_{gap} + \Delta E_{VB} + \Delta E_{CB} + E_{coulomb}$) is plotted against the calculated IR photoluminescence energy ($E_{danglingbond} + \Delta E_{CB}$) and compared with the experimental photoluminescence data of Petrova-Koch and Muschik[9]. Agreement with experiment is very good.

## 6. FUTURE WORK

We are currently studying the nature of the band edge wavefunctions as a function of the cluster size. Three-dimensional Fourier transformation of the band edge wavefunctions gives the distribution of k-values contributing to the band edge states. The results will indicate whether the lowest energy electronic transition can be described as direct or indirect gap and will help explain the mechanism of absorption in Si nanocrystals.

We are also working on direct two-particle calculations of electron-hole properties, and addition of the electron-phonon interaction to our model.

This material is based upon work supported by the NSF under award number CHE-9308704. N.Hill thanks Cray Research for award of their Fellowship in Computational Chemistry. The calculations were performed on the Cray C-90 at the San Diego Supercomputer Center.

![](./images/811670002292752384_6.jpg)

Figure 6: Comparison between experimental and theoretical Si photoluminescence data.

## REFERENCES

[1] N.A.Hill and K.B.Whaley, J.Chem.Phys. 99, 3707 (1993)
N.A.Hill and K.B.Whaley, J.Chem.Phys. 100, 2831 (1994)

[2] L.T.Canham, Appl.Phys.Lett. 61, 1948 (1992)
Light emission from silicon, edited by S.S.Iyer, R.T.Collins and L.T.Canham, (Mater.
Res. Soc. Proc. 256, Pittsburgh, PA, 1992)

[3] S.Y.Ren and J.D.Dow, Phys.Rev.B 45, 6492 (1992)
J.P.Proot, C.Delerue and G.Allen, Appl.Phys.Lett. 61, 1948 (1992)
B.Delley and E.F.Steigmeier, Phys.Rev.B 47, 1397 (1993)
L.W.Wang and A.Zunger, J.Phys.Chem. 98, 2158 (1994)
L.W.Wang and A.Zunger, J.Phys.Chem. 100, 2394 (1994)

[4] H.Takagi et al., Appl.Phys.Lett. 56, 2379 (1990)
A.Halimaoui et al., Appl.Phys.Lett. 59, 304 (1991)
M.A.Tischler et al., Appl.Phys.Lett. 60, 639 (1992)
K.A.Littau et al., J.Phys.Chem. 97, 1224 (1993)

[5] P.E.Batson and J.R.Heath, Phys.Rev.Lett. 71, 911 (1993)

[6] P.Vogl, H.P.Hjalmarson and J.D.Dow, J.Phys.Chem.Solids 44, 365 (1983)

[7] Gaussian Inc., 4415 Fifth Avenue, Pittsburgh, PA 15213

[8] Z.Jing and J.L.Whitten, Phys.Rev.B 46, 9544 (1992)
E.Kaxiras and J.D.Joannopoulos, Phys.Rev.B 37, 8842 (1988)

[9] V.Petrova-Koch and T.Muschik, to appear in Thin Solid Films