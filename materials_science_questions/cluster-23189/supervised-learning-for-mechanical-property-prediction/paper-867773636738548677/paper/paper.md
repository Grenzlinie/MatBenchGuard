# NPLIC: A Machine Learning Approach to Piecewise Linear Interface Construction

Mohammadmehdi Ataei$^{a,b}$, Markus Bussmann$^{b,*}$, Vahid Shaayegan$^{b}$, Franco Costa$^{c}$, Sejin Han$^{d}$, Chul B. Park$^{b}$

$^{a}$Vector Institute, 661 University Ave Suite 710, Toronto, ON M5G 1M1, Canada
$^{b}$Department of Mechanical Engineering, University of Toronto, 5 King's College Rd, Toronto, ON M5S 3G8, Canada
$^{c}$Autodesk, Inc., 259-261 Colchester Rd., Kilsyth, VIC. 3137, Australia
$^{d}$Autodesk, Inc. 2353 North Triphammer Rd., Ithaca, NY 14850, USA

---

## Abstract
Volume of fluid (VOF) methods are extensively used to track fluid interfaces in numerical simulations, and many VOF algorithms require that the interface be reconstructed geometrically. For this purpose, the Piecewise Linear Interface Construction (PLIC) technique is most frequently used, which for reasons of geometric complexity can be slow and difficult to implement. Here, we propose an alternative neural network based method called NPLIC to perform PLIC calculations. The model is trained on a large synthetic dataset of PLIC solutions for square, cubic, triangular, and tetrahedral meshes. We show that this data-driven approach results in accurate calculations at a fraction of the usual computational cost, and a single neural network system can be used for interface reconstruction of different mesh types.

**Keywords:** Machine Learning, Neural Networks, PLIC, Piecewise Linear Interface Construction, Volume Of Fluid, VOF, Computational Fluid Dynamics

---

## 1. Introduction
In the numerical simulation of multiphase flows, the volume of fluid (VOF) method is widely used to track fluid interfaces through a computational domain (e.g. [1–7]). In this method, a scalar field $\alpha$ denotes the volume fraction of one fluid within each cell. In the case of a liquid-gas system, for example, $\alpha=1$ in liquid cells, $\alpha=0$ in gas cells, and $0<\alpha<1$ in interface cells.

Reconstruction of the interface geometry from the $\alpha$ field is an important step for calculating volume fluxes advected across cell boundaries [8], and related

---

*Corresponding author

Preprint submitted to Computers & Fluids
January 26, 2021

calculations such as finding the distance between two interfaces [9]. Since the pioneering work of Youngs [10], Piecewise Linear Interface Construction (PLIC) has been widely employed to geometrically reconstruct interfaces in VOF sim- ulations.

Given a known interface normal $\vec{n}$ and the volume fraction $\alpha_0$ of an in- terface cell, PLIC calculates the constant $C$ of the plane $\vec{n} \cdot \vec{x} + C = 0$ ($\vec{x} \in R^2$ in 2D or $R^3$ in 3D) that splits the cell into two parts, with volume fractions $\alpha_0$ and $1 - \alpha_0$ (see Fig. 1). The reconstructed interface is the polygon resulting from the plane's intersection with the cell.

![](./images/867773636738548677_1.jpg)

Figure 1: A plane representing the interface splits the cell into two parts, with volume fractions $\alpha_0$ and $1 - \alpha_0$.

Especially in 3D, finding $C$ involves complex geometrical operations that can be slow to compute. In some algorithms, $C$ is found iteratively [11, 12], until the target volume fractions $\alpha_0$ and $1 - \alpha_0$ are achieved within a given tolerance. For simpler geometries such as triangular or rectangular meshes, analytical solutions have been developed that reduce the computational cost [13, 14], although these approaches may also include a slow iterative step used to select one from a set of several governing equations.

Machine learning algorithms are increasingly being applied in computational science [15] and Computational Fluid Dynamics (CFD) simulations in various ways; for example, flow approximation [16-18], shape optimization for fluid flow processes [19], cardiovascular flow modeling [20], shock detection [21], computing interface curvature [22, 23], and for turbulence modeling [24-26]. In this work, we will demonstrate a machine learning approach to find $C$, by using artificial neural networks to relate $C$, $\alpha_0$, and $\vec{n}$ for different cell geometries. It will be shown that neural networks can outperform standard PLIC algorithms, while being nearly as accurate. We will also show that a single neural network system can find the PLIC solution for different mesh types. We limit the results of this paper to square, cubic, triangular, and tetrahedral mesh structures, although the same methodology could be extended to other mesh types.

2

## 2. Methodology

Artificial neural networks can be thought of as universal approximators capable of extracting nonlinear relationships between different parameters through a kind of machine perception [27]. Fig. 2 shows a multilayer perceptron (MLP) "fully-connected" neural network that consists of an interconnected network of so-called artificial neurons, comprised of an input layer, a series of fully-connected hidden layers, and an output layer. Each neuron is made up of a set of inputs, weights, and a bias. The bias is added to the combined sum of input-weight products, and the result passes though an activation unit, which is usually a sigmoid or ReLU function.

Initially, the network weights and biases are ignorant of the inputs and outputs. The goal is to find a combination of weights and biases that best map the appropriate inputs to the correct PLIC solution. To this reason, the network is fed a synthetic dataset of PLIC solutions, and the weights and biases are updated iteratively by using the gradient of the following loss function:

$$
L(C, \bar{C}) = \sum_{batch} (C - \bar{C})^2 \tag{1}
$$

which is the squared sum of the difference between each predicted value $C$ and the actual value $\bar{C}$, summed over the training batch. As shown in Fig. 2, the training is continued until the validation loss is less than a given tolerance, or a specified maximum number of epochs is reached.

![](./images/867773636738548677_2.jpg)

Figure 2: Neural network architecture.

Initially, we use four separate fully-connected neural networks to find the PLIC constants $C$ for square, cubic, triangular, and tetrahedral meshes. The output layer of each of these networks is a single neuron outputting a constant $C$; the inputs differ depending on the mesh structure. Later on, we will use a single neural network for PLIC calculation of different mesh types.

For square and cubic meshes, the geometries are constant, and so $C$ can be defined as only a function of the interface cell normal $\vec{n}$ and volume fraction $\alpha_0$. As such, for square and cubic meshes the input layers are $(\alpha_0, \theta)$ and $(\alpha_0, \phi, \theta)$ respectively, where $\vec{n} = [cos\ \theta, sin\ \theta]$ in 2D, and $\vec{n} = [sin\ \theta cos\ \phi, sin\ \theta sin\ \phi, cos\ \theta]$ in 3D, in spherical/polar coordinate systems with axes aligned with the cell sides. In VOF models, the interface normal $\vec{n}$ is often obtained from the gradient of the volume fraction field or a smoothed representation of it (e.g., $\vec{n} = \nabla\alpha/|\alpha|$) [28].

As shown in Fig. 3, the geometry of an arbitrarily-shaped tetrahedral mesh cell can be expressed by coinciding one of the vertices $P_1$ with the origin, $P_2$ with the axis $x$, and one of the faces with the $x-y$ plane that contains $P_1$, $P_2$, and $P_3$. This tetrahedron can be transformed into a unit tetrahedron in the coordinate system $\vec{\delta}$ using the following transformation $\mathbf{Q}$:

$$
\underbrace{\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}}_{\vec{x}} = \underbrace{\begin{pmatrix}
x_2 & x_3 & x_4 \\
0 & y_3 & y_4 \\
0 & z_3 & z_4
\end{pmatrix}}_{\mathbf{Q}} \underbrace{\begin{pmatrix}
\gamma \\
\beta \\
\zeta
\end{pmatrix}}_{\vec{\delta}} \tag{2}
$$

The transformation $\mathbf{Q}$ reduces the number of parameters for the PLIC calculation to $\phi$, $\theta$, and $\alpha_0$. While $\mathbf{Q}$ preserves $\alpha_0$, the unit normal undergoes a nonlinear transformation so $\phi$ and $\theta$ must be recalculated under the transformation $\mathbf{Q}$ [29].

![](./images/867773636738548677_3.jpg)

Figure 3: Normalizing a tetrahedral cell.

Similarly, as shown in Fig. 4, an arbitrarily-shaped triangular cell can be transformed into a unit triangle under $\mathbf{Q}$:

$$
\underbrace{\begin{pmatrix} x \\ y \end{pmatrix}}_{\vec{x}} = \underbrace{\begin{pmatrix} x_2 & x_3 \\ 0 & y_3 \end{pmatrix}}_{\mathbf{Q}} \underbrace{\begin{pmatrix} \gamma \\ \beta \end{pmatrix}}_{\vec{\delta}} \tag{3}
$$

![](./images/867773636738548677_4.jpg)

Figure 4: Normalizing a triangular cell.

In this case, the input layer of the network is $\theta$ and $\alpha_0$.

The fact that the inputs to the neural network for triangular and square meshes in 2D, and the inputs for tetrahedral and cubic meshes in 3D are iden- tical, also allows us to use a single neural network to calculate a PLIC solution for triangular and square meshes, and similarly use another neural network for tetrahedral and cubic mesh types. An input parameter $m$ is introduced to dis- tinguish between the mesh types for the neural networks, which takes the value of 1 for triangular/tetrahedral cell types and zero for square/cubic mesh types.

In summary, the input parameters for the neural networks depending on the mesh type are given in Table 1:

<table>
  <thead>
    <tr>
      <th>Mesh type</th>
      <th>Parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Square</td>
      <td>$\theta$, $\alpha_0$</td>
    </tr>
    <tr>
      <td>Triangular</td>
      <td>$\theta$, $\alpha_0$</td>
    </tr>
    <tr>
      <td>Cubic</td>
      <td>$\phi$, $\theta$, $\alpha_0$</td>
    </tr>
    <tr>
      <td>Tetrahedral</td>
      <td>$\phi$, $\theta$, $\alpha_0$</td>
    </tr>
    <tr>
      <td>Triangular and square (T-S)</td>
      <td>$\theta$, $\alpha_0$, $m$</td>
    </tr>
    <tr>
      <td>Tetrahedral and cubic (T-C)</td>
      <td>$\phi$, $\theta$, $\alpha_0$, $m$</td>
    </tr>
  </tbody>
</table>

Table 1: Inputs of the neural network for different mesh types.

We generated synthetic PLIC datasets for each mesh type by computing the

PLIC solution (i.e., the constant $C$) for a large number of input parameters.
The following equations were used to discretely approximate the boundary of a
unit sphere to create sets of normal orientations $S_{\vec{n}}$ and volume fractions $S_{\alpha_{0}}$
(adapted from [29, 30]:

$$
\begin{aligned}
S_{\vec{n}}(N_{\vec{n}})=&\left\{[cos\phi\ sin\theta, sin\phi\ sin\theta, cos\theta]:(\phi, \theta) \in\right. \\
&\left.\frac{\pi}{2 N_{\vec{n}}}[1,2, \ldots, 2 N_{\vec{n}}] \times \frac{\pi}{N_{\vec{n}}}[0,1, \ldots, N_{\vec{n}}]\right\},
\end{aligned}
\tag{4}
$$

$$
\begin{gathered}
S_{\alpha}(N_{\alpha})=\left\{10^{-k}: 5 \leq k \leq 9\right\} \cup \\
\left\{10^{-4}+\frac{m-1}{N_{\alpha}-1}\left(1-2 \cdot 10^{-4}\right): 1 \leq m \leq N_{\alpha}\right\} \cup \\
\left\{1-10^{-k}: 5 \leq k \leq 9\right\}
\end{gathered}
\tag{5}
$$

Eq. 5 ensures that $\alpha_{0}$ is sufficiently sampled near 0 and 1. In 2D, Eq. 4 becomes:

$$
S_{\vec{n}}(N_{\vec{n}})=\left\{[cos\theta, sin\theta]:(\theta) \in \frac{\pi}{N_{\vec{n}}}[0,1, \ldots, N_{\vec{n}}]\right\}
\tag{6}
$$

We set $N_{\alpha}=20$ and $N_{\vec{n}}=40$ in 3D, which results in $2 N_{\vec{n}}(N_{\vec{n}}+1)(N_{\alpha}+10)=$
98400 input parameters, and $N_{\alpha}=100$ and $N_{\vec{n}}=100$ in 2D, that gives us
$N_{\vec{n}}(N_{\alpha}+10)=11000$ input parameters.

Each dataset was randomly split into three parts: 70% for training, 20% for
testing, and 10% for validation. Each model was initially trained on the training
dataset; during training, the validation dataset was used to prevent over-fitting;
and the test dataset was used to evaluate the predictive performance of the final
trained model.

The neural network models were developed and trained using the Pytorch
[31] deep learning library. Computations were carried out on an NVIDIA 1080
Ti Graphics Card with 11GB GDDR5X frame buffer, using a PC running Linux
Ubuntu 20.04 with Intel Core™ i7-8700K Coffee Lake Processor (6 Cores, up to
4.7 GHz) and 32GB of DDR4 RAM.

In this work, we use a deep neural network with one hidden layer containing
$N$ neurons, and ReLU as the activation function [32], except for the output
layer which is a linear function to allow for negative outputs. Each neural
network was trained until the validation loss was less than $\epsilon=5 \times 10^{-5}$, up to
a maximum of $10^{5}$ epochs with a batch size of 8192, using $N=24$ or $N=48$
in the hidden layer. For training, the Adam optimization algorithm [33] was
used with a learning rate of $10^{-4}$. The training of each network took 10-20
minutes. The results presented in this work are the average of three runs with
three different random seeds for the initialization of the networks.

The training performance was evaluated using the Mean Squared Error
(MSE). Fig. 5 shows MSE of the training dataset after each epoch for a neural

network with $N=24$ trained on the cubic mesh dataset.

The neural network models for computing PLIC calculations are hereafter referred to as NPLIC.

![](./images/867773636738548677_5.jpg)

Figure 5: Mean Squared Error (MSE) vs epoch for a neural network with $N=24$ trained on the cubic mesh dataset.

## 3. Results and Discussion

### 3.1. Predictive Performance

The test datasets were used to evaluate the predictive capability of each trained model. In Fig. 6, the value of $C$ computed by NPLIC is plotted against $\bar{C}$ from the test dataset. For a perfect fit, all the points would lie on the diagonal. It can be observed that the values of $C$ predicted by NPLIC are in very good agreement with the test results for all the mesh types. The final MSE and MAE (Mean Absolute Error) for each trained model (over the test dataset) are shown in Figs. 7 and 8 for the neural networks that were trained up to $10^5$ epochs. The models with $N=48$ have errors close to $0.1\%$, which implies that NPLIC can be used in place of PLIC algorithms with little to no effect on accuracy. In general, the errors are comparable to other PLIC approximation techniques (e.g. [34]). With increasing mesh complexity, predictably the accuracy of NPLIC decreases, and by increasing the number of neurons the accuracy increases.


![](./images/867773636738548677_6.jpg)

Figure 6: Plots of the NPLIC predictions vs the test data for each mesh. On each plot, only a hundred data points (selected randomly) are plotted to avoid clutter.

![](./images/867773636738548677_7.jpg)

![](./images/867773636738548677_8.jpg)

### 3.2. Speedup

Figs. 9 and 10 show a comparison of NPLIC speedups versus a number of popular PLIC models. To calculate the speedups, the PLIC algorithms were implemented in C++, and compiled using optimization flag -O3 using the GCC compiler v 9.3. Since a neural network can leverage performing calculations on batches of inputs (rather than each cell one by one), we compared the speedups by performing the calculations on different numbers of meshes from $10^3$ to $10^7$. The PLIC models were executed on one CPU core. The NPLIC models were executed on both one CPU core and on the GPU. Since the implementation of PLIC models on the GPU is not trivial, we used the performance of PLIC on the CPU as the basis of our comparisons.

The wall-time of the PLIC algorithms were measured by the `std::chrono` library, and the wall-time of NPLIC on the CPU and GPU (ignoring GPU warm-up time) were measured by Pytorch's Profiler. For the profiling tasks, we used the more accurate neural networks with $N=48$.

For square and cubic meshes, we compared NPLIC with the analytical PLIC model of Scardovelli and Zaleski [13], which is faster than iterative methods for rectangular meshes. For triangular and tetrahedral meshes, we compared NPLIC with the efficient analytical model of López et al. [35].

In comparison to the PLIC models, NPLIC is up to 100 times faster when executed on a GPU, and it can be more than 8 times faster on one CPU core. It can be seen that the speedup gains are more significant on the more complex 3D meshes and triangular meshes. However, on the square mesh, the analytical implementation of PLIC is sufficiently simple that it cannot be outperformed by NPLIC.

To explain the NPLIC speedup gains, we compared the floating point operations (FLOPs) of NPLIC versus López et al. [35] for performing the calculations on 1 million tetrahedral cells. For the C++ implementation of the PLIC model, the number of FLOPs was estimated by the Intel's Software Development Emulator (Intel SDE) tool. The Thop library was used to calculate the number of FLOPs for the NPLIC model. We found that while the PLIC model requires fewer floating operations than the NPLIC (1.98 GFLOPs vs 9.6 GFLOPs), on the CPU the NPLIC algorithm operates at higher GFLOPs per second than PLIC (72 GFLOPs per second vs 2.42 GFLOPs per second), and the performance increases further to 1.21 TFLOPs per second on the GPU. This is because NPLIC makes better use of hardware (on both the CPU and GPU), because the essence of neural network operations consists only of simple matrix multiplications, and because deep learning libraries such as Pytorch are heavily optimized to leverage the available hardware.

![](./images/867773636738548677_9.jpg)

Figure 9: Performance speedups of NPLIC for each 2D mesh type, in comparison to the methods of Scardovelli et al. [13] (square mesh, analytical) and López et al. [35] (triangular mesh, analytical).

![](./images/867773636738548677_10.jpg)

Figure 10: Performance speedups of NPLIC for each 3D mesh type, in comparison to the methods of Scardovelli et al. [13] (cubic mesh, analytical) and López et al. [35] (tetrahedral mesh, analytical).

11

### 3.3. Reconstructing a VOF Scalar Field

Fig. 11 shows a 2D VOF scalar field for a circular bubble in a liquid. The gas and liquid phases correspond to $\alpha=0$ and $\alpha=1$, and the interface cells $0<\alpha<1$. A coarse $8\times8$ grid is chosen so that we can easily illustrate the reconstruction results. In Fig. 12, the interface cells are reconstructed by the Scardovelli analytical PLIC and NPLIC models. The zoomed-in plot shows that the results of NPLIC and PLIC overlap as expected.

![](./images/867773636738548677_11.jpg)

Figure 11: The $\alpha$ scalar field representing a circular bubble on an 8 by 8 grid.

![](./images/867773636738548677_12.jpg)

Figure 12: NPLIC and PLIC reconstructions in the bubble interface cells.

### 3.4. Implementation in a CFD Solver

Finally, Basilisk (https://basilisk.fr) [36] is an open-source CFD solver for adaptive Cartesian meshes. Basilisk uses PLIC VOF to solve the advection equation for the volume fraction field [8, 36], by reconstructing interfaces using PLIC, and calculating volume fluxes geometrically.

NPLIC can be easily integrated into an existing codebase. The trained neural networks can be called as subroutines from other programs (e.g. using Pytorch's TorchScript for C++ implementations). We replaced the PLIC algorithm in Basilisk with NPLIC, and ran a 2D simulation of a droplet impacting a pool of liquid. As shown in Fig. 13, the NPLIC results are indistinguishable from the PLIC ones at all timesteps. In this case, NPLIC performed the interface reconstructions about five times faster.

![](./images/867773636738548677_13.jpg)

Figure 13: NPLIC performs as well as PLIC when implemented in a multiphase flow solver.

### 4. Conclusions

We have presented a machine learning approach to perform Piecewise Linear Interface Construction (PLIC) on square, cubic, and arbitrarily-shaped triangular and tetrahedral meshes. Each mesh type was normalized to reduce the number of inputs to the neural network. Fully-connected deep neural networks were trained on synthetic datasets for each mesh type. We have shown that the neural networks are capable of performing up to 100 times faster than available PLIC algorithms with minimal loss of accuracy.

### Acknowledgements

We thank the Natural Sciences and Engineering Research Council of Canada (NSERC) and Autodesk Inc. for their financial support.

### References

[1] E. Aulisa, S. Manservisi, R. Scardovelli, S. Zaleski, A geometrical area-preserving volume-of-fluid advection method, Journal of Computational Physics 192 (1) (2003) 355–364.

[2] D. Gueyffier, J. Li, A. Nadim, R. Scardovelli, S. Zaleski, Volume-of-fluid interface tracking with smoothed surface stress methods for three-dimensional flows, Journal of Computational Physics 152 (2) (1999) 423–456.

[3] G. Agbaglah, S. Delaux, D. Fuster, J. Hoepffner, C. Josserand, S. Popinet, P. Ray, R. Scardovelli, S. Zaleski, Parallel simulation of multiphase flows using octree adaptivity and the volume-of-fluid method, Comptes Rendus Mécanique 339 (2) (2011) 194–207.

[4] M. Huang, L. Wu, B. Chen, A piecewise linear interface-capturing volume-of-fluid method based on unstructured grids, Numerical Heat Transfer, Part B: Fundamentals 61 (5) (2012) 412–437.

[5] S. W. Welch, J. Wilson, A volume of fluid based method for fluid flows with phase change, Journal of Computational Physics 160 (2) (2000) 662–682.

[6] K. Kleefsman, G. Fekken, A. Veldman, B. Iwanowski, B. Buchner, A volume-of-fluid based simulation method for wave impact problems, Journal of Computational Physics 206 (1) (2005) 363–393.

[7] M. Renardy, Y. Renardy, J. Li, Numerical simulation of moving contact line problems using a volume-of-fluid method, Journal of Computational Physics 171 (1) (2001) 243–263.

[8] R. Scardovelli, S. Zaleski, Direct numerical simulation of free-surface and interfacial flow, Annual Review of Fluid Mechanics 31 (1) (1999) 567–603.

[9] M. Ataei, V. Shaayegan, F. Costa, S. Han, C. B. Park, M. Bussmann, Lbfoam: An open-source software package for the simulation of foaming using the lattice boltzmann method, Computer Physics Communications 259 (2021) 107698. doi:https://doi.org/10.1016/j.cpc.2020.107698.

[10] D. L. Youngs, Time-dependent multi-material flow with large fluid distortion, Numerical Methods in Fluid Dynamics (1982) 273–486.

[11] M. Skarysz, A. Garmory, M. Dianat, An iterative interface reconstruction method for PLIC in general convex grids as part of a coupled level set volume of fluid solver, Journal of Computational Physics 368 (2018) 254–276.

[12] W. J. Rider, D. B. Kothe, Reconstructing volume tracking, Journal of Computational Physics 141 (2) (1998) 112–152.

[13] R. Scardovelli, S. Zaleski, Analytical relations connecting linear interfaces and volume fractions in rectangular grids, Journal of Computational Physics 164 (1) (2000) 228-237.

[14] X. Yang, A. J. James, Analytic relations for reconstructing piecewise linear interfaces in triangular and tetrahedral grids, Journal of Computational Physics 214 (1) (2006) 41-54.

[15] A. Oishi, G. Yagawa, Computational mechanics enhanced by deep learning, Computer Methods in Applied Mechanics and Engineering 327 (2017) 327-351.

[16] X. Guo, W. Li, F. Iorio, Convolutional neural networks for steady flow approximation, Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (2016) 481-490.

[17] F. L. Peña, V. D. Casás, A. Gosset, R. Duro, A surrogate method based on the enhancement of low fidelity computational fluid dynamics approximations by artificial neural networks, Computers & Fluids 58 (2012) 112 - 119.

[18] R. Swischuk, L. Mainini, B. Peherstorfer, K. Willcox, Projection-based model reduction: Formulations for physics-based machine learning, Computers & Fluids 179 (2019) 704 - 717.

[19] K. Hirschen, M. Schäfer, Bayesian regularization neural networks for optimizing fluid flow processes, Computer Methods in Applied Mechanics and Engineering 195 (7) (2006) 481-500.

[20] G. Kissas, Y. Yang, E. Hwuang, W. R. Witschey, J. A. Detre, P. Perdikaris, Machine learning in cardiovascular flows modeling: Predicting arterial blood pressure from non-invasive 4D flow MRI data using physics-informed neural networks, Computer Methods in Applied Mechanics and Engineering 358 (2020) 112623.

[21] Y. Liu, Y. Lu, Y. Wang, D. Sun, L. Deng, F. Wang, Y. Lei, A CNN-based shock detection method in flow visualization, Computers & Fluids 184 (2019) 1-9.

[22] Y. Qi, J. Lu, R. Scardovelli, S. Zaleski, G. Tryggvason, Computing curvature for volume of fluid methods using machine learning, Journal of Computational Physics 377 (2019) 155-161.

[23] H. Patel, A. Panda, J. Kuipers, E. Peters, Computing interface curvature from volume fractions: A machine learning approach, Computers & Fluids 193 (2019) 104263.

[24] J. Ling, A. Kurzawski, J. Templeton, Reynolds averaged turbulence modelling using deep neural networks with embedded invariance, Journal of Fluid Mechanics 807 (2016) 155-166.

15

[25] F. Sarghini, G. de Felice, S. Santini, Neural networks based subgrid scale modeling in large eddy simulations, Computers & Fluids 32 (1) (2003) 97-108.

[26] Z. Zhou, G. He, S. Wang, G. Jin, Subgrid-scale model for large-eddy simu- lation of isotropic turbulent flows using an artificial neural network, Com- puters & Fluids 195 (2019) 104319.

[27] M.-C. Popescu, V. E. Balas, L. Perescu-Popescu, N. Mastorakis, Multilayer perceptron and neural networks, WSEAS Transactions on Circuits and Systems 8 (7) (2009) 579-588.

[28] D. B. Kothe, R. C. Mjolsness, RIPPLE - a new model for incompressible flows with free surfaces, AIAA Journal 30 (11) (1992) 2694-2700.

[29] J. Kromer, D. Bothe, Face-based Volume-of-Fluid interface positioning in arbitrary polyhedra (2021).

[30] T. Maric, Iterative Volume-of-Fluid interface positioning in general poly- hedrons with Consecutive Cubic Spline interpolation (2020).

[31] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga, A. Desmaison, A. Kopf, E. Yang, Z. DeVito, M. Raison, A. Tejani, S. Chilamkurthy, B. Steiner, L. Fang, J. Bai, S. Chintala, Pytorch: An imperative style, high- performance deep learning library, in: Advances in Neural Information Processing Systems, Vol. 32, Curran Associates, Inc., 2019, pp. 8026-8037.

[32] B. Hanin, Universal function approximation by deep neural nets with bounded width and ReLU activations, Mathematics 7 (10) (2019) 992.

[33] D. P. Kingma, J. Ba, Adam: A Method for Stochastic Optimization, arXiv e-prints (2014) arXiv:1412.6980.

[34] A. Kawano, A simple volume-of-fluid reconstruction method for three- dimensional two-phase flows, Computers & Fluids 134-135 (2016) 130-145.

[35] J. López, J. Hernández, P. Gómez, F. Faura, VOFTools - A software pack- age of calculation tools for volume of fluid methods using general convex grids, Computer Physics Communications 223 (2018) 45-54.

[36] S. Popinet, An accurate adaptive solver for surface-tension-driven interfa- cial flows, Journal of Computational Physics 228 (16) (2009) 5838-5866.