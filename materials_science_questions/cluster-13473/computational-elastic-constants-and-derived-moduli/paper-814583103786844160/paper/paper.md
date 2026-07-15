# Computation of graphene elastic moduli at low temperature
I. Yu. Zubko, and V. I. Kochurov

Citation: *AIP Conference Proceedings* **1683**, 020240 (2015);
View online: https://doi.org/10.1063/1.4932930
View Table of Contents: http://aip.scitation.org/toc/apc/1683/1
Published by the American Institute of Physics

---

## Articles you may be interested in
Estimation of elastic moduli of graphene monolayer in lattice statics approach at nonzero temperature
*AIP Conference Proceedings* **1683**, 020241 (2015); 10.1063/1.4932931

# Computation of Graphene Elastic Moduli at Low Temperature

I. Yu. Zubko$^{1, \text{a)}}$ and V. I. Kochurov$^{1}$

$^{1}$ Perm National Research Polytechnic University, Perm, 614990 Russia

$^{\text{a)}}$Corresponding author: zoubko@list.ru

**Abstract.** Finding the values of parameters for the simplest Mie's family potentials is performed in order to estimate elastic moduli of graphene monolayers using lattice statics approach. The coincidence criterion of the experimentally determined Poisson's ratio with the estimated value is taken in order to select dimensionless power parameters of the Mie-type potential. It allowed obtaining more precise estimation of elastic properties in comparison with variety of other potentials for carbon atoms in graphene monolayer.

Carbone nanoparticles having a relatively small number of atoms are quite convenient for studying within the discrete atomistic approaches which enable the determination of their mechanical properties. But the parameters of the used interatomic interaction potentials require experimental identification. The known experiments with graphene and thin graphite films show a considerable discrepancy of results. A lot of data are not found *in-situ* but obtained from additional computations using one or another model of elastic shells and rods. Thus, a great experimental data scattering is caused not only with different techniques but also with an approximate type of the chosen model.

For theoretical estimation of elastic properties using discrete approaches applied in the modelling of graphene monolayer and other carbon structures response on external actions, it is necessary to consider the fact that carbon atoms in such materials are in the $\text{sp}^{2}$-hybridization state; and covalent bindings set certain interaction directions. As a rule, complicated potentials are used to describe them. Despite quite a number of parameters of the known models, it is still not possible to obtain a set of graphene mechanical properties, which could provide an equally acceptable correspondence with the experimental values for all the properties. Using different potentials leads to different estimations of the elastic moduli. And even if it is possible to provide the correspondence with the experimental value for one elastic modulus, the second one shows a considerable deviation.

The paper suggests an easier method of graphene elastic moduli computation using the simplest empiric power-type potentials in nonsymmetric formulation, including identification of potential parameters. The arbitrariness in choosing the graphene layer thickness enables to obtain any value of three dimensional Young's modulus. However the dimensionless Poisson's ratio does not depend on the layer thickness, and there is a greatest scatter of its computed values among all moduli and a considerable deviation from the experiment. It is possible to face the estimated value exceeding $v=1$ [1] which is inconsistent with positive-definiteness of the elasticity tensor. The computations performed by different authors have an important peculiarity: the violation of the isotropy of the elastic response for graphene. Almost all the papers use a rectangular sample which results in the arising orthotropy of the in-plane monolayer elastic response [2–5] and does not correspond with the well known results of the elasticity for two-dimensional materials. In particular, the authors of [3] obtained quite different sets of the elastic moduli, including the sign change of the Poisson's ratio depending on the type of deformation (directions of axes for tension and simple shear). The dependence of the elastic moduli on the sample shape and size has been proved with experiments and emphasized in [2].

The statics approach is used to find graphene elastic properties. Small distortions of graphene monolayer are considered, whereas the lattice stability or changes of the covalent binding direction under lattice deformation are not studied. It is accepted that the power-type pair potential can be used to describe the atoms interaction.

---
*Advanced Materials with Hierarchical Structure for New Technologies and Reliable Structures*
AIP Conf. Proc. 1683, 020240-1–020240-5; doi: 10.1063/1.4932930
© 2015 AIP Publishing LLC 978-0-7354-1330-6/$30.00

020240-1

Fundamentally the situation is always the same: if two atoms take part in the force interaction, then they repulse each other when coming closer, and they are attracted when moving apart. The applied method accepts that the system of the covalent binding already exists and a certain crystal structure is formed, so, based on it we can determine its elastic properties. It is considered that the interaction potential part responsible for the atoms repulsion is active between all the sample atoms; and the attraction is considered only for the close atoms located in the direction of the covalent binding action according to the $\mathrm{sp}^{2}$-hybridized electron shell.

# DETERMINATION OF INITIAL CONFIGURATION FOR GRAPHENE MONOLAYER

In order to eliminate the mutual superposition of the sample and lattice symmetry classes, the computational experiments are performed with plane hexagonal sample possessing the triad axis symmetry. If we determine the elastic moduli, the affine deformations are applied on the body in the stress-free natural state. We suppose that in any state we can neglect difference in atom spacing along the specimen and consider the homogeneous structure. So we impose that the reference configuration is characterised only by the interatomic distance $a$, which is considered to be a variable and found as a minimiser for the full potential energy $\Phi(a)$ of the sample:

$$
\Phi(a) \rightarrow \min _{a}, \quad \Phi=\sum_{i=1}^{M-1}\left(\sum_{j=i+1}^{M} \varphi^{+}\left(\mathbf{R}_{j}-\mathbf{R}_{i}\right)+\sum_{j>i, j \in S_{i}} \varphi^{-}\left(\mathbf{R}_{j}-\mathbf{R}_{i}\right)\right), \quad \mathbf{R}_{i}, \mathbf{R}_{j} \in A, \tag{1}
$$

where $M$ is the number of all atoms for graphene sample, $A$ is a two dimensional area containing its atoms, $\varphi^{+}(\mathbf{R}_{j}-\mathbf{R}_{i})$ is a part of the pair interaction potential responsible for the repulsion of atoms; $\varphi^{-}(\mathbf{R}_{j}-\mathbf{R}_{i})$ describes the attraction; $S_{i}$ is a set of atom indices forming a close neighbourhood of $i$-atom and connected to it with the covalent bindings. For these parts we choose the Mie potential

$$
\varphi^{+}(r)=\beta n(\alpha / r)^{m} /(m-n), \quad \varphi^{-}(r)=-\beta m(\alpha / r)^{n} /(m-n), \tag{2}
$$

where $\alpha$ is an equilibrium distance for an isolated pair of atoms, $\beta$ is the energy which corresponds to the potential well depth at the interaction of these atoms. The examples of dependences for the dimensionless complex $a/\alpha$ on the number of $N$ atoms at the sample side for two sets of $m$ and $n$ parameters values are obtained for ideal graphene lattice (corresponding to the crystal at low temperature) according to the following expression, where real numbers $b_{(ij)} = \left|\mathbf{b}_{(ij)}\right|$ are dimensionless initial atoms distances, vectors $\mathbf{b}_{(ij)} \equiv \mathbf{R}_{(ij)}/a$, $\mathbf{R}_{(ij)} = \mathbf{R}_{j} - \mathbf{R}_{i}$

$$
a/\alpha = \left[ \sum_{i=1}^{M-1} \sum_{j=i+1}^{M} b_{(ij)}^{-m} \bigg/ \sum_{i=1}^{M-1} \sum_{\substack{j>i, \\ j \in S_{i}}} b_{(ij)}^{-n} \right]^{1/(m-n)},
$$

![](./images/814583103786844160_1.jpg)

FIGURE 1. The dependences of the complex $a/\alpha$ (a) and inner displacement $\delta$ (b) on the number of atoms $N$ at the sample side for two sets of $m$ and $n$, the dashed lines are horizontal asymptotes

020240-2

![](./images/814583103786844160_2.jpg)

FIGURE 2. The dependencies of the dimensionless elastic moduli on atoms number $N$ at the sample side for two sets
of parameters: $m=6, n=5$ (a), $m=5, n=3$ (b)

and shown in Fig. 1a. These sequences converge fast enough. The family of functions $y=c(x-x_0)^k+b$ is used to obtain an approximate relationship for them.

The parameters $c, k, b, x_0$ are determined with the least square method. Meanwhile it turned out that $k$ parameter corresponds with the $k=-1$ value for all the studied values of $m$ and $n$. So, $b$ parameter characterizes the horizontal asymptote place and it is connected to the interatomic distance at the macroscale as $a^\infty/\alpha=b$. The limit distance $a^\infty$ is expressed for two sets of $m$ and $n$:

$$1)\, m=6, n=5: \, a^\infty=1.909\alpha, \, 2)\, m=5, n=3: \, a^\infty=1.897\alpha. \tag{3}$$

The value of $a$ found for graphene in the experiments is $a^\text{exp}=1.42\times10^{-10}$ [m]. This distance is expressed with the obtained one as $a^\text{exp}=a^\infty/\sqrt{3}$, so $\alpha$ for the set values of $m, n$ is expressed as

$$1)\, m=6, n=6: \, \alpha=1.29\times10^{-10} \, [\text{m}], \, 2)\, m=5, n=3: \, \alpha=1.30\times10^{-10} \, [\text{m}]. \tag{4}$$

The obtained correlation between the lattice parameter and sample size (which is more important at the nanoscale) shows that the mechanical properties of nanoparticles are different from the properties of macroscopic body. It means that, from the mechanical point of view, they consist of different materials, although their structures and chemical composition are the same. The value of inner displacements parameter $\delta$ also depends on the exponents $m, n$ and the number $N$ (Fig. 1b). The limit values are found in the same way and they are equal to:

$$1)\, m=6, n=5: \, \delta^\infty=0.064, \, 2)\, m=5, n=3: \, \delta^\infty=0.091. \tag{5}$$

# ELASTIC MODULI COMPUTATION

The elastic moduli dependencies on specimen size in Fig. 2 are found using the following formulae

$$
C_{kkll} = \left. \frac{1}{V_0} \frac{\partial^2 \varphi(\lambda_1, \lambda_2)}{\partial \lambda_k \partial \lambda_l} \right|_{\substack{\lambda_k \to 1 \\ \lambda_l \to 1}} , \,\,
C_{klkl} = \left. \frac{1}{V_0} \frac{\partial^2 \varphi(\gamma_{kl})}{\partial (\gamma_{kl})^2} \right|_{\gamma_{kl} \to 0} , \,\,
C_{kllk} = \left. \frac{1}{V_0} \frac{\partial^2 \varphi(\gamma_{kl}, \gamma_{lk})}{\partial (\gamma_{kl}) \partial (\gamma_{lk})} \right|_{\substack{\gamma_{kl} \to 0 \\ \gamma_{lk} \to 0}} , \tag{6}
$$

where $\varphi(\mathbf{F})$ is potential energy of the graphene sample in actual configuration, $\mathbf{F}$ is affinor connecting the reference and actual configurations, $V_0$ is "volume" (square) of the specimen in reference configuration. The right hand part derivatives in (6) may be obtained using the simplest power-type Mie's family potential as the following expressions

$$
\left. \frac{\partial^2 (\varphi/\beta)}{\partial (\lambda_k)^2} \right|_{\lambda_k \to 1} = \frac{mn}{m-n} \bigg[ (a/\alpha)^{-m} \sum_{i=1}^{M-1} \sum_{j=i+1}^M A_{ij}(m,k,k) - (a/\alpha)^{-n} \sum_{i=1}^{M-1} \sum_{j>i, j \in S_i} A_{ij}(n,k,k) \bigg],
$$

020240-3

<table>
<thead>
<tr>
<th colspan="4">TABLE 1</th>
</tr>
<tr>
<th>$E^{2D}$, Paxm</th>
<th>v</th>
<th>$a$, nm</th>
<th>The method of obtaining</th>
</tr>
</thead>
<tbody>
<tr>
<td>345</td>
<td>0.236</td>
<td>0.142</td>
<td>Using the Mie potential parameters values: $m=6$, $n=5$,
$\alpha=1.29×10^{-10}$ [m], $\beta=1.16×10^{-18}$ [J]</td>
</tr>
<tr>
<td>345</td>
<td>$0.17±0.01$</td>
<td>–</td>
<td>The experiment of O.L. Blakslee, 1970 [5]</td>
</tr>
<tr>
<td>365</td>
<td>0.102</td>
<td>0.142</td>
<td>Using the Mie potential parameters values: $m=5$, $n=3$,
$\alpha=1.30×10^{-10}$ [m], [J]</td>
</tr>
<tr>
<td>365</td>
<td>0.125</td>
<td>0.142</td>
<td>The experiment of A. Bosak, 2007 [6]</td>
</tr>
</tbody>
</table>

$$
\left.\frac{\partial^{2}(\varphi / \beta)}{\partial\left(\lambda_{k}\right) \partial\left(\lambda_{l}\right)}\right|_{\substack{\lambda_{k} \rightarrow 1 \\ \lambda_{l} \rightarrow 1}}=\left.\frac{\partial^{2}(\varphi / \beta)}{\partial\left(\gamma_{k l}\right) \partial\left(\gamma_{l k}\right)}\right|_{\substack{\gamma_{k l} \rightarrow 0 \\ \gamma_{l k} \rightarrow 0}}=\frac{m n}{m-n}\left[(a / \alpha)^{-m} \sum_{i=1}^{M-1} \sum_{j=i+1}^{M} B_{i j}(m, k, l)-(a / \alpha)^{-n} \sum_{i=1}^{M-1} \sum_{j>i, j \in S_{i}} B_{i j}(n, k, l)\right],
$$

$$
\left.\frac{\partial^{2}(\varphi / \beta)}{\partial\left(\gamma_{k l}\right)^{2}}\right|_{\gamma_{k l} \rightarrow 0}=\frac{m n}{m-n}\left[(a / \alpha)^{-m} \sum_{i=1}^{M-1} \sum_{j=i+1}^{M} A_{i j}(m, k, l)-(a / \alpha)^{-n} \sum_{i=1}^{M-1} \sum_{j>i, j \in S_{i}} A_{i j}(n, k, l)\right],
$$

where $a$ is the equilibrium atom spacing discussed above; the functions $A_{i j}(m, k, l)$, $B_{i j}(m, k, l)$ on power exponents $m$, $n$ and moduli indices $k$, $l$ are defined as
$$
A_{i j}(m, k, l)=((2+m)\left(\mathbf{b}_{(i j)}\right)_{k}^{2}-b_{(i j)}^{2})\left(\mathbf{b}_{(i j)}\right)_{l}^{2} b_{(i j)}^{-m-4}, \quad B_{i j}(m, k, l)=(2+m)\left(\mathbf{b}_{(i j)}\right)_{k}^{2}\left(\mathbf{b}_{(i j)}\right)_{l}^{2} b_{(i j)}^{-m-4}.
$$

The Poisson’s ratio values $v$ for the samples of different sizes with $m$ and $n$ values from the sets $n=\overline{3,8}$, $m=\overline{n+1,14}$ which are calculated using the inner displacements corrections lie within the interval $v \in(0.1 ; 0.99)$.
The best approximation of the experimental value $v=0.17±0.01$ that is determined for graphite in [5] is obtained under the following power parameters:
$$
1) \, m=6, n=5: v^{\infty}=0.236, \, 2) \, m=5, n=3: v^{\infty}=0.102.
$$

Under any values of $m$ and $n$ for the samples of different sizes between the three elastic moduli which are calculated independently, the strict components correlation $C_{1212}=(C_{1111}-C_{1122})/2$ is found to be true for the ideal graphene lattice. Thus the tensor of the elastic moduli $C$ for graphene is symmetric at low temperature. All elastic moduli depend on the sample size, as shown in Fig. 2. The Young’s modulus computation using the obtained tensor $C$ components for the chosen values of $m$ and $n$ parameters provides its limit (macroscopic) values through Mie potential parameters:
$$
1) \, m=6, n=5: E^{\infty}=4.915 \beta / \alpha^{2}, \, 2) \, m=5, n=3: E^{\infty}=2.305 \beta / \alpha^{2}.
$$

As $\alpha$ parameter is already determined for different values of $m$ and $n$, then we can identify $\beta$ based on the experimental value of the Young’s modulus. The “two-dimensional Young's modulus” of graphene is equal to $E^{2D} \approx 340±50$ [N m$^{-1}$] as obtained in [5–7], so the $\beta$ parameter is found as:
$$
1) \, m=6, n=5: \beta=1.16×10^{-18} \text{ [J], } 2) \, m=5, n=3: \beta=2.66×10^{-18} \text{ [J]}.
$$

## CONCLUSION

The obtained two sets of the Mie potential parameters provide the Young’s modulus values and interatomic distance values for graphene monolayer, which fully comply with the experimental values in Table 1. Only the Poisson’s ratio remains different (although more precise in comparison with computations of the other authors) which is obtained in the specified experiments not for graphene sheet but for graphite thin sample; and it still needs to be precised. Applying the Mie’s family potential with the obtained parameters allows a further study of other mechanical properties of graphene, graphite or carbon structures in the frame of lattice statics approach.

020240-4

# ACKNOWLEDGMENTS

The work was supported by state assignment of the Russian Federation No. 2014/152 (project code is 1911).

# REFERENCES

1.  A. Sakhaee-Pour, *Solid State Commun.* **149**, 91–95 (2009).
2.  C. D. Reddy, S. Rajendran, and K. M. Liew, *Nanotechnology* **17**, 864–870 (2006).
3.  F. Scarpa, S. Adhikari, and P. A. Srikantha, *Nanotechnology* **20**, 065709 (11 p.) (2009).
4.  M. M. Shokrieh and R. Rafiee, *Mater. Design* **31**, 790–795 (2010).
5.  O. L. Blakslee, D. G. Proctor, and E. J. Seldin, *J. Appl. Phys.* **8**, 3373–3389 (1970).
6.  A. Bosak, M. Krisch, M. Mohr, J. Maultzsch, and C. Thompsen, *Phys. Rev. B* **75**, 153408 (4 p.) (2007).
7.  C. Lee, X. Wei, J.W. Kysar, and J. Hone, *Science* **321**, 385–388 (2008).

020240-5