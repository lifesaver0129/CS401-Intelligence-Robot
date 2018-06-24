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
* Update each individual cell using a binary Bayes filter: Bel(m_t^[xy])=ηp(z_t|mt^[xy])∫p(mt^[xy]|m\_(t-1)^[xy],u\_(t-1))Bel(m \_(t-1))dm_(t-1)^[xy]
* Additional assumption: Map is static: Bel(m_t^[xy])ηp(z_t|m_t[xy])Bel(m_(t-1)^[xy]) 

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
  * 

