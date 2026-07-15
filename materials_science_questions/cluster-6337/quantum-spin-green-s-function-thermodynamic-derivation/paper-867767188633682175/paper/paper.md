
# Time evolution and decoherence of a spin- \( \frac{1}{2} \)  particle coupled to a spin bath in thermal equilibrium

Y. Hamdouni \( ^{*} \)  and F. Petruccione

School of Physics, University of KwaZulu-Natal, Westville Campus, Durban 4001, South Africa

The time evolution of a spin- \( \frac{1}{2} \)  particle under the influence of a locally applied external magnetic field, and interacting with anisotropic spin environment in thermal equilibrium at temperature T is studied. The exact analytical form of the reduced density matrix of the central spin is calculated explicitly for finite number of bath spins. The case of an infinite number of environmental spins is investigated using the convergence of the rescaled bath operators to normal Gaussian random variables. In this limit, we derive the analytical form of the components of the Bloch vector for antiferromagnetic interactions within the bath, and we investigate the short-time and long-time behavior of reduced dynamics. The effect of the external magnetic field, the anisotropy and the temperature of the bath on the decoherence of the central spin is discussed.

PACS numbers: 03.65.Yz, 03.67.Lx, 73.21.La, 75.10.Jm

## I. INTRODUCTION

The loss of quantum coherence due to unavoidable interactions of quantum systems with the surrounding environment is known as decoherence. It represents the main obstacle to quantum computing and quantum information processing \( ^{1,2,3} \) . The environment destroys quantum interferences of the central system within time scales much shorter than those typically characterizing dissipation \( ^{4} \) . The unwanted effect of decoherence reduces the advantages of quantum computing methods by producing errors in their outcomes. Different strategies, such as error-correcting codes, are adopted to overcome this difficulty \( ^{5,6,7,8} \) . Great scientific effort has been devoted to the understanding of the process of decoherence in quantum systems, mainly focused on solid state spin nanostructures. These systems seem to be the most promising candidates that can be efficiently used in quantum information processing and computation \( ^{9,10,11} \) .

Several models were proposed to study decoherence of single and multi-spin systems interacting with a surrounding environment \( ^{12} \) . Very often, the derivation of the reduced dynamics involves complications and difficulties that can be overcome in many cases by making recourse to approximation techniques. In particular, the Markovian approximation together with the master equation approach turns out to be very useful \( ^{13,14} \) . However, any approximation method is inevitably based on some assumptions which do not necessarily reflect the actual properties of the composite system. Moreover, many realistic spin systems exhibit non-Markovian behavior for which the standard derivation of the master equation ceases to be applicable. The non-Markovian dynamics of a central spin-system coupled to a spin environment has been investigated by many authors \( ^{15,16,17,18,19} \) .

In general, the course of the decoherence process depends on the intrinsic properties of the bath such as temperature, polarizations, and quantum fluctuations. At low environmental temperatures, the dominant effect arises from the contributions of localized modes such as nuclear spins \( ^{20} \) . In quantum dots, the decoherence of the central spins is mainly caused by the hyperfine coupling with the surrounding nuclear spins. The effect of bath polarizations and external magnetic fields on the decoherence of electron spins in quantum dots has been investigated by Zhang et al \( ^{21} \) .

In the following paper we study the dynamics of a spin- \( \frac{1}{2} \)  particle interacting with a large spin environment in thermal equilibrium. In Sec. II we introduce the model Hamiltonian together with the initial states of the central spin and the environment. In Sec. III, we calculate the exact time evolution operator of the composite system and we derive the reduced density matrix of the central spin. Sec. IV is devoted to the case of an infinite number of spins in the bath. We study the long-time behavior as well as the short-time behavior of the reduced density matrix, and we discuss the effect of the magnetic field and the bath temperature on decoherence. A short conclusion ends the paper.

## II. THE MODEL

We consider a central spin- \( \frac{1}{2} \)  particle coupled to a spin bath composed of N interacting spin- \( \frac{1}{2} \)  particles in thermal equilibrium at temperature T. The spin operators corresponding to the central system are denoted by  \( S_{i}^{0} \)  with i = x, y, z, those associated with the bath constituents are denoted by  \( S_{i}^{k} \) , where  \( k = 1, 2, ..., N \)  and i = x, y, z. We assume that the central system as well as every spin in the bath couples to all other spins through long-range anisotropic Heisenberg interactions. Moreover, an external magnetic field of controlled strength  \( \mu \)  is locally applied to the central spin along the z direction. Under the above assumptions, the model Hamiltonian
 

can be written as

 \[ H=H_{S}+H_{S B}+H_{B} \quad (1) \] 

where  \( H_{S} \)  and  \( H_{B} \)  are, respectively, the Hamiltonian operators of the central spin and the surrounding environment. The coupling between the open system and the bath is described by the Hamiltonian  \( H_{SB} \) . Explicitly, we have

 \[ H_{S}=2\mu S_{z}^{0}, \quad (2) \] 

 \[ H_{S B}=\frac{2\gamma}{\sqrt{N}}S_{z}^{0}\sum_{i=1}^{N}S_{z}^{i}+\frac{2\alpha}{\sqrt{N}}\Big[S_{x}^{0}\sum_{i=1}^{N}S_{x}^{i}+S_{y}^{0}\sum_{i=1}^{N}S_{y}^{i}\Big], \quad (3) \] 

 \[ H_{B}=\frac{g}{N}\Biggl[\sum_{i\neq j}^{N}\Bigl(S_{x}^{i}S_{x}^{j}+S_{y}^{i}S_{y}^{j}\Bigr)+\Delta\sum_{i\neq j}^{N}S_{z}^{i}S_{z}^{j}\Biggr], \quad (4) \] 

where  \( \gamma \)  and  \( \alpha \)  are the coupling constants of the central spin to the environment, g stands for the strength of interactions of spins in the bath, and  \( \Delta \)  is the anisotropy constant. The coefficient 2 in front of  \( \mu \) ,  \( \gamma \)  and  \( \alpha \)  in Eqs. (2) and (3) is introduced for later convenience. Furthermore, we have rescaled the above interaction strengths with appropriate powers of the number of spins in the environment in order to ensure good thermodynamical behavior, namely an extensive free energy. Obviously, a more realistic model would include site-dependent interactions.

Note that in the case where  \( \gamma = 0 \) ,  \( H_{SB} \)  reduces to Heisenberg XY Hamiltonian which was recently used to model the coupling of one and two qubits to star-like environments \( ^{15,16,17,22} \) . Moreover, when  \( \gamma = \alpha \)  we simply have  \( H_{SB} = \frac{\alpha}{\sqrt{N}} \vec{S}^{0} \sum_{i=1}^{N} \vec{S}^{i} \) , which should be compared with the Hamiltonian of the hyperfine contact coupling of electron spin to the nuclear spins in quantum dot. In Ref. 23, the Hamiltonian  \( h_{B} = \sum_{i > j} g_{ij} (\vec{S}^{i} \vec{S}^{j} - 3 S_{z}^{i} S_{z}^{j}) \)  was used to model the intra-bath dipolar coupling between nuclear spins in quantum dot. If we assume uniform coupling between nuclear spins, i.e. all the  \( g_{ij} \)  are the same, then the operator  \( h_{B} \)  (with rescaled coupling constant) becomes equivalent to  \( H_{B} \)  in the case where  \( \Delta = -2 \) . It should also be noted that the bath Hamiltonian  \( H_{B} \)  is very close to that of the isotropic Lipkin-Meshkov-Glick model \( ^{24,25} \) . There, the magnetic field globally applied to all spins plays the role of the anisotropy present in our model. This can be better seen by applying mean field approximation to the longitudinal term of  \( H_{B} \) .

The Hamiltonian operators  \( H_{B} \)  and  \( H_{SB} \)  can be rewritten in terms of the lowering and raising operators  \( S_{\pm}^{i} = S_{x}^{i} \pm i S_{y}^{i} \)  as follows

 \[ H_{S B}=\frac{2\gamma}{\sqrt{N}}S_{z}^{0}\sum_{i=1}^{N}S_{z}^{i}+\frac{\alpha}{\sqrt{N}}\Big[S_{+}^{0}\sum_{i=1}^{N}S_{-}^{i}+S_{-}^{0}\sum_{i=1}^{N}S_{+}^{i}\Big], \quad (5) \] 

 \[ H_{B}=\frac{g}{2N}\Biggl[\sum_{i\neq j}^{N}\Bigl(S_{+}^{i}S_{-}^{j}+S_{-}^{i}S_{+}^{j}\Bigr)+2\Delta\sum_{i\neq j}^{N}S_{z}^{i}S_{z}^{j}\Biggr]. \quad (6) \] 

By introducing the total angular momentum of the bath  \( \vec{J} = \sum_{i=1}^{N} \vec{S}^{i} \) , together with the corresponding lowering and raising operators  \( J_{\pm} \) , it is possible to put the above Hamiltonian operators into the following form

 \[ H_{S B}=\frac{2\gamma}{\sqrt{N}}S_{z}^{0}J_{z}+\frac{\alpha}{\sqrt{N}}\Big[S_{+}^{0}J_{-}+S_{-}^{0}J_{+}\Big], \quad (7) \] 

 \[ H_{B}=\frac{g}{2N}\Big[N+K+2\Delta J_{z}^{2}-\frac{(2+\Delta)N}{2}\Big]. \quad (8) \] 

Here,  \( J_{z} \)  is the z-component of the total angular momentum J, and we have introduced the operator  \( K = J_{+}J_{-} + J_{-}J_{+} \) . From here on, we shall neglect the constant  \( (2 + \Delta)g/4 \)  appearing in the expression of  \( H_{B} \)  since it has no effect on the dynamics of the system. This can be done by redefining the energy origin of the spectrum of the bath Hamiltonian.

The spin spaces corresponding to the central spin and the environment are given by  \( \mathbb{C}^{2} \)  and  \( (\mathbb{C}^{2})^{\otimes N} \) , respectively. The latter space can be decomposed as a direct sum of subspaces  \( C^{d_{j}} \)  each of which has a dimension equal to  \( d_{j}=2j+1 \)  where  \( 0\leq j\leq\frac{N}{2} \)  \( ^{16} \)  (we take N even), namely  \( (\mathbb{C}^{2})^{\otimes N}=\bigoplus_{j=0}^{\frac{N}{2}}\nu(N,j)\mathbb{C}^{d_{j}} \) . The degeneracy  \( \nu(N,j) \)  is given by \( ^{26} \) 

 \[ \nu(N,j)=\frac{2j+1}{\frac{N}{2}+j+1}\frac{N!}{(\frac{N}{2}-j)!({\frac{N}{2}+j})!}. \quad (9) \] 

It is worth noting that the bath Hamiltonian can be expressed in terms of the operators  \( J^{2} \)  and  \( J_{z} \)  as  \( H_{B} = \frac{g}{N}[J^{2} + (\Delta - 1)J_{z}^{2}] \) . Therefore, the operator  \( H_{B} \)  is diagonal in the standard basis of  \( (\mathbb{C}^{2})^{\otimes N} \)  formed by the common eigenvectors of  \( J^{2} \)  and  \( J_{z} \)  which we denote by  \( |j, m\rangle \)  where  \( -j \leq m \leq j \) . In this basis, the eigenvalues of the operator K are simply given by  \( 2(j(j + 1) - m^{2}) \)  (we set  \( \hbar = 1 \) ).

## III. REDUCED DYNAMICS OF THE CENTRAL SPIN

In this section we derive the exact time evolution of the central spin for finite number of environmental spins. As usual, we introduce the time evolution operator  \( \mathbf{U}(t) = \mathrm{e}^{-iHt} \)  together with the total density matrix operator of the spin-bath system,  \( \rho_{\mathrm{tot}}(t) \) . The initial value of the
 

latter is denoted by  \( \rho_{\mathrm{tot}}(0) \) . The evolution in time of the composite system is unitary, its density matrix at any moment of time is given by

 \[ \rho_{\mathrm{t o t}}(t)=\mathbf{U}(t)\rho_{\mathrm{t o}t}(0)\mathbf{U}^{\dagger}(t). \quad (10) \] 

The reduced density matrix of the central spin can be calculated by tracing  \( \rho_{\mathrm{tot}}(t) \)  with respect to the environmental degrees of freedom, namely

 \[ \rho(t)=\mathrm{t r}_{B}\{\rho_{\mathrm{t o t}}(t)\}. \quad (11) \] 

This can be explicitly written in terms of bath states as

 \[ \rho(t)=\sum_{j,m}\nu(N,j)\langle j,m|\rho_{\mathrm{t o t}}(t)|j,m\rangle. \quad (12) \] 

In order to solve the time evolution problem (10), one needs to calculate the exact analytical form of  \( \mathbf{U}(t) \)  and to specify the initial density matrix.

## A. Initial conditions

Initially, the central spin is assumed to be uncorrelated with the environment. The corresponding total density matrix is given by the direct product  \( \rho_{\mathrm{tot}}(0)=\rho(0)\otimes\rho_{B} \)  where  \( \rho(0) \)  and  \( \rho_{B} \)  are, respectively, the initial density matrices of the central spin and the bath. In the standard basis composed of the eigenvectors  \( |-\rangle \)  and  \( |+\rangle \)  of the operator  \( S_{z}^{0} \) ,  \( \rho_{S}(0) \)  takes the general form

 \[ \rho(0)=\begin{pmatrix}\rho_{11}^{0}&\rho_{12}^{0}\\ \rho_{12}^{0*}&\rho_{22}^{0}\end{pmatrix}, \quad (13) \] 

where  \( \rho_{11} \)  and  \( \rho_{22} \)  are positive real numbers which satisfy  \( \rho_{11} + \rho_{22} = 1 \) . For instance, if at t = 0 the central system was in the state

 \[ |\psi(0)\rangle=a|-\rangle+b|+\rangle, \quad (14) \] 

where \(a\) and \(b\) are complex numbers satisfying \(|a|^{2}+|b|^{2}=1\), then \(\rho_{11}^{0}=|a|^{2}\) and \(\rho_{12}^{0}=ab^{*}\).

Alternatively,  \( \rho(0) \)  can be expressed in terms of the components of the Bloch vector  \( \vec{\lambda} = (\lambda_{1}, \lambda_{2}, \lambda_{3}) \)  as

 \[ \rho(0)=\frac{1}{2}\begin{pmatrix}{{{1-\lambda_{3}(0)}}}&{{{\lambda_{1}(0)-i\lambda_{2}(0)}}} \\{{{\lambda_{1}(0)+i\lambda_{2}(0)}}}&{{{1+\lambda_{3}(0)}}}\end{pmatrix}, \quad (15) \] 

with the condition  \( |\vec{\lambda}| \leq 1 \) ; the equality holds for pure initial states. We shall use both representations of the density matrix throughout the paper.

At t = 0, the spin bath is taken in thermal equilibrium at finite temperature T. Its density matrix is given by the Boltzmann distribution

 \[ \rho_{B}=\frac{\mathrm{e}^{-\beta H_{B}}}{Z_{N}}, \quad (16) \] 

where  \( \beta = 1/T \)  (we set  \( k_{B} = 1 \) ), and  \( Z_{N} = \operatorname{tr}_{B} e^{-\beta H_{B}} \)  is the partition function of the bath. Clearly,  \( \rho_{B} \)  is diagonal in the standard basis  \( \{|j, m\rangle\} \)  from which it follows that \( ^{27} \) 

 \[ \langle j,m|\rho_{B}|j,m\rangle=\frac{1}{Z_{N}}\mathrm{e}^{-\frac{\alpha\beta}{N}[j(j+1)+(\Delta-1)m^{2}]}, \quad (17) \] 

and

 \[ Z_{N}=\sum_{j,m}\nu(N,j)\mathrm{e}^{-\frac{\alpha\beta}{N}[j(j+1)+(\Delta-1)m^{2}]}. \quad (18) \] 

In the case of the isotropic Heisenberg model, i.e. when  \( \Delta = 1 \) , the above expression simplifies to

 \[ Z_{N}=\sum_{j}\nu(N,j)(2j+1)\mathrm{e}^{-\frac{\alpha\beta}{N}[j(j+1)]}. \quad (19) \] 

In the extreme case of an infinite temperature ( \( \beta \rightarrow 0 \) ), the density matrix of the bath reads

 \[ \rho_{B}(T=\infty)=\frac{\mathbf{1}_{B}}{2^{N}}, \quad (20) \] 

which corresponds to a completely unpolarized spin bath. In the previous expression  \( 1_{B} \)  stands for the unity matrix in the bath space.

## B. Time evolution operator

Let  \( U_{ij} \)  denote the components of the time evolution operator U in the basis  \( \{|-\rangle, |+\rangle\} \)  corresponding to the central system space. Therefore, we can write

 \[ \mathbf{U}|-\rangle=U_{11}|-\rangle+U_{21}|+\rangle, \quad (21) \] 

 \[ \mathbf{U}|+\rangle=U_{12}|-\rangle+U_{22}|+\rangle. \quad (22) \] 

On the other hand, the operator U satisfies the Schrödinger equation

 \[ i\frac{d}{d t}\mathbf{U}|\pm\rangle=H\mathbf{U}|\pm\rangle. \quad (23) \] 

Substituting Eq. (21) into Eq. (23) yields the following system of coupled differential equations

 \[ \begin{align*}i\dot{U}_{11}&=\left[-\left(\mu+\frac{\gamma J_{z}}{\sqrt{N}}\right)+\frac{g}{2N}\Big(K+2\Delta J_{z}^{2}\Big)\right]U_{11}+\frac{\alpha J_{+}}{\sqrt{N}}U_{21},\\i\dot{U}_{21}&=\frac{\alpha J_{-}}{\sqrt{N}}U_{11}+\left[\left(\mu+\frac{\gamma J_{z}}{\sqrt{N}}\right)+\frac{g}{2N}\Big(K+2\Delta J_{z}^{2}\Big)\right]U_{21}.\end{align*} \quad (24) \quad (25) \] 

Similarly, from Eq. (22) and Eq. (23) we obtain

 \[ i\dot{U}_{22}=\left[\left(\mu+\frac{\gamma J_{z}}{\sqrt{N}}\right)+\frac{g}{2N}\Big(K+2\Delta J_{z}^{2}\Big)\right]U_{22}+\frac{\alpha J_{-}}{\sqrt{N}}U_{12}, \quad (26) \] 

 \[ i\dot{U}_{12}=\frac{\alpha J_{+}}{\sqrt{N}}U_{22}+\left[-\left(\mu+\frac{\gamma J_{z}}{\sqrt{N}}\right)+\frac{g}{2N}\Big(K+2\Delta J_{z}^{2}\Big)\right]U_{12}. \quad (27) \]
 

Since  \( \mathbf{U}(0)=\mathbf{1}_{2}\otimes\mathbf{1}_{B} \) , one gets the initial conditions

 \[ U_{11}(0)=U_{22}(0)=\mathbf{1}_{B},\ U_{12}(0)=U_{21}(0)=0. \quad (28) \] 

The difficulty with solving the above set of differential equations resides in the fact that the coefficients of the operator variables  \( U_{21} \)  and  \( U_{12} \)  are not diagonal and do not commute with those of  \( U_{11} \)  and  \( U_{22} \) . Nevertheless, as we shall see below, this problem can be overcome by transforming these equations into new ones involving commuting diagonal operators. Indeed, by making use of the change of variables (see Ref. 19 for a similar method)

 \[ U_{11}=\mathrm{e}^{-i[-\left(\mu+\frac{\gamma J_{\pm}}{N}\right)+\frac{g}{2N}\left(K+2\Delta J_{z}^{2}\right)]t}\widetilde{U}_{11}, \quad (29) \] 

 \[ U_{21}=J_{-}\mathrm{e}^{-i[-\left(\mu+\frac{\gamma J_{\pm}}{N}\right)+\frac{g}{2N}\left(K+2\Delta J_{z}^{2}\right)]t}\widetilde{U}_{21}, \quad (30) \] 

 \[ U_{22}=\mathrm{e}^{-i\left[\left(\mu+\frac{\gamma J_{\pm}}{N}\right)+\frac{g}{2N}\left(K+2\Delta J_{z}^{2}\right)\right]t}\widetilde{U}_{22}, \quad (31) \] 

 \[ U_{12}=J_{+}\mathrm{e}^{-i\left[\left(\mu+\frac{\gamma J_{\pm}}{N}\right)+\frac{g}{2N}\left(K+2\Delta J_{z}^{2}\right)\right]t}\widetilde{U}_{12}, \quad (32) \] 

and taking into account the commutation relations

 \[ \left[J_{z},J_{\pm}\right]=\pm J_{\pm},\quad\left[J_{z}^{2},J_{\pm}\right]=\pm J_{\pm}(2J_{z}\pm1) \] 

and

 \[ \left[K,J_{\pm}\right]=\mp2J_{\pm}(2J_{z}\pm1), \quad (33) \] 

we obtain

 \[ \dot{\tilde{U}}_{11}=\frac{\alpha}{\sqrt{N}}J_{+}J_{-}\tilde{U}_{21}, \quad (34) \] 

 \[ \dot{\tilde{U}}_{21}=\frac{\alpha}{\sqrt{N}}\tilde{U}_{11}+2\Big[\mu+\Big(\frac{\gamma}{\sqrt{N}}+\frac{g}{N}(1-\Delta)\Big)\Big(J_{z}-\frac{1}{2}\Big)\Big]\tilde{U}_{21}, \quad (35) \] 

 \[ \dot{\tilde{U}}_{22}=\frac{\alpha}{\sqrt{N}}J_{-}J_{+}\tilde{U}_{12}, \quad (36) \] 

 \[ \dot{\tilde{U}}_{12}=\frac{\alpha}{\sqrt{N}}\tilde{U}_{22}-2\Big[\mu+\Big(\frac{\gamma}{\sqrt{N}}+\frac{g}{N}(1-\Delta)\Big)\Big(J_{z}+\frac{1}{2}\Big)\Big]\tilde{U}_{12}. \quad (37) \] 

Now, the coefficients in front of the new operator variables  \( \tilde{U}_{ij} \)  are diagonal in the common eigenbasis of  \( J^{2} \)  and  \( J_{z} \) , whence the standard method of solving systems of differential equations can be easily applied. Combining the above relations leads to the following second order homogeneous differential equations for the operators  \( \tilde{U}_{21} \)  and  \( \tilde{U} \) .

 \[ \begin{align*}\ddot{\tilde{U}}_{21}+2i\Big[\mu+\Big(\frac{\gamma}{\sqrt{N}}+\frac{g}{N}(1-\Delta)\Big)\Big(J_{z}-\frac{1}{2}\Big)\Big]\ddot{\tilde{U}}_{21}\\+\frac{\alpha^{2}}{N}J_{+}J_{-}\tilde{U}_{21}=0,\end{align*} \quad (38) \] 

 \[ \begin{align*}\ddot{\tilde{U}}_{12}-2i\Big[\mu+\Big(\frac{\gamma}{\sqrt{N}}+\frac{g}{N}(1-\Delta)\Big)\Big(J_{z}+\frac{1}{2}\Big)\Big]\dot{\tilde{U}}_{12}\\+\frac{\alpha^{2}}{N}J_{-}J_{+}\tilde{U}_{12}=0,\end{align*} \quad (39) \] 

which admit the following solutions

 \[ \begin{aligned}\tilde{U}_{21}&=2iC_{1}\mathrm{e}^{-iF_{1}t}\sin\Big(t\sqrt{M_{1}}\Big),\\\tilde{U}_{12}&=2iC_{2}\mathrm{e}^{-iF_{2}t}\sin\Big(t\sqrt{M_{2}}\Big).\end{aligned} \quad (40) \quad (41) \] 

Here,  \( C_{1} \)  and  \( C_{2} \)  are some diagonal operators to be determined and we have

 \[ F_{1}=\mu+\Big(\frac{\gamma}{\sqrt{N}}+\frac{g}{N}(1-\Delta)\Big)\Big(J_{z}-\frac{1}{2}\Big), \quad (42) \] 

 \[ M_{1}=F_{1}^{2}+\frac{\alpha^{2}}{N}J_{+}J_{-}, \quad (43) \] 

 \[ F_{2}=-\mu-\Big(\frac{\gamma}{\sqrt{N}}+\frac{g}{N}(1-\Delta)\Big)\Big(J_{z}+\frac{1}{2}\Big), \quad (44) \] 

 \[ M_{2}=F_{2}^{2}+\frac{\alpha^{2}}{N}J_{-}J_{+}. \quad (45) \] 

Integrating the right-hand side of Eq. (40) gives

 \[ \begin{align*}\tilde{U}_{11}=-2C_{1}\mathrm{e}^{-iF_{1}t}\frac{\sqrt{N M_{1}}}{\alpha}\\\times\Big[\cos\Big(t\sqrt{M_{1}}\Big)+\frac{i F_{1}}{\sqrt{M_{1}}}\sin\Big(t\sqrt{M_{1}}\Big)\Big]+C_{3}.\end{align*} \quad (46) \] 

The constant operators  \( C_{1} \)  and  \( C_{3} \)  can be determined using the initial conditions (28) and the unitarity condition for the time evolution operator, which yield  \( C_{1} = \)
 

 \( -\alpha/(2\sqrt{NM_{1}})\mathbf{1}_{B} \)  and  \( C_{3}=0 \) . Hence, we obtain

 \[ U_{11}(t)=\mathrm{e}^{-i G_{1}t}\Big[\cos\Big(t\sqrt{M_{1}}\Big)+\frac{i F_{1}}{\sqrt{M_{1}}}\sin\Big(t\sqrt{M_{1}}\Big)\Big], \quad (47) \] 

 \[ U_{21}(t)=-i J_{-}\frac{\alpha}{\sqrt{N M_{1}}}\mathrm{e}^{-i G_{1}t}\sin\Big(t\sqrt{M_{1}}\Big), \quad (48) \] 

where

 \[ G_{1}=-\frac{\gamma}{2\sqrt{N}}+\frac{g}{2N}\Big[\Big(K+2\Delta J_{z}^{2}\Big)+2(1-\Delta)\Big(J_{z}-\frac{1}{2}\Big)\Big]. \quad (49) \] 

Following the same method, we find that

 \[ U_{22}(t)=\mathrm{e}^{-i G_{2}t}\Big[\cos\Big(t\sqrt{M_{2}}\Big)+\frac{i F_{2}}{\sqrt{M_{2}}}\sin\Big(t\sqrt{M_{2}}\Big)\Big], \quad (50) \] 

 \[ U_{12}(t)=-i J_{+}\frac{\alpha}{\sqrt{N M_{2}}}\mathrm{e}^{-i G_{2}t}\sin\Big(t\sqrt{M_{2}}\Big), \quad (51) \] 

where

 \[ G_{2}=-\frac{\gamma}{2\sqrt{N}}+\frac{g}{2N}\Big[\Big(K+2\Delta J_{z}^{2}\Big)+2(\Delta-1)\Big(J_{z}+\frac{1}{2}\Big)\Big]. \quad (52) \] 

It is easy to see that the operators  \( G_{1} \)  and  \( G_{2} \)  are diagonal in the common basis of  \( J^{2} \)  and  \( J_{z} \) .

## C. Reduced density matrix

Having determined the exact analytical form of the time evolution operator, we are able to calculate the reduced density matrix of the central spin. Indeed, from Eqs. (10) and (11), and by making use of the trace properties of the lowering and raising operators  \( J_{\pm} \) , we find that

 \[ \rho_{11}(t)=\frac{1}{Z_{N}}\Big[\rho_{11}^{0}\mathrm{t r}_{B}\Big(\mathrm{e}^{-\beta H_{B}}U_{11}U_{11}^{*}\Big) \] 

 \[ +\rho_{22}^{0}\mathrm{t r}_{B}\Big(\mathrm{e}^{-\beta H_{B}}U_{21}^{*}U_{12}\Big)\Big], \quad (53) \] 

 \[ \rho_{12}(t)=\frac{1}{Z_{N}}\rho_{12}^{0}\mathrm{t r}_{B}\Big(\mathrm{e}^{-\beta H_{B}}U_{11}U_{22}^{*}\Big). \quad (54) \] 

Furthermore, with the help of the commutation relations (33), we can easily prove that  \( J_{-}F_{1} = -F_{2}J_{-} \) , and  \( J_{-}M_{1} = M_{2}J_{-} \) . Using the latter equalities, one can check that the time-dependent components of the Bloch vector are given by

 \[ \lambda_{3}(t)=-\frac{2}{Z_{N}}\mathrm{t r}_{B}\Big\{\frac{\alpha^{2}J_{+}J_{-}}{N M_{1}}\mathrm{e}^{-\frac{g\beta}{2N}\left[K+2\Delta J_{z}^{2}+(1-\Delta)(2J_{z}-1)\right]}\sin^{2}\Big(t\sqrt{M_{1}}\Big)\sinh\Big[\frac{g\beta}{2N}(1-\Delta)(2J_{z}-1)\Big]\Big\} \] 

 \[ +\lambda_{3}(0)\Big\{1-\frac{2}{Z_{N}}\mathrm{t r}_{B}\Big\{\frac{\alpha^{2}J_{+}J_{-}}{N M_{1}}\mathrm{e}^{-\frac{g\beta}{2N}\left[K+2\Delta J_{z}^{2}+(1-\Delta)(2J_{z}-1)\right]}\sin^{2}\Big(t\sqrt{M_{1}}\Big)\cosh\Big[\frac{g\beta}{2N}(1-\Delta)(2J_{z}-1)\Big]\Big\}\Big\}, \quad (55) \] 

 \[ \lambda_{1}(t)=\mathrm{t r}_{B}\Big\{\Big(\lambda_{1}(0)\cos(\Omega t)+\lambda_{2}(0)\sin(\Omega t)\Big)A-\Big(\lambda_{1}(0)\sin(\Omega t)-\lambda_{2}(0)\cos(\Omega t)\Big)B\Big\}, \quad (56) \] 

 \[ \lambda_{2}(t)=-\mathrm{t r}_{B}\Big\{\Big(\lambda_{1}(0)\sin(\Omega t)-\lambda_{2}(0)\cos(\Omega t)\Big)A+\Big(\lambda_{1}(0)\cos(\Omega t)+\lambda_{2}(0)\sin(\Omega t)\Big)B\Big\}, \quad (57) \] 

where

 \[ \Omega=\frac{2g}{N}(\Delta-1)J_{z}, \quad (58) \] 

 \[ A=\frac{1}{Z_{N}}\Big\{\mathrm{e}^{-\frac{g\beta}{2N}[K+2\Delta J_{z}^{2}]}\Big[\cos\Big(t\sqrt{M_{1}}\Big)\cos\Big(t\sqrt{M}_{2}\Big)+\frac{F_{1}F_{2}}{\sqrt{M_{1}M_{2}}}\sin\Big(t\sqrt{M_{1}}\Big)\sin\Big(t\sqrt{M}_{2}\Big)\Big]\Big\}, \quad (59) \] 

 \[ B=\frac{1}{Z_{N}}\Big\{\mathrm{e}^{-\frac{g\beta}{2N}[K+2\Delta J_{z}^{2}]}\Big[\frac{F_{1}}{\sqrt{M_{1}}}\sin\Big(t\sqrt{M_{1}}\Big)\cos\Big(t\sqrt{M_{2}}\Big)-\frac{F_{2}}{\sqrt{M_{2}}}\sin\Big(t\sqrt{M_{2}}\Big)\cos\Big(t\sqrt{M_{1}}\Big)\Big]\Big\}. \quad (60) \] 

From here on, the parameters  \( \mu \)  and  \( \gamma \)  will be given in units of the coupling constant  \( \alpha \) . The behavior of the component  \( \lambda_{2}(t) \)  does not significantly differ from the one corresponding to  \( \lambda_{1}(t) \) . Throughout the remainder of the paper we shall deal with the latter component and restrict ourselves to positive values of the anisotropy constant  \( \Delta \) .
Depending on the nature of interactions within the bath, we can distinguish two different cases. The first one corresponds to positive values of g, i.e. antiferromagnetic couplings between the constituents of the environment. In this case, as the number of spins increases, the plots saturate and a nontrivial limit exists as shown in Fig. 1. This will be investigated in the following section. The other case corresponds to negative values of g, i.e. fer-
 
![](./images/867767188633682175_1.jpg)

![](./images/867767188633682175_2.jpg)

FIG. 1: Time evolution of the components  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  for different values of the number of spins in the environment: N = 100 (dotted lines), N = 200 (dashed lines), and N = 400 (solid lines). The other parameters are  \( \gamma = 0 \) , g = 1,  \( \beta = 0.5 \) ,  \( \Delta = 0 \) , and  \( \mu = \alpha \) . The initial conditions are  \( \lambda_{3}(0) = \frac{1}{2} \) ,  \( \lambda_{1,2}(0) = \frac{3}{8} \) .

![](./images/867767188633682175_3.jpg)

(a)

![](./images/867767188633682175_4.jpg)

![](./images/867767188633682175_5.jpg)

![](./images/867767188633682175_6.jpg)

(b)

FIG. 2: The Gaussian decay of the Bloch vector components  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  in the case of ferromagnetic interactions: (a) N=100 and (b) N=200. The plot on the left of each subfigure corresponds to  \( \lambda_{3}(t) \) , the one on the right corresponds to  \( \lambda_{1}(t) \) . The other parameters are  \( \gamma=2\alpha \) ,  \( \beta=1 \) , g=-5,  \( \Delta=0.5 \) ,  \( \mu=0 \) ,  \( \lambda_{3}(0)=\frac{1}{2} \) , and  \( \lambda_{1,2}(0)=\frac{3}{8} \) .

romagnetic couplings within the bath. When  \( \Delta < 1 \)  the components of the Bloch vector exhibit in general Gaussian decay accompanied by fast damped oscillations even when the strength of the magnetic field is very weak. In contrast to  \( \lambda_{1}(t) \) , the component  \( \lambda_{3}(t) \)  decays faster as the number of spins increases. When the latter is small,  \( \lambda_{3}(t) \)  may revive to decay again and so forth. The numerical simulation shows that the details of the time evolution of the reduced density matrix are rather complex and depend on the different values of the parameters of the model, including the number of bath spins. For example if we set  \( \Delta = 0 \) , we observe that the oscillations are quickly suppressed with the increase of the strength of the magnetic field, or the value of the coupling constant  \( \gamma \) . In this case, the components  \( \lambda_{2,3}(t) \)  do not vanish at long time scales; the corresponding asymptotic values depend, however, on N in contrast to the antiferromagnetic case. For large values of the coupling constant g, the component  \( \lambda_{1}(t) \)  quickly decays whereas  \( \lambda_{3}(t) \)  oscillates around zero with large amplitudes (typically of the same order of magnitude as the corresponding initial value). We also notice that the frequencies of the damped oscillations increase with the increase of the number of bath spins as shown in Fig. 2. Roughly speaking, when  \( \Delta > 1 \) , the behavior of the components of the Bloch vector is quiet similar to the antiferromagnetic counterpart. For example when  \( \gamma = 0 \) , the components  \( \lambda_{i}(t) \)  show saturation behavior with respect to the number of spins N; their asymptotic values are different from zero.

In order to explain the differences between the behavior of the reduced density matrix in the ferromagnetic and the antiferromagnetic environments, we note that in the latter case, the form of interactions favors antiparallel spins. This is the reason for which the ground state of the antiferromagnetic bath,  \( |\Psi_{G}\rangle \) , is equal to  \( |0,0\rangle \) . On the contrary, ferromagnetic interactions force the spins in the bath to align along an arbitrary direction in the space. In this case  \( |\Psi_{G}\rangle \)  belongs to the subspace  \( C^{N+1} \)  spanned by the state vectors  \( |\frac{N}{2}, m\rangle \)  corresponding to  \( j = \frac{N}{2} \) . For instance, when  \( \Delta > 1 \) , the ground state of the bath turns out to be doubly degenerate, namely  \( |\Psi_{G}\rangle = |\frac{N}{2}, \pm\frac{N}{2}\rangle \) . For  \( \Delta < 1 \) , we simply have  \( |\Psi_{G}\rangle = |\frac{N}{2}, 0\rangle \) . However, when  \( \Delta = 1 \) , the ground energy of the bath is independent of the quantum number m; the degeneracy of  \( |\Psi_{G}\rangle \)  is equal to  \( N + 1 \) . Hence we conclude that the Hamiltonian  \( H_{B} \)  displays quantum phase transition at  \( \Delta = 1 \) . This is the reason for which the reduced dynamics depends on whether the anisotropy constant is less or greater than one. Note that the mean value of  \( J^{2} \)  is close to zero in the case of antiferromagnetic interactions within the spin bath in contrast with the ferromagnetic case where  \( \langle J^{2}\rangle \sim N^{2} \) . Obviously, the central spin decoheres less if the spin bath, to which it couples, is characterized by a total angular momentum close to zero. At zero temperature, the antiferromagnetic bath occupies its ground state  \( |0, 0\rangle \)  which is an eigenvector of  \( H_{B} \) , and satisfies
 

 \( H_{SB}|\pm\rangle\otimes|0,0\rangle=0 \) . Hence, the central spin remains decoupled from the bath if the initial state factorizes: the two-level system preserves its coherence regardless of the number of environmental spins. Let us now consider the case where  \( \gamma=0 \)  and  \( \Delta>1 \) . At low temperatures, the total angular momentum of the ferromagnetic bath has the tendency to be directed along the z direction. Since the central spin couples to the bath through Heisenberg XY interactions ( \( \gamma=0 \) ), we end up with a situation quiet similar to that where g>0. The above results show that properties of the bath at zero temperature affect the behavior of the reduced dynamics when T>0. At infinite temperature, the ferromagnetic and antiferromagnetic environments become completely unpolarized; the reduced dynamics displays the same behavior in both systems as N increases.

## IV. THE LIMIT  \( N \rightarrow \infty \) 

This section is devoted to the case of an infinite number of spins in the environment, i.e. the case  \( N \rightarrow \infty \) . We investigate the effect of the bath temperature, the external magnetic field, and the anisotropy constant on the reduced density matrix of the central spin. To this end it should be noted that the trace of the operators  \( J_{\pm} / \sqrt{N} \)  together with  \( J_{z} / \sqrt{N\} \)  is identically zero, namely

 \[ \mathrm{tr}_{B}\Big\{\frac{J_{\pm}}{\sqrt{N}}\Big\}=\mathrm{tr}_{B}\Big\{\frac{J_{z}}{\sqrt{N}}\Big\}=0. \quad (61) \] 

A more general property of the trace of the lowering and raising operators can be expressed as

 \[ \begin{align*}\lim_{N\to\infty}2^{-N}\mathrm{tr}_{B}\Big\{\prod_{i=1}^{k}\Big(\frac{J_{\pm}J_{\mp}}{N}\Big)^{n_{i}}\Big\}\\=\lim_{N\to\infty}2^{-N}\mathrm{tr}_{B}\Big\{\prod_{i=1}^{k}\Big(\frac{J_{\pm}}{\sqrt{N}}\Big)^{n_{i}}\Big(\frac{J_{\mp}}{\sqrt{N}}\Big)^{n_{i}}\Big\}=\frac{n!}{2^{n}},\end{align*} \quad (62) \] 

where  \( n = \sum_{i=1}^{k} n_{i} \)  is positive integer; the trace vanishes for all the cases in which  \( J_{+} \) and  \( J_{-} \) appear with different exponents. This means that  \( J_{\pm} / \sqrt{N} \)  are well-behaved fluctuation operators with respect to the tracial state. Hence in the limit  \( N \to \infty \) , the operator  \( J_{+} / \sqrt{N} \)  converges to a complex random variable z with the probability density function \( ^{16} \) 

 \[ z\mapsto\frac{2}{\pi}\mathrm{e}^{-2|z|^{2}}. \quad (63) \] 

Here, we wish to mention the similarity that exists between relation (62) and

 \[ 4\int\limits_{0}^{\infty}t dt t^{2n}\mathrm{e}^{-2t^{2}}=\frac{n!}{2^{n}} \quad (64) \] 

which is a special case of  \( \int\limits_{0}^{\infty}t^{2n+1}\mathrm{e}^{-at^{2}}dt=\frac{n!}{2^{n+1}} \) , where  \( n=0,1,2,\ldots \) , and the real part of a satisfies  \( \operatorname{Re}(a)>0 \) .

The operator  \( J_{z}/\sqrt{N} \)  also converges to a real random variable m (to be differentiated from the eigenvalue m) when  \( N \to \infty \) , with the probability density function

 \[ m\mapsto\sqrt{\frac{2}{\pi}}\mathrm{e}^{-2m^{2}}. \quad (65) \] 

For example, consider the operator  \( e^{-i\frac{2\gamma t}{\sqrt{N}}J_{z}} \)  and let us calculate

 \[ \mathrm{t r}_{B}\Big\{\mathrm{e}^{-i\frac{2\gamma t}{\sqrt{N}}J_{z}}\Big\}=\prod_{k=1}^{N}\mathrm{t r}e^{-i\frac{\gamma t}{\sqrt{N}}\sigma_{z}^{k}}. \quad (66) \] 

The trace under the product in the right-hand side of the above equation can be easily evaluated as  \( 2\cos(\frac{\gamma t}{\sqrt{N}}) \) . Consequently,

 \[ \mathrm{t r}_{B}\Big\{\mathrm{e}^{-i\frac{2\gamma t}{\sqrt{N}}J_{z}}\Big\}=2^{N}\Big[\cos\Big(\frac{\gamma t}{\sqrt{N}}\Big)\Big]^{N}. \quad (67) \] 

Expanding the cosine function in a Taylor series and taking the limit  \( N \to \infty \)  yield

 \[ \begin{align*}\lim_{N\to\infty}2^{-N}\mathrm{tr}_{B}\Big\{\mathrm{e}^{-i\frac{2\gamma t}{\sqrt{N}}J_{z}}\Big\}&=\lim_{N\to\infty}\Big[1-\frac{\gamma^{2}t^{2}}{2N}+O\Big(\frac{1}{N^{2}}\Big)\Big]^{N}\\&=\mathrm{e}^{-\frac{\gamma^{2}t^{2}}{2}}.\end{align*} \quad (68) \] 

On the other hand we have

 \[ \sqrt{\frac{2}{\pi}}\int\limits_{-\infty}^{\infty}\mathrm{e}^{-2m^{2}-2i\gamma t m}d m=\mathrm{e}^{-\frac{\gamma^{2}t^{2}}{2}}, \quad (69) \] 

which is in agreement with Eq. (68). In particular we can infer that

 \[ \lim_{N\to\infty}2^{-N}\mathrm{tr}_{B}\Big(J_{z}/\sqrt{N}\Big)^{2n}=\frac{\Gamma(n+\frac{1}{2})}{2^{n}\sqrt{\pi}}, \quad (70) \] 

where  \( \Gamma(z) \)  is Euler gamma function. We shall use the latter results when we investigate the short-time behavior of the reduced density matrix in the case where  \( \gamma \)  is different from zero.

One can check that for large values of N,

 \[ \begin{align*}\mathrm{tr}_{B}\Big\{\Big(\frac{J_{z}}{\sqrt{N}}\Big)^{k}\Big(\frac{J_{\pm}J_{\mp}}{N}\Big)^{\ell}\Big\}\approx&2^{-N}\mathrm{tr}_{B}\Big\{\Big(\frac{J_{z}}{\sqrt{N}}\Big)^{k}\Big\}\\&\times\mathrm{tr}_{B}\Big\{\Big(\frac{J_{\pm}J_{\mp}}{N}\Big)^{\ell}\Big\}.\end{align*} \quad (71) \] 

For odd powers of  \( J_{z} \) , the left-hand side of the above relation vanishes as N increases; the right-hand side is always zero. Eq. (71) simply implies that the operators  \( J_{\pm}J_{\mp}/N \)  and  \( J_{z}/\sqrt{N} \)  become uncorrelated under the tracial state at large values of N. Note that the above state corresponds to a bath of N independent
 

spin- \( \frac{1}{2} \)  particles, i.e. the state of maximum entropy. In the limit of large number of spins such a bath has the tendency to behave as a classical stochastic system. The scaled bath operators  \( J_{\alpha}/\sqrt{N} \)  (where  \( \alpha \equiv x, y, z \) ) converge to independent commuting random variables. For instance, we can easily show that the trace over the environmental degrees of freedom of the operator  \( \exp\left[\frac{\epsilon t}{\sqrt{N}}\left(a_{1}J_{x} + a_{2}J_{y} + a_{3}J_{z}\right)\right] \) , where  \( a_{1,2,3} \in C \)  and  \( \epsilon = \sqrt{\pm1} \) , is given by  \( 2^{N}\left\{\cosh\left[\frac{\epsilon t}{2\sqrt{N}}\sqrt{a_{1}^{2} + a_{2}^{2} + a^{2}_{3}}\right]\right\}^{N} \) .

at least for bounded functions  \( f : C \times R \to R \) . The latter relation has been numerically checked for large number of functions; the agreement between its two sides is perfect. In fact, the class of functions for which the integral in the right-hand side of Eq. (72) exists contains all the functions having the form  \( \mathrm{e}^{-(a|z|^{2}+bm^{2})}h(|z|^{2},m) \)  where h is bounded and a and b are complex numbers satisfying  \( \mathrm{Re}(a) > -2, \mathrm{Re}(b) > -2 \) . If the latter conditions are not satisfied then the integral does not converge. This is the reason for which we shall restrict ourselves to the antiferromagnetic case where g and  \( \Delta \)  are positive.

Under the above assumptions, it is possible to evaluate the quantity

 \[ \begin{align*}\bar{Z}&=\lim_{N\to\infty}2^{-N}Z_{N}\\&=\Big(\frac{2}{\pi}\Big)^{3/2}\int\limits_{-\infty}^{\infty}dm\int\limits_{\mathbb{C}}dz dz^{*}\mathrm{e}^{-(2+g\beta\Delta)m^{2}-(2+g\beta)|z|^{2}}\end{align*} \quad (73) \] 

by making use of the polar coordinates \((r,\phi)\) where \(z = re^{i\phi}\). A straightforward calculation yields

 \[ \bar{Z}=\frac{2\sqrt{2}}{(2+g\beta)\sqrt{2+g\beta\Delta}}\rightarrow\frac{2}{(2+g\beta)} \quad (74) \] 

when  \( \Delta\to0 \) . Obviously, if  \( g\beta=0 \)  then  \( \bar{Z}=1 \) . The agreement between the right-hand side and the left-hand side of Eqs. (72) is illustrated in Table I where we display  \( 2^{-N}Z_{N} \)  at different values of N and compare it with  \( \bar{Z} \)  for g=2,  \( \Delta=5 \)  and  \( \beta=1 \) ; the agreement is clearly very good for N=5000.

Let us now focus on the general structure of Eqs. (55)-(57). Clearly, we need to evaluate terms having the general form
If we expand the cosh function in Taylor series and take the limit  \( N \to \infty \) , as we did in Eq. (68), we end up with the result  \( \exp[\frac{\epsilon^{2}\pi}{8}(a_{1}^{2}+a_{2}^{2}+a_{3}^{2})] \) . The latter can be obtained by multiple integration over three independent random variables each of which has the same probability density function as m [see Eq. (69)]. It follows that the random variables z and m can be treated as independent in the limit  \( N \to \infty \) .

From the above discussion, we can conclude that

 \[ \lim_{N\to\infty}2^{-N}\mathrm{tr}_{B}\Big\{f\Big(\frac{J_{\pm}J_{\mp}}{N},\frac{J_{z}}{\sqrt{N}}\Big)\Big\}=\Big(\frac{2}{\pi}\Big)^{3/2}\int\limits_{-\infty}^{\infty}dm\int\limits_{\mathbb{C}}dzdz^{*}f(|z|^{2},m)\mathrm{e}^{-2(m^{2}+|z|^{2})} \quad (72) \] 

TABLE I:  \( 2^{-N}Z_{N} \)  at different values of N for g = 2,  \( \Delta = 5 \)  and  \( \beta = 1 \) ;  \( \bar{Z} = 0.204124 \) .

<table><tr><td>N</td><td>10</td><td>100</td><td>1000</td><td>5000</td></tr><tr><td>\( 2^{-N}Z_{N} \)</td><td>0.203026</td><td>0.203997</td><td>0.204111</td><td>0.204122</td></tr></table>

 \[ \frac{1}{Z_{N}}\mathrm{tr}_{B}\Big\{f\Big(\frac{J_{\pm}J_{\mp}}{N},\frac{J_{z}}{\sqrt{N}}\Big)\Big\}=\frac{2^{-N}\mathrm{tr}_{B}\Big\{f\Big(\frac{J_{\pm}J_{\mp}}{N},\frac{J_{\pm}}{\sqrt{N}}\Big)\Big\}}{2^{-N}Z_{N}}. \quad (75) \] 

As  \( N \rightarrow \infty \) , the previous quantity tends to

 \[ \langle f\rangle=\bar{Z}^{-1}4\Big(\frac{2}{\pi}\Big)^{1/2}\int\limits_{-\infty}^{\infty}dm\int\limits_{0}^{\infty}rdr f(r^{2},m)\mathrm{e}^{-2(m^{2}+r^{2})}. \quad (76) \] 

This is permissible since the functions of interest appearing in Eqs (55)-(57) fulfil all the conditions mentioned above. Note that the factor 4 in Eq. (76) appears after performing the integration with respect to the polar coordinate  \( \phi \)  (this actually follows from the symmetry with respect to the z direction). It is also quiet interesting to notice that the behavior of the central spin when  \( -2 < g\beta < 0 \)  and  \( -2 < \frac{g\beta\Delta}{2} < 0 \)  is similar to that where g > 0 and  \( \Delta > 0 \)  as indicated by the conditions on the convergence of the integral in Eq. (72).

## A. The case  \( \gamma = 0 \) 

Let us assume that the coupling constant  \( \gamma \)  is equal to zero. First of all, it should be noted that, although the operator  \( J_{z}/\sqrt{N} \)  converges to a random variable, we can neglect the contribution of  \( J_{z}/N \)  when N becomes very large. This means that in the limit  \( N \to \infty \) , the
 
![](./images/867767188633682175_7.jpg)

![](./images/867767188633682175_8.jpg)

FIG. 3: Evolution in time of  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  for N = 400 (dotted lines), and  \( N \to \infty \)  (solid lines); the dashed lines correspond to the asymptotic values. Other parameters are  \( \gamma = 0 \) , g = 1,  \( \beta = 5 \) ,  \( \Delta = 0.5 \) ,  \(  \mu = 0.4\alpha \) ,  \( \lambda_{3}(0) = \frac{1}{2} \)  and  \( \lambda_{1,2}(0) = \frac{3}{8} \) .

quantities  \( M_{1,2} \)  do not depend on the random variable m; the sinh (sin) and the cosh (cos) functions appearing in Eq. (55) [Eqs. (56)-(57)] should be replaced by zero and one, respectively. We only need to integrate with respect to the random variable z since the integrals with respect to m occurring in the numerator and denominator of Eq. (76) cancel each other. One then concludes that the anisotropy constant  \( \Delta \)  has no effect on the dynamics of the central spin when  \( N \to \infty \) . This is due to the fact that  \( H_{SB} \)  simplifies to Heisenberg XY Hamiltonian. Only transverse interactions contribute to the reduced dynamics when N is sufficiently large because  \( J_{z}/\sqrt{N} \)  and K/N (or equivalently  \( J_{\pm}J_{\mp}/N \) ) become practically uncorrelated under the tracial state [see Eq.(71)].

Hence, in the limit of an infinite number of spins within the bath we obtain

 \[ \lambda_{3}(t)=\lambda_{3}(0)\Big(1-n(t)\Big), \quad (77) \] 

where

 \[ \eta(t)=\Big\langle2r^{2}\frac{\sin^{2}\Big(t\sqrt{\mu^{2}+r^{2}}\Big)}{\mu^{2}+r^{\mathrm{c}}}e^{-g\beta\left[r^{2}+\Delta m^{2}\right]}\Big\rangle. \quad (78) \] 

Note that the time variable is now given in units of  \( \alpha \) . We show in the appendix that the above function can be written as

 \[ \begin{align*}\eta(t)&=1-\cos(2\mu t)+\frac{it}{2}\sqrt{\frac{\pi}{2+g\beta}}\Big\{\mathrm{erf}\Big[\frac{\mu(g\beta+2)-it}{\sqrt{g\beta+2}}\Big]-\mathrm{erf}\Big[\frac{\mu(g\beta+2)+it}{\sqrt{g\beta+2}}\Big]\Big\}\mathrm{e}^{[(2+g\beta)\mu^{2}-\frac{r^{2}}{2+g\beta}]}\\&-(g\beta+2)\mu^{2}\mathrm{e}^{(g\beta+2)\frac{\mu^{2}}{2}}\Gamma\Big[0,(g\beta+2)\mu^{2}\Big]+\mu^{2}(g\beta+2)\mathrm{e}^{(g\beta+2)\mu^{2}}\mathrm{Re}\Big\{\Gamma\Big[0,(g\beta+2)\mu^{2}+2\mu it\Big]\Big\}\\&+\mu^{2}\mathcal{M}(t;\mu,\beta),\end{align*} \quad (79) \] 

where

 \[ \mathrm{erf}(z)=\frac{2}{\sqrt{\pi}}\int\limits_{0}^{z}e^{-t^{2}}dt, \quad (80) \] 

 \[ \Gamma(a,z)=\int\limits_{z}^{\infty}t^{a-1}e^{-t}dt. \quad (81) \] 

are, respectively, the error and the incomplete gamma functions \( ^{28} \) . The function M is given by Eq. (A.10) of the appendix.

The remaining components of the Bloch vector are given by

 \[ \lambda_{1}(t)=\lambda_{1}(0)\Big[\zeta(t)+\frac{1}{2}\eta(t)\Big]+\lambda_{2}(0)\xi(t), \quad (82) \] 

 \[ \lambda_{2}(t)=\lambda_{2}(0)\Big[\zeta(t)+\frac{1}{2}\eta(t)\Big]-\lambda_{1}(0)\xi(t), \quad (83) \] 

where
 

 \[ \begin{align*}\zeta(t)&=\left\langle\mathrm{e}^{-g\beta(r^{2}+\Delta m^{2})}\cos\Big(2t\sqrt{\mu^{2}+r^{2}}\Big)\right\rangle\\&=\cos\Big(2\mu t\Big)+\frac{it}{2}\mathrm{e}^{\left[(2+g\beta)\mu^{2}-\frac{t^{2}}{2+g\beta}\right]\sqrt{\frac{\pi}{2+g\beta}}}\Big\{\mathrm{erf}\Big[\frac{\mu(g\beta+2)+it}{\sqrt{g\beta+2}}\Big]-\mathrm{erf}\Big[\frac{\mu(g\beta+2)-it}{\sqrt{g\beta+2}}\Big]\Big\},\end{align*} \quad (84) \] 

and

 \[ \begin{align*}\xi(t)&=\left\langle\mu\mathrm{e}^{-g\beta(r^{2}+\Delta m^{2})}\frac{\sin\left(2t\sqrt{\mu^{2}+r^{2}}\right)}{\sqrt{\mu^{2}+{r^{2}}}}\right\rangle\\&=\frac{i\mu}{2}\sqrt{\pi(2+g\beta)}\mathrm{e}^{\left[(2+g\beta)\mu^{2}-\frac{t^{2}}{2+g\beta}\right]}\Big\{\mathrm{erf}\Big[\frac{\mu(g\beta+2)-it}{\sqrt{g\beta+2}}\Big]-\mathrm{erf}\Big[\frac{\mu(g\beta+2)+it}{\sqrt{g\beta+2}}\Big]\Big\}.\end{align*} \quad (85) \] 

The asymptotic behavior of the reduced density matrix can be easily determined as follows. Let us begin with the simplest functions namely  \( \zeta(t) \)  and  \( \xi(t) \) . Their limits when  \( t \to \infty \)  are equal to zero which immediately follows from the Riemann-Lebesgue lemma

 \[ \lim_{t\to\infty}\zeta(t)=\lim_{t\to\infty}{\xi(t)}=0. \quad (86) \] 

The same lemma can be applied to the function  \( \eta(t) \)  after some simplifications of the integrals of interest as shown in the appendix. Only one term survives the above approach when t goes to infinity, namely

 \[ \lim_{t\to\infty}\eta(t)=1-\eta^{\infty}, \quad (87) \] 

where

 \[ \eta^{\infty}=\mu^{2}(g\beta+2)\mathrm{e}^{\mu^{2}(g\dot{\beta}+2)}\Gamma\Big(0,\mu^{2}(g\dot{\beta}+2)\Big). \quad (88) \] 

Hence, the asymptotic behavior of the reduced density matrix can be expressed as

 \[ \lim_{t\to\infty}\vec{\lambda}(t)=\vec{\lambda}_{0}-\eta^{\infty}\mathcal{W}\vec{\lambda}(0) \quad (89) \] 

with

 \[ \vec{\lambda}_{0}=\frac{1}{2}\begin{pmatrix}\lambda_{1}(0)\\ \lambda_{2}(0)\\ 0\end{pmatrix},\quad\mathcal{W}=\begin{pmatrix}\frac{1}{2}&0&0\\ 0&\frac{1}{2}&\mathbf{0}\\ 0&\mathbf{0}&-1\end{pmatrix}. \quad (90) \] 

The evolution in time of the components  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  is shown in Fig. 3 for N = 400 spins in the environment, along with the corresponding infinite case and the asymptotic limits obtained in Eq. (89). We can see that the off-diagonal elements of the reduced density matrix show partial decoherence. At low temperature, the relevant bath states are those with low energies (i.e. j close to zero). In this case, the central spin is weakly coupled to the bath and hence preserves most of its coherence. At high temperature, the two-level system becomes more correlated with the bath which, however, behaves as a system of independent uncoupled particles. Thus quantum fluctuations within the antiferromagnetic spin-environment reduce the effect of the decoherence of the central spin. In the following, we discuss how the bath temperature and the strength of the applied magnetic field affect the decay of the elements of the reduced density matrix.

![](./images/867767188633682175_9.jpg)

![](./images/867767188633682175_10.jpg)

FIG. 4: The decay of the components  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  for g = 0 (dotted lines), g = 5 (dashed lines), and g = 10 (solid lines). Other parameters are  \( \beta = 1 \) ,  \( \gamma = \Delta = 0 \) ,  \( \mu = 0.1\alpha \) ,  \( \lambda_{3}(0) = \frac{1}{2} \)  and  \( \lambda_{1,2}(0) = \frac{3}{8} \) .

Clearly, if  \( \mu=0 \) , the vector component  \( \lambda_{3}(t) \)  vanishes when  \( t\to\infty \)  regardless of the bath temperature. This means that  \( \rho_{11}(\infty)=\rho_{22}(\infty)=\frac{1}{2} \) , which is obviously independent of the initial state of the central system. On the contrary, the off-diagonal elements tend asymptotically.
 

ically to half of their initial values. This follows from the fact that the temperature-dependent quantity  \( \eta^{\infty} \)  is proportional to the magnetic field strength. The latter results are mainly due to the rotational symmetry of the model Hamiltonian together with the randomness of the interactions within the bath. Fig 4 illustrates the difference in the decoherence process between the case of a static bath  \( (g=0) \)  and a dynamic bath  \( (g\neq0) \) . We can see that the asymptotic value of  \( \lambda_{1}(t) \)  decreases with the increase of g in contrast to  \( \lambda_{3}(t) \)  which assumes larger asymptotic values when g increases. However, at short times the above components decay slower with the increase of g, implying that strong quantum correlations within the environment suppress the effect of the decoherence process \( ^{29} \) . As we shall see below, the decay of the reduced density matrix exhibits a reverse behavior with respect to the temperature of the bath. This can be explained by the dependence of the decoherence time constant of our model, which turns out to be equal to  \( \tau=\sqrt{\frac{2+g\beta}{\alpha^{2}}} \)  as revealed by Eqs. (79), (84) and (85), on the product  \( g\beta \) . Clearly,  \( \tau\to\infty \)  as  \( g\to\infty \)  or/and  \( T\to0 \) , which confirms the above statements.

![](./images/867767188633682175_11.jpg)

![](./images/867767188633682175_12.jpg)

FIG. 5: Dependence of  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  on the strength of the magnetic field in the case  \( N\to\infty \) :  \( \mu=0 \)  (dotted lines),  \( \mu= \)   \( 0.5\alpha \)  (dashed lines), and  \( \mu=2\alpha \)  (solid lines). The parameters are  \( \gamma=0 \) ,  \( g\beta=2 \) ,  \( \lambda_{3}(0)=\frac{1}{2} \)  and  \( \lambda_{1,2}(0)=\frac{3}{8} \) .

Figure 5 illustrates the dependence of the components of the Bloch vector on the strength of the magnetic field. We can see that  \( \lambda_{1}(t) \)  decays with the increase of  \( \mu \)  whereas  \( \lambda_{3}(t) \)  approaches its initial value. Indeed, by making use of the following asymptotic expression of the incomplete gamma function \( ^{28} \) 

 \[ \Gamma(a,z)\sim z^{a-1}\mathrm{e}^{-z}\Big[1+\frac{a-1}{z}+\frac{(a-1)(a-2)}{z^{2}}+\ldots\Big], \quad (91) \] 

when  \( z \to \infty \)  in  \( \left| \arg z \right| < 3\pi/2 \) , we obtain

 \[ \lim_{\mu,\beta\to\infty}\eta^{\infty}=1. \quad (92) \] 

Therefore, if the ratio  \( \mu/\alpha \)  is infinitely big then the off-diagonal elements of the reduced density matrix tend asymptotically to zero; the diagonal ones assume their initial values. The above results can be explained by the fact that the effect of the bath on the dynamics of the central spin can be neglected when  \( \mu \)  is very large compared to  \( \alpha \) . The evolution in time is thus governed by the free Hamiltonian  \( H_{S} \)  which does not affect the diagonal elements of the reduced density matrix. The off-diagonal elements, however, show periodic oscillations; the vanishing asymptotic values obtained from Eqs. (87) and (92) will never be reached since the decoherence time constant is infinite ( \( \alpha \rightarrow 0 \) ).

![](./images/867767188633682175_13.jpg)

![](./images/867767188633682175_14.jpg)

FIG. 6: Dependence of  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  on the bath temperature in the case  \( N\to\infty \) :  \( \beta=0 \)  (dotted lines),  \( \beta=1 \)  (dashed lines), and  \( \beta=10 \)  (solid lines). The parameters are  \( \gamma=0 \) ,  \( g=2 \) ,  \( \mu=0.5\alpha \) ,  \( \lambda_{3}(0)=\frac{1}{2} \)  and  \( \lambda_{1,2}(0)=\frac{3}{8} \) .

From Fig. 6 it can be seen that the bath temperature has a reverse effect on the decay of the reduced density matrix elements. The components  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  decay faster with the increase of T. Furthermore, we can see that the diagonal elements assume larger asymptotic values in contrast with the off-diagonal ones. In the limit of
 

zero temperature, the asymptotic behavior is identical to the one corresponding to  \( \mu \rightarrow \infty \) , see Eq. (89). Indeed, at zero temperature the bath and the central spin evolve independently from each other as we already mentioned in the previous section. Once again, we find that the dynamics of the central spin is governed by the free Hamiltonian  \( H_{S} \)  which preserves the coherence of the central system.

![](./images/867767188633682175_15.jpg)

![](./images/867767188633682175_16.jpg)

![](./images/867767188633682175_17.jpg)

FIG. 7: The short-time behavior of  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  in the case  \( N \to \infty \) . The solid lines correspond to the exact solutions, the dotted lines denote the approximations (93-94). Here,  \( \gamma = 0 \) ,  \( g\beta = 1 \) ,  \( \mu = 0.5\alpha \) ,  \( \lambda_{3}(0) = \frac{1}{2} \)  and  \( \lambda_{1,2}(0) = \frac{3}{8} \) .

Let us now discuss the short-time behavior of the reduced dynamics. The aim here is to find simple analytical expressions which describe the variation of the reduced density matrix at short time scales. It is clear from the expressions of the functions  \( \eta(t) \) ,  \( \zeta(t) \)  and  \( \xi(t) \)  that the term of interest which describes the decay of the Bloch vector components is given by  \( \mathrm{e}^{-\frac{t^{2}}{(g\beta+2)}} \) . We shall look for functions of the form  \( \mathrm{e}^{-\frac{t^{2}}{(g\beta+2)}}g(t) \)  where  \( g(t) \)  is some complex-valued function of the time. In the case of the off-diagonal elements, the ansatz  \( g(t)=\mathrm{e}^{2i\mu t} \)  can be justified by the competition of two processes, namely oscillations due to the external magnetic field and damping due to the coupling with the environment. In the limiting case where the magnetic field is absent, it is found that for small values of the time, the decay is purely Gaussian. On the other hand if we assume that there is no coupling between the bath and the central spin, i.e.  \( \alpha=0 \) , then the dynamics is governed by the external magnetic field.

![](./images/867767188633682175_18.jpg)

FIG. 8: (Color online) Purity evolution for different values of the bath temperature in the case  \( N \rightarrow \infty \)  with  \( \gamma = 0 \) , g = 1 and  \( \mu = 0 \) . The initial conditions are  \( \lambda_{3}(0) = \sqrt{\frac{2}{8}} \) ,  \( \lambda_{1,2}(0) = \frac{1}{4} \) .

![](./images/867767188633682175_19.jpg)

FIG. 9: (Color online) Evolution in time of the purity for different values of the bath temperature in the case  \( N \rightarrow \infty \)  with  \( \gamma = 0 \) , g = 1 and  \( \mu = \alpha \) .

The component  \( \lambda_{3}(t) \)  is not affected by the magnetic field even when there is no coupling between the spin and the bath. It is shown in Ref. 15 that this component decays two times faster than the other ones. Consequently, the short-time behavior of the reduced density matrix can be described by

 \[ \frac{\lambda_{3}(t)}{\lambda_{3}(0)}\approx\exp\Bigl(-\frac{2t^{2}}{2+g\beta}\Bigr), \quad (93) \] 

 \[ \frac{\lambda_{1}(t)-i\lambda_{2}(t)}{\lambda_{1}(0)-i\lambda_{2}(\mathbb{0})}\approx\exp\Bigl(-\frac{t^{2}}{2+g\beta}+2i\mu t\Bigr). \quad (94) \] 

In Fig. 7, the short time behavior of the Bloch vector components  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  is shown together with the approximations (93) and (94); these are in good agreement with the exact solutions.
 
![](./images/867767188633682175_20.jpg)

![](./images/867767188633682175_21.jpg)

FIG. 10: Evolution of  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  for N = 600 (dotted lines) and  \( N \to \infty \)  (solid lines). The dashed lines correspond to the asymptotic values. Here,  \( \gamma = 2\alpha \) , g = 1,  \( \beta = 1.5 \) ,  \( \Delta = 1 \) ,  \( \mu = 0.3\alpha \) ,  \( \lambda_{3}(0) = \frac{1}{2} \)  and  \( \lambda_{1,2}(0) = \frac{3}{8} \) . The plots corresponding to  \( \lambda_{3}(t) \)  are almost identical, the latter component saturates with respect to N faster than  \( \lambda_{1}(t) \) .

There exist many measures that allow for the quantification of the degree of the decoherence due to the interaction with an environment. In this work we use the measure  \( D(t) = 1 - P(t) \) , where

 \[ P(t)=\mathrm{t r}\{\rho(t)^{2}\} \quad (95) \] 

Obviously, the functions  \( \zeta(t) \)  and  \( \xi(t) \)  tend to zero when  \( t \to \infty \) . Hence, even if we set  \( \mu = 0 \) , the asymptotic state is still temperature dependent. Nevertheless, the dependence of the Bloch vector components on the bath temperature is quiet similar to the one corresponding to  \( \gamma = 0 \) . The influence of the magnetic field on the dynamics of the central spin is appreciable only when its strength is sufficiently large; this can be seen from the absence of oscillations in the components  \( \lambda_{1}(t) \)  and  \( \lambda_{3}(t) \)  is the purity of the central system. Note that in the previous expression the trace is performed over the degrees of freedom of the central spin. The purity takes its maximum value 1 at pure states; its minimum value, 1/2, corresponds to the fully mixed state  \( \rho = 1_{2}/2 \) . In our case, the purity can be expressed in terms of the Bloch vector components as

 \[ P(t)=\frac{1}{2}\Big(1+\lambda_{1}(t)^{2}+\lambda_{2}(t)^{2}+\mathbf{\lambda}_{3}(t)^{2}\Big). \quad (96) \] 

The above expression shows that the decay of the purity in the short-time regime described by Eqs. (93)-(94) is Gaussian which reflects the non-Markovian character of the dynamics. The decay process is slowed down by decreasing the temperature of the bath and/or applying a magnetic field of sufficient strength as illustrated in Figs. 8 and 9. When  \( t \to \infty \) , the central spin shows partial decoherence; if  \( \mu = 0 \) , then the asymptotic value of the purity is independent of the bath temperature as expected (see Fig. 8).

## B. The case  \( \gamma \neq 0 \) 

The time dependence of the Bloch vector components when the constant  \( \gamma \)  is different from zero can be obtained with the same method used in the previous subsection. Since  \( \gamma \neq 0 \) , the quantities  \( M_{1,2} \)  are m-dependent which means that the effect of the anisotropy constant has to be taken into account. When  \( \gamma \neq 0 \) , we need to perform double integration with respect to the real variables r and m as shown in Eq. (72). By making use of the Riemann-Lebesgue lemma, it is possible to find the following asymptotic expression for the function  \( \eta(t) \)  obtained by replacing  \( \mu \)  by  \( \mu + \gamma m \)  in Eq. (78)(see Fig. 10)

 \[ \lim_{t\to\infty}\eta(t)=1-\frac{1}{\sqrt{\pi}}(2+g\beta)\sqrt{2+g\beta\Delta}\int\limits_{-\infty}^{\infty}(\mu+\gamma m)^{2}\mathrm{e}^{(\mu+\gamma m)^{3}(g\beta+2)-(2+g\beta\Delta)m^{2}}\Gamma\Big(0,(\mu+\gamma m)^{2}(2+g\beta)\Big)dm. \quad (97) \] 

displayed in figure 10. Fig. 11 shows that the off-diagonal elements decay slower and assume larger asymptotic values when the anisotropy constant  \( \Delta \)  increases. The opposite situation holds for the component  \( \lambda_{3}(t) \) , that is when  \( \Delta \)  decreases the latter component assumes larger asymptotic limits.

At short times the diagonal elements of the reduced density matrix do not depend on  \( \Delta \)  in contrast with the off-diagonal ones. In the case of the Heisenberg XY
 
![](./images/867767188633682175_22.jpg)

![](./images/867767188633682175_23.jpg)

FIG. 11: Dependence of  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  on the anisotropy constant in the case  \( N\to\infty \) :  \( \Delta=0 \)  (solid lines),  \( \Delta=5 \)  (dashed lines), and  \( \Delta=10 \)  (dotted lines). Here,  \( \gamma=2\alpha \) ,  \( g\beta=1 \) ,  \( \mu=0.1\alpha \) ,  \( \lambda_{3}(0)=\frac{1}{2} \)  and  \( \lambda_{1,2}(0)=\frac{3}{8} \) .

![](./images/867767188633682175_24.jpg)

![](./images/867767188633682175_25.jpg)

FIG. 12: The short-time behavior of  \( \lambda_{3}(t) \)  and  \( \lambda_{1}(t) \)  in the case  \( N\to\infty \) . The solid lines correspond to the exact solutions, the dotted lines denote the approximations (98-99). The parameters are  \( \gamma=1\alpha \) ,  \( \Delta=0 \) ,  \( g\beta=1 \)  and  \( \mu=5\alpha \) . The initial conditions are the same as in Fig.11.

model, i.e. when  \( \Delta = 0 \) , the short-time behavior of the Bloch vector components can be determined with the same procedure used in the case where  \( \gamma = 0 \) . The main difference here is that the contribution of the interaction  \( V = \frac{\gamma}{\sqrt{N}} S_{z}^{0} J_{z} \)  has to be taken into account. Using the result we obtained in Eq. (68), we can describe the short-time behavior of the reduced density matrix by (see Fig. 12)

 \[ \begin{aligned}\frac{\lambda_{3}(t)}{\lambda_{3}(0)}&\approx\exp\Bigl(-\frac{2t^{2}}{2+g\beta}\Bigr),\\\frac{\lambda_{1}(t)-i\lambda_{2}(t)}{\lambda_{1}(0)-i\lambda_{2}}(0)&\approx\exp\Bigl(-\frac{t^{2}}{2+g\beta}-\frac{\gamma^{2}t^{2}}{2}+2i\mu t\Bigr).\end{aligned} \quad (98) \quad (99) \] 

For  \( \Delta\neq0 \) , the situation is much more complicated; here we only discuss the special case where  \( \mu=\alpha=0 \) , and  \( \Delta>>1 \) . The last condition implies that the transverse term of  \( H_{B} \)  can be neglected compared to the longitudinal one. Under the above assumption,  \( H_{B} \)  simplifies to  \( g\Delta/NS_{z}^{2} \)  and thus all interactions are of Ising type. Therefore, the operators  \( H_{SB} \)  and  \( H_{B} \)  commute with each other which means that the diagonal elements are not affected by the coupling to the environment. The coherence of the central spin can be calculated as usual. Taking the limit of an infinite number of spins and using the probability density function corresponding to the random variable m, we find that the off-diagonal elements decay according to the Gaussian law  \( \exp\left[-\frac{\gamma^{2}t^{2}}{2+g\beta\Delta}\right] \) . Hence the larger the anisotropy constant the slower the decay of the off-diagonal elements, which explains the behavior at short times of  \( \lambda_{1}(t) \)  displayed in Fig. 11. More details about the case of Ising couplings can be found in Ref. 30. To end our discussion about the short-time behavior, it should be noted that the deviation of the short-time expressions (94) and (99) from the exact solutions depends on the value of the strength of the magnetic field. For small values of  \( \mu \) , the above relations are valid at relatively large intervals of time. However, as  \( \mu \)  increases, the domains of time for which the above approximations are valid become shorter.

The variation in time of the purity in this case differs from the one corresponding to  \( \gamma = 0 \)  by the suppression of the damped oscillations caused by the external magnetic field as shown in Fig 13. This is mainly due to the interaction described by the Hamiltonian V. Consequently, the central spin decoheres less when  \( \gamma \)  is equal to zero. The above result was expected because the longitudinal coupling vanishes: the central spin is less correlated
 
![](./images/867767188633682175_26.jpg)

FIG. 13: (Color online) Purity evolution for different values of the bath temperature in the case  \( N \rightarrow \infty \)  with  \( \gamma = 2\alpha \) ,  \( \Delta = 1 \) , g = 1, and  \( \mu = \alpha \) . The initial conditions are  \( \lambda_{3}(0) = \sqrt{\frac{2}{5}} \) ,  \( \lambda_{1,2}(0) = \frac{1}{4} \) .

to the environment and thus the destructive effect of the environment on the coherence of the two-level system is less appreciable. Indeed, the decoherence time constant is found to be inversely proportional to  \( \gamma \) , namely  \( \tau = \frac{1}{\alpha} \sqrt{\frac{4 + 2g\beta}{2 + \gamma^{2}(2 + g\beta)}} \) . This simply implies that  \( \tau \to 0 \)  as  \( \gamma \to \infty \) .

## V. CONCLUSION

In conclusion we have investigated the dynamics of a spin- \( \frac{1}{2} \)  particle, subjected to the effect of a locally applied external magnetic field, and coupled to anisotropic Heisenberg spin environment in thermal equilibrium. The reduced density matrix was analytically derived for finite number of spins in the environment and arbitrary values of the interaction strengths. The evolution in time of the central spin depends on the nature of interactions within the bath. In the case of ferromagnetic environment, the decay of the Bloch vector components is Gaussian accompanied by fast damped oscillations. In the antiferromagnetic case, the components of the bloch vector saturate with respect to the number of environmental spins and display partial decoherence. We showed that the partial trace over the degrees of freedom of the bath can be calculated using the convergence of the rescaled bath operators to normal independent Gaussian random variables. This allowed us to study the case of an infinite number of environmental spins, and to analytically derive the asymptotic behavior of the components of the Bloch vector. The above limit represents a good approximation for the cases with finite number of spins ( \( N \sim 100 \) ). At short time scales, the decay of the off-diagonal elements is found to be Gaussian with a decoherence time constant given by  \( \tau = \sqrt{\frac{2 + g\beta}{\alpha^{2}}} \)  ( \( \gamma = 0 \) ). This result is mainly due to the non-Markovian nature of the dynamics, which in turn follows from the time-independence of the bath correlation functions and the symmetry of the bath Hamiltonian. Also, it has been shown that the effect of low bath temperatures on the decoherence of the central spin is similar to that of strongly applied magnetic fields and large bath anisotropy. The results obtained in this work are valid for any number of spins in the environment and arbitrary values of the strength of the external magnetic field and the bath temperature. They are in good agreement with those of Ref. 21 where the authors studied decoherence of electron spins in quantum dots. The model can be generalized to the case of two or more interacting qubits where questions related to the decoherence and the entanglement can be investigated.

## Acknowledgments

Y. H. would like to express his gratitude for the warm hospitality extended to him during his visit to Institut de Physique, Université Mentouri-Constantine, Algeria, where this work was partially carried out. The financial support from the South African National Research Foundation within the Focus Area Programme Unlocking the Future is gratefully acknowledged.

## APPENDIX: DERIVATION OF THE ANALYTICAL FORM OF  \( \eta(t) \) 

This appendix is devoted to the derivation of the asymptotic behavior and the analytical form of the function  \( \eta(t) \)  appearing in Eq. (79). Explicitly we have  \( (\Delta = 0) \) 

 \[ \eta(t)=\frac{8}{Z}\int\limits_{0}^{\infty}\mathrm{e}^{-(g\beta+2)r^{2}}\frac{r^{2}}{\mu^{2}+r^{2}}\sin^{2}\Big(t\sqrt{\mu^{2}+r^{2}}\Big)d r. \quad (A.1) \] 

By making the following change of variable  \( r^{2}=s^{2}-\mu^{2} \)  and taking into account the trigonometric equality  \( \sin^{2}x=\frac{1}{2}\left[1-\cos(2x)\right] \) , we can rewrite the above function as

 \[ \begin{align*}\eta(t)&=\frac{2}{Z}\mathrm{e}^{(2+g\beta)\mu^{2}}\Biggl\{\int\limits_{\mu^{2}}^{\infty}dv^{2}\mathrm{e}^{-(2+g\beta)v^{2}}\Bigl[1-\cos(2vt)\Bigr]\\&-2\mu^{2}\Bigl[\int\limits_{v}^{\infty}\frac{dv}{v}\mathrm{e}^{-(2+g\beta)v^{2}}\Bigl(1-\cos(2vt)\Bigr)\Bigr]\Biggr\}.\end{align*} \quad (A.2) \] 

The Riemann-Lebesgue lemma implies that the second and the fourth terms involving the cosine function in the above expression vanish when  \( t \to \infty \) . The first term can
 

be easily evaluated and we simply get

 \[ \int\limits_{\mu^{2}}^{\infty}d v^{2}\mathrm{e}^{-(2+g\beta)v^{2}}=\frac{1}{2+g\beta}\mathrm{e}^{-(2+g\beta)\mu^{2}}. \quad (A.3) \] 

The third term reads

 \[ 2\int\limits_{\mu}^{\infty}\frac{dv}{v}\mathrm{e}^{-(2+g\beta)v^{2}}=\int\limits_{\mu^{2}(2+g\beta)}^{\infty}\frac{dv^{2}}{v^{2}}\mathrm{e}^{-v^{2}}=\Gamma\Big(0,(2+g\beta)\mu^{2}\Big), \quad (A.4) \] 

where we have made the change of variable  \( (2 + g\beta)v^{2} \rightarrow v^{2} \) . Taking into account the expression of  \( \bar{Z} \)  in Eq. (74) we obtain the asymptotic expression of  \( \eta(t) \)  displayed in Eq. (88).

The second term simplifies to

 \[ \mathrm{R e}\left\{2\mathrm{e}^{-\frac{t^{2}}{2+g\beta}}\int\limits_{\mu}^{\infty}v d v\exp\left[-(2+g\beta)\Big(v+\frac{i t}{2+g\beta}\Big)^{2}\right]\right\}=e^{-\frac{t^{2}}{2+g\beta}}\mathrm{R e}\Big\{\int\limits_{\delta_{1}}^{\infty}d v\frac{\mathrm{e}^{-v}}{2+g\beta}-\frac{2i t}{(2+g\beta)^{\frac{3}{2}}}\int\limits_{\delta}^{\infty}d v e^{-v^{2}}\Big\}, \quad (A.5) \] 

where  \( \delta=\sqrt{2+g\beta}(\mu+\frac{it}{2+g\beta}) \) . One can easily check that

 \[ \mathrm{R e}\left(I_{1}\right)=\frac{1}{2+g\beta}\exp\Bigl[-(2+g\beta)\mu^{2}+\frac{t^{2}}{2+g\beta}\Bigr]\cos\Bigl(2\mu t\Bigr). \quad (A.6) \] 

The second integral is given by the complementary error function, namely

 \[ I_{2}=\frac{\sqrt{\pi}i t}{(2+g\beta)^{\frac{3}{2}}}\mathrm{e r f c}\Big[\Big(\mu+\frac{i t}{2+g\beta}\Big)\sqrt{2+g\beta}\Big]. \quad (A.7) \] 

It is then sufficient to use the property 2 Im  \( \operatorname{erfc}(a+it)=i\left[\operatorname{erf}(a+it)-\operatorname{erf}(ai-it)\right] \) , where a is real and  \( \operatorname{Im}(x) \)  stands for the imaginary part of x, to get the first three terms appearing in the right-hand side of Eq. (79).

Similarly, we have

 \[ \begin{align*}\mathrm{Re}\Biggl\{2\int\limits_{\mu}^{\infty}\frac{dv}{v}\exp\Bigl[-(2+g\beta)\Bigl(v+\frac{it}{2+g\beta}\Bigr)^{2}\Bigr]\Biggr\}\\=\mathrm{Re}\Biggl\{2\int\limits_{\delta}^{\infty}\frac{ds}{s-\frac{it}{\sqrt{2+g\beta}}}\mathrm{e}^{-s^{2}}\Biggr\},\end{align*} \quad (A.8) \] 

where we have introduced the new variable  \(  s = (v + \frac{it}{\sqrt{2 + g\beta}}) \sqrt{2 + g \beta}  \) . By multiplying the numerator and the denominator of the quantity under the sign of integral by  \( s + \frac{it}{\sqrt{2 + g\beta}} \)  we get two new integrals. The first one is given by

 \[ \begin{align*}\mathrm{Re}\Biggl\{2\int\limits_{\delta}^{\infty}s ds\frac{\mathrm{e}^{-s^{2}}}{s^{2}+\frac{t^{2}}{2+g\beta}}\Biggr\}&=\mathrm{e}^{\frac{t^{2}}{2+g\beta}}\mathrm{Re}\Biggl\{\int\limits_{\delta_{2}}^{\infty}\frac{ds}{s}\mathrm{e}^{-s}\Biggr\}\\&=\exp\Biggl\{\frac{t^{2}}{2+g\beta}\Biggr\}\mathrm{Re}\Biggl\{\Gamma(0,\delta_{2})\Biggr\},\end{align*} \quad (A.9) \] 

where  \( \delta_{2}=(2+g\beta)\mu^{2}+2\mu it \) . The remaining integral defines the function M, namely

 \[ \begin{align*}\mathcal{M}(t;\mu,\beta)&=\exp\Big\{-\Big[\frac{t^{2}}{2+g\beta}-(2+g\beta)\mu^{2}\Big]\Big\}\\&\quad\times\mathrm{Re}\Biggl\{2it\sqrt{2+g\beta}\int\limits_{\delta}^{\infty}\frac{\mathrm{e}^{-s^{2}}}{s^{2}+\frac{t^{2}}{2+g\beta}}ds\Biggr\}.\end{align*} \quad (A.10) \] 

The analytical expressions of the functions  \( \xi(t) \)  and  \( \zeta(t) \)  can be determined with the same method. In the case  \( \gamma \neq 0 \)  we should replace  \( \mu \)  by  \( \mu + \gamma m \)  and then perform the integration with respect to m. For practical investigation, numerical integration is used.
 

 \( ^{6} \)  J. H. Reina, L. Quiroga, and N. F. Johnson, Phys. Rev. A 65, 032326 (2002).

 \( ^{7} \)  D. Gottesman, Phys. Rev. A 54, 1862 (1996).

 \( ^{8} \)  A. M. Steane, Phys. Rev. Lett. 77, 793 (1996).

 \( ^{9} \)  D. Loss and D. P. DiVincenzo Phys. Rev. A 57, 120 (1998).

 \( ^{10} \)  G. Burkard, D. Loss, and D. P. DiVincenzo, Phys. Rev. B 59, 2070 (1999).

 \( ^{11} \)  M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, 2000).

 \( ^{12} \)  W. Zhang, N. Konstantinidis, K. Al-Hassanieh, and V. V. Dobrovitski, J. Phys.: Condens. Matter 19 083202 (2007).

 \( ^{13} \)  C. W. Gardiner, Quantum Noise (Springer, Berlin, 1991).

 \( ^{14} \)  D. F. Walls and G. J. Milburn, Quantum optics (Springer-Verlag, Berlin, 1995).

 \( ^{15} \)  H. P. Breuer, D. Burgarth, and F. Petruccione, Phys. Rev. B 70, 045323 (2004).

 \( ^{16} \)  Y. Hamdouni, M. Fannes, and F. Petruccione, Pys. Rev. B 73, 245323 (2006).

 \( ^{17} \)  Z. Huang, G. Sadiek, and S. Kais, J. Chem. Phys. 124, 144513 (2006).

 \( ^{18} \)  D. D. Bhaktavatsala Rao, V. Ravishankar, and V. Subrahmanyam, Phys. Rev. A 74, 022301 (2006).

 \( ^{19} \)  X. Z. Yuan, H. S. Goan, and K. D. Zhu, Phys. Rev. B 75, 045331 (2007).

 \( ^{20} \)  N. V. Prokof'ev and P. C. E. Stamp, Rep. Prog. Phys. 63 669 (2000).

 \( ^{21} \)  W. Zhang, V. V. Dobrovitski, K. A. Al-Hassanieh, E. Dagotto, and B. N. Harmon, Phys. Rev. B 74, 205313 (2006).

 \( ^{22} \)  A. Hutton and S. Bose, Phys. Rev. A 69, 042312 (2004).

 \( ^{23} \)  W. Zhang, V. V. Dobrovitski, L. F. Santos, L. Viola, and B. N. Harmon, cond-mat/0703453v1.

 \( ^{24} \)  H. J. Lipkin, N. Meshkov, and A. J. Glick, Nucl. Phys. 62, 188 (1965).

 \( ^{25} \)  S. Dusuel and J. Vidal, Phys. Rev. Lett. 93 237204 (2004).

 \( ^{26} \)  W. Von Waldenfels, Séminaire de probabilité (Starsburg), tome 24, p.349-356 (Springer-Verlag, Berlin, 1990).

 \( ^{27} \)  X. Wang and K. Mølmer, Eur. Phys. J. D, 18 385 (2002).

 \( ^{28} \)  M. Danos and J. Rafelski, Pocketbook of Mathematical Functions (Verlag Harri Deutsch, Frankfurt, 1984).

 \( ^{29} \)  L. Tessieri and J. Wilkie, J. Phys. A 36 12305 (2003).

 \( ^{30} \)  H. Krovi, O. Oreshkov, M. Ryazonov, and D. Lidar, e-print arXiv:0707.2096.
 
