# Finals

## Mapping

### Problem

* Sensor interpretation
  * extract relevant information 
  * integrate info over time
* Locations have to be estimated 

### Occupancy GridMap

* Robot positions are known
* Bel(mt)=P(m_t|u_1,z_2 ... ,u_t-1,z_t)=∏(x,y)Bel(m^[xy])
* Update each individual cell using a binary Bayes filter: Bel(m_t^[xy])=ηp(z_t|m_t^[xy])∫p(m_t^[xy]|m\_(t-1)^[xy],u\_(t-1))Bel(m\_(t-1))dm_(t-1)^[xy]
* Additional assumption: Map is static: Bel(m_t^[xy])ηp(z_t|m_t^[xy])Bel(m_(t-1)^[xy]) 

### Reflection Maps  

* Counting
  * hits(x,y): number of cases where a beam ended at <x,y>
  * misses(x,y): number of cases where a beam passed through <x,y> 
  * Bel(m^[xy])=hits(x, y)/(hits(x,y)+misses(x,y))
  * Value of interest: P(reflects(x,y)) 
* Measurement Model 
  * pose at time t: x_t
  * beam n of scan t: z_(t,n) 
  * maximum range reading ς_(t,n)=1
  * beam reflected by an object ς_(t,n)=0
* Maximum Likelihood Map 
  * Compute values for m that maximize m*=arg_(m)maxP(m|z1,...,zt,x1,...,xt)
  * Assuming a uniform prior probability for p(m), this is equivalent to maximizing (applic. of Bayes rule) 
  * m*=arg_(m)maxP(z1,...,zt m, x1,..., xt ) =arg\_(m)max∏P(zt|m,xt) =arg\_(m)max∑lnP(zt|m,xt) 

### Compare

* The counting model determines how often a cell reflects a beam.
* The occupancy model represents whether or not a cell is occupied by an object. 
* Out of 1000 beams only 60% are reflected from a cell and 40% intercept it without ending in it. Suppose p(occ | z) = 0.55 when a beam ends in a cell and p(occ | z) = 0.45 when a cell is intercepted by a beam that does not end in it. (0.55/0.45)^(n\*0.6)+(0.45/0.55)^(n*0.4)



## Error propagation and feature extraction 

### Error Propagation  

* First-order error propagation is fundamental for: Kalman filter (KF), landmark extraction, KF-based localization and SLAM 
  * Approximating f(X) by a first-order Taylor series expansion about the point X = μX
* Jacob Matrix
  * It’s the orientation of the tangent plane to the vector- valued function at a given point 
  * Generalizes the gradient of a scalar valued function
* Input covariance matrix CX and Jacobian matrix FX 
  * Error propagation Law Cy=FxCxFx^T 
* Monte-Carlo: Non-parametric representation of uncertainties 
  * Sampling from p(X)
  * Propagation of samples 
  * Histogramming
  * Normalization 

### Feature Extraction 

* Landmarks for: Localization, SLAM, Scene analysis 
  * Lines, corners, clusters: good for indoor
  * Circles, rocks, plants: good for outdoor 
* Properties
  * A feature/landmark is a physical object which is, static, perceptible, (at least locally) unique 
  * Abstraction from the raw data
    * type (range, image, vibration, etc.)
    * amount (sparse or dense)
    * origin (different sensors, map) 
  * +Compact, efficient, accurate, scales well, semantics, − Notgeneral 
* Can be subdivided into Segmentation and Fitting

### Split and Merge 

* Split 
  - Obtain the line passing by the two extreme points 
  - Find the most distant point to the line 
  - If distance > threshold, split and repeat with the left and right point sets 
* Merge 
  - If two consecutive segments are close/collinear enough, obtain the common line and find the most distant point 
  - If distance <= threshold, merge both segments 
* Improvements
  * Residual analysis before split 
  * Split only if the break point provides a "better interpretation" in terms of the error sum 
  * Merge non-consecutive segments as a post- processing step
* Fit Expressions 
  * Given: A set of n points in polar coordinates 
  * Wanted: Line parameters a', r



##  Extended kalman filter localization 

###  Localization Problem Statement 

* Given
  * Map of the environment.
  * Sequence of sensor measurements. 
* Wanted
  * Estimate of the robot’s position. 
* Problem classes
  * Position tracking
  * Global localization
  * Kidnapped robot problem (recovery) 

### Landmark-based Localization  

* Landmark Extraction 
  * Hessian line model: xcos(a)+ysina-r=0
* Measurement Prediction
  * coordinate frame transform world-to-sensor 
  * Given the predicted state (robot pose), predicts the location z(hat)_k and location uncertainty HC(hat)\_kH^T of expected observations in sensor coordinates zk=h(x(hat)\_k, m)
* Data association 
  * Associates predicted measurements z(hat)\_k^i with observations z(hat)\_k^i,  v_k^(ij)=z(hat)\_k^j - z\_k^i, S_k^(ij)= R\_k^i+H^(i)C(hat)\_kH^(iT)
  * Innovation, v_k^(ij),  innovation covariance S_k^(ij)
  * Matching on significance level alpha 
* Update
  * Kalman gain: Kk=C(hat)_kH^TS\_k^(-1)
  * State update: x_k=x(hat)_k+K\_k*v_k
  * State covariance update: C_k=(I-K_kH)C(hat)_k

### EKF Localization  

* Prediction, Observation Prediction, Correction, Estimation Sequence, Comparison 
* Highly efficient: Polynomial in measurement dimensionality k and state dimensionality n: O(k^2.376+n^2)
* Not optimal, Can diverge if nonlinearities are large 



## Synchronous localization and mapping 

### SLAM Problem Statement  

* SLAM is the process by which a robot builds a map of the environment and, at the same time, uses this map to compute its location, learning a map and locating the robot simultaneously 
* Localization/map: inferring location given a map/localization 
* A map is needed for localizing a robot ↔ A pose estimate is needed to build a map 
* Given
  * The robot’s controls: U_(0:k)={u\_1... u\_k}
  * Relative observations: Z_(0:k)={z\_1... z\_k}
* Wanted
  * Map of features: m={u\_1... u\_k}
  * Path of the robot: X_(0:k)={x\_1... x\_k}
* Absolute robot pose, absolute landmark positions, only relative measurements of landmarks 
* Why SLAM hard
  * Robot path and map are both unknown 
  * Errors in map and pose estimates correlated 
  * The mapping between observations and landmarks is unknown
  * Data Association: picking wrong data associations can have catastrophic consequences (divergence)
* Full SLAM: p(x_(0:t),m|z\_(1:t),u\_(1:t)), Estimates entire path and map
* Online SLAM: p(x_(t),m|z\_(1:t),u\_(1:t))= ∫∫...∫p(x\_(t),m|z\_(1:t),u\_(1:t))dx_1dx_2...dx\_(t-1), most recent pose and map 
* Building the Map: Filter Cycle 
  * State prediction (odometry)
  * Measurement prediction
  * Observation
  * Data Association 
  * Update
  * Integration of new landmarks 
* Loop Closure 
  * revisiting already mapped areas, uncertainties in robot and landmark estimates can be reduced 
  * exploited to "optimally" explore 
  * the problem of where to acquire new information 
* KF-SLAM Properties  
  * The determinant of any sub-matrix of the map covariance matrix decreases monotonically as successive observations are made
  * When initialized, its uncertainty is maximal 
  * Landmark uncertainty decreases monotonically 
  * In the limit, the landmark estimates become fully correlated, and the covariance associated with any single landmark location estimate is determined only by the initial covariance in the vehicle location estimate. 
* Complexity 
  * Cost per step: quadratic in n, the number of landmarks: O(n2) 
  * Total cost to build a map with n landmarks: O(n3)
  * Memory: O(n2) 
  * Problem: becomes computationally intractable for large maps



##  Path planning and collision avoidance

### Motion Planning  

* Goals: 
  * Collision-free trajectories
  * Robot should reach the goal location as fast as possible
*  Challenges 
  * Calculate the optimal path taking potential uncertainties in the actions into account 
  * Quickly generate actions in the case of unforeseen objects 

### Dynamic Windows Approach 

* Collision avoidance: determine collision- free trajectories using geometric operations 
* Here: robot moves on circular arcs  
* Motion commands (v,ω)  
* Steering commands are chosen by a heuristic navigation function. 
* This function tries to minimize the travel-time by “driving fast in the right direction.” 
* Navigation Function: NF=å\*vel+ßnf+γΔnf+δgoal 
  * vel: maxmizes velocity
  * n: consider cost to reach the goal
  * f: follows grid basd path computed by A*
  * goal: goal nearness
* Problem: robot does not slow down early enough to enter the doorway

###  A* Algorithm 

* g(n) = actual cost from the initial state to n. 
* h(n) = estimated cost from n to the next goal. 
* f(n) = g(n) + h(n), the estimated cost of the cheapest solution through n. 
* h is admissible if the following holds for all n : h(n) ≤ h*(n) 
* Assumptions
  * A robot is assumed to be localized.
  * Robot has to compute a path based on an occupancy grid.
  * Often the correct motion commands are executed (but no perfect map). 
* Convolution of the Grid Map 
  * Convolution blurs the map. 
  * Obstacles are assumed to be bigger than in reality. 
  * Perform an A* search in such a convolved map. 
  * Robots increases distance to obstacles and moves on a short path! 
* A* in Convolved Maps 
  * The costs are a product of path length and occupancy probability of the cells. 
  * Cells with higher probability are avoided by the robot, keeps distance to obstacles 

### 5D Planning 

* Plans in the full <x,y,θ,v,ω>-configuration space using A*, generates a sequence of steering commands to reach the goal location,  maximizes trade-off between driving time and distance to obstacles. 
* quality of the trajectory scales  
* Main Steps
  * Update (static) grid map based on sensory input. 
  * Use A* to find a trajectory in the <x,y>-space using the updated grid map. 
  * Determine a restricted 5d-configuration space based on step 2. 
  * Find a trajectory by planning in the restricted <x,y,θ,v,ω>-space. 
* Timeout Avoidance: reduce the size of the channel the 2d-path that has high cost 

### Summary 

* Robust navigation requires combined path planning & collision avoidance 
* Approaches need to consider robot's kinematic constraints and plans in the velocity space. 

