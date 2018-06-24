# Midterm

## Robot types
* Robot manipulators
  - Assembly, automation
* Field robots
  - Military, space
* Service robots
  - Cleaning, medical
* Entertainment/education robots
  Why use robots
* Dangerous, dirty, dull, difficult
* Automation, augmentation, assistance, autonomous
  Robotic system
* Mechanical structure
  - Kinematics and dynamics
* Actuators
  - Electrical, hydraulic, pneumatic, artificial muscle
* Sensors
  - Passive: optical, infrared, electro-magnetic
  - Active: laser, ultrasound, microwave
* Computation, communication and control
* User interface and power unit
* Environmental sensors ->motion planner ->controller -> mechanical structure -> configuration sensor
  Optimization for intelligent robots
* Perception
* Control
* Decision
* Planning
* Scheduling Optimization
* Finding minimizer of a function subject t- constraints
* Most of the machine learning problems are, in the end, optimization problem
* Convex
  - Unconstrained optimization
* Gradients descent
* Newton's method
* Batch learning
* Stochastic gradient descent
  - Constrained optimization
* Lagrange function
* General methods
* Non-convex
  - Heuristic algorithms, approximate methods

## Mobile robot

* Automatic machine that capable of locomotion
  Control & decision paradigms
* Mathematical model, system diagram, classical / reactive / hybrid paradigm, potential field method
* Classical / hierarchical paradigm
  - Sense->plan->act->
  - Focus on automated reasoning and knowledge representation
  - Perfect world model, close world assumption
  - Find boxes and move them t- designated position
* Reactive / behavior-based paradigm
  - Sense <-> act
  - N- models
  - Easy successes, limitations
  - Investigate biological system
  - Characteristics
* Situated
* N- memory
* Tight coupling between perception and action
* Eg- centric, only local, behavior-specific sensing
  - Behaviors
* Direct mapping of sensory input
* Emergent
* Modularity
* Hybrid deliberative / reactive 
  - Sense<->plan<->act<->
  - Closed loop, reactive control
  Field methodologies
* Treat robot as particle
* Along the derivative of the potential
* Field depends on obstacles, desired travel, directions, targets
* Summation of primitive fields
* Strength change with distance t- obstacle
  Primitive potential fields
* Uniform, perpendicular, attractive, repulsive, tangential
  Corridor with potential fields
* 0(collision avoidance): repulsive field of detected obstacles
* 1(wander): uniform field
* 2(corridor following) replaces wander fields by 3 fields
* Suffer from local minima
* Characteristics
  - N- preference layers
  - Easy t- visualize, combine different fields
  - High update rates
  - Parameter tuning
  Control design architectures
* COROS architect and dev framework
* Control and decision architecture
* Software architecture 

## Turtle-bot specification

* Base, motor, motor encoder, gyroscope, accelerometer, magnetometer
  Rotary encoder based odometry
* Use of data from motion sensors t- estimate change in position
  Manipulator- vs. Mobile Robot Kinematics
* Both are with forward and inverse kinematics
* However, for mobile robots, encoder values don‘t map t- unique robot poses
* However, mobile robots can move unbound with respect t- their environment
  - There is n- direct (=instantaneous) way t- measure the robot’s position
  - Position must be integrated over time, depends on path taken
  - Leads t- inaccuracies of the position (motion) estimate
* Understanding mobile robot motion starts with understanding wheel constraints placed on the robot’s mobility
  Non-holonomic systems
* differential equations are not integrable
* the measure of the traveled distance of each wheel is not sufficient t- calculate the final position of the robot
* This is in stark contrast t- actuator arms
  Locomotion of wheeled robots
* Power of motion form place t- place
* Differential drive
* Car drive
* Synchronous drive
* Mecanum wheels
  Wheeled Mobile Robots
* Bi-wheel type robot
  - Smooth motion
  - Risk of slipping
  - Some times use roller-ball t- make balance
* Caterpillar type robot
  - Exact straight motion
  - Robust t- slipping
  - Inexact modeling of turning
* Omnidirectional robot
  - Free motion
  - Complex structure
  - Weakness of the frame
  Instantaneous center of rotation(ICR) and instantaneous center of curvature(ICC)
* Mobility: degree of freedom of the robot motion
* Steerability number of centered orientable wheels that can be steered independently in order t- steer the robot
  Non-Holonomic Constraints 
* limit the possible incremental movements within the configuration space of the robot
* Robots with differential drive or Ackerman drive synchronous drive move on a circular trajectory and cannot move sideways
  Mobile robot motion control
* The objective of a kinematic controller is t- follow a trajectory described by its position and/or velocity profiles as function of time.
* Motion control is not straight forward because mobile robots are typically non- holonomic and MIM- systems.
* Most controllers (including the one presented here) are not considering the dynamics of the system
* Open loop control, feedback control, kinematic position control, coordinates transformation
* Control law
  - the direction of movement is kept positive or negative during movement
  - parking maneuver is performed always in the most natural way and without ever inverting its motion.

## Perception for mobile robots

* Raw data->(navigation)->features->(interaction)->objects->(servicing/reasoning)->places/situations
  Sensors for Mobile Robots 
* Contact sensors: Bumpers
* Internal sensors 
  - Motor encoder
  - Accelerometers (spring-mounted masses)
  - Gyroscopes (spinning mass, laser light)
  - Compasses, inclinometers (earth magnetic field, gravity)
* Proximity sensors
  - Ultrasonic Range Sensor (time of flight)
  - Laser range-finders (triangulation, tof, phase)
  - Structured light
  - Infrared (intensity)
* Visual sensors: Cameras
* Satellite-based sensors: GPS
  Wheel / Motor Encoders
* electro-mechanical device that converts linear or angular position of a shaft t- an analog or digital signal, making it an linear/angular transducer
* Applications:
  - measure position or speed of the wheels or steering
  - integrate wheel movements t- get an estimate of the position -> odometry 
  - optical encoders are proprioceptive sensors
* Mechanisms:
  - regular: counts the number of transitions but cannot tell the direction of motion
  - quadrature: uses tw- sensors in quadrature-phase shift. The ordering of which wave produces a rising edge first tells the direction of motion. Additionally, resolution is 4 times higher
  Mechanical accelerometer
* Mass, suspension mechanism, sensing element
* Measure all external forces acting upon item: gravity
* Acts like spring mass damper system
  Gyroscope
* Provide an absolute measure for the heading of a mobile system 
* Preserve the orientation in relation t- a fixed reference frame.
* Classification:
  - Mechanical Gyroscopes: Standard gyr- (angle) and rate gyr- (speed) 
  - Optical Gyroscopes: Rate gyr- (speed)
  Compress
* Magnetic field on earth
* absolute measure for orientation
* Classification:
  - mechanical magnetic compass
  - direct measure of the magnetic field (Hall-effect, magneto-resistive sensors)
  - Gyrocompass (non-magnetic, finds true north by using fast-spinning wheel and friction forces in order t- exploit the rotation of the Earth) -> used on ships

## Probabilistic robotics

* Explicit representation of uncertainty
  - Perception = state estimation
  - Action = utility optimization
  Actions
* Often the world is dynamic since 
  - actions carried out by the robot,
  - actions carried out by other agents,
  - just the time passing by change of the world
  Typical action
* turns wheels t- move
* uses its manipulator t- grasp an object
* Actions are never carried out with absolute certainty
* actions generally increase the uncertainty
  Modeling actions
* P(x|u,x’)
  - This term specifies the pdf that executing u changes the state from x’ t- x.
  Bayes Filters
* Given
  - Stream of observations z and action data u: dt{u1,z1, ...,ut,zt}
  - Sensor model P(z|x)
  - Action model P(x|u,x’)
  - Prior probability of the system state P(x)
* Wanted:
  - Estimate of the state X of a dynamical system  
  - The posterior of the state is als- called Belief: Bel(xt)=P(xt |u1,z1,...,ut,zt)

## Probabilistic motion models

* The term p(x j x’, u) specifies a posterior probability, that action u carries the robot from x’ t- x.
  Coordinate system
* Three-dimensional Cartesian coordinates plus three Euler angles pitch, roll, and tilt.
  Typical Motion Models
* Odometry-based: when systems are equipped with wheel encoders
* Velocity-based (dead reckoning): n- wheel encoders are given.
  - Dead reckoning: Mathematical procedure for determining the present location of a vehicle. Achieved by calculating the current pose of the vehicle based on its velocities and the time elapsed.
* They calculate the new pose based on the velocities and the time elapsed.

## Proximity sensors

* The central task is t- determine P(z|x), i.e., the probability of a measurement z given that the robot is at position x.
  Beam-based sensors
* Scan z consists of K measurements: z = {z1 , z2 ,..., zK }
* Individual measurements are independent given the robot position P(z|x,m)=(k=1)P(zk |x,m)
  Typical Errors of Range Measurements
* Beams reflected by obstacles
* Beams reflected by persons / caused by crosstalk
* Random measurements
* Maximum range measurements
  Proximity Measurement
* Measurement can be caused by …
  - a known obstacle.
  - cross-talk.
  - an unexpected obstacle (people, furniture, ...).  
  - missing all obstacles (total reflection, glass, ...).
* Noise is due t- uncertainty ...
  - in measuring distance t- known obstacle
  - in position of known obstacles.
  - in position of additional obstacles.
  - whether obstacle is missed.
  Summary of Beam-Based Model
* Shortcomings
  - Not smooth for small obstacles and at edges
  - Not very efficient
* Assumes independence between beams. 
  - Justification? Overconfident!
* Models physical causes for measurements
  - Mixture of densities for these causes.
  - Assumes independence between causes. Problem?
* Implementation
  - Learn parameters based on real data.
  - Different models should be learned for different angles at which the sensor beam hits the obstacle.
  - Determine expected distances by ray-tracing.
  - Expected distances can be pre-processed.
  Scan-based model
* a Gaussian distribution with mean at distance to
  closest obstacle,
* a uniform distribution for random
  measurements, and
* a small uniform distribution for max range measurements.
* Highly efficient, uses 2D tables only.
* Smooth w.r.t. t- small changes in robot
  position.
* Allows gradient descent, scan matching.
* Ignores physical properties of beams.
  Landmarks
* Active beacons (e.g., radio, GPS)
* Passive (e.g., visual, retro-reflective)
* Standard approach is triangulation
* Sensor provides
  - distance, bearing, distance and bearing.
  Sensor Models
* Explicitly modeling uncertainty in sensing is key t- robustness.
* In many cases, good models can be found by the following approach:
  - Determine parametric model of noise free measurement.
  - Analyze sources of noise.
  - Add adequate noise t- parameters (eventually mix in densities for noise).
  - Learn (and verify) parameters by fitting model t- data.
  - Likelihood of measurement is given by “probabilistically comparing” the actual with the expected measurement.

## Kalman filters

* Estimates the state x of a discrete-time controlled process that is governed by the linear stochastic difference equation
* Xt=AtXt-1+Btut+et with the measurement zt=Ctxt+ht
  - At: Matrix (nxn) that describes how the state evolves from t t- t-1 without controls or noise.
  - Bt: Matrix (nxl) that describes how the control ut changes the state from t t- t-1.
  - Ct: Matrix (kxn) that describes how t- map the state xt t- an observation zt.
  - Et, ht: Random variables representing the process and measurement noise that are assumed t- be independent and normally distributed with covariance Qt and Rt respectively.

## Sample based localization problem motivation

* Discrete filter
  - Discretize the continuous state space
  - High memory complexity
  - Fixed resolution (does not adapt t- the belief)
* Particle filters are a way t- efficiently represent non-Gaussian distribution
* Basic principle
  - Set of state hypotheses (“particles”)
  -  Survival-of-the-fittest
  Function approximation
* The more particles fall int- an interval, the higher the probability of that interval
  Rejection sampling
* Sample x from a uniform distribution
* Sample c from [0,1]
* if f(x) > c keep the sample; otherwise reject the sample
  Importance sampling principle
* use a different distribution g t- generate samples from f
* By introducing an importance weight w, we can account for the “differences between g and f ”
* w = f/g
* f: target; g: proposal
* Pre-condition: f(x)>=0 g(x)>0
  Particle Filter Algorithm
* Sample the next generation for particles using the proposal distribution
* Compute the importance weights:
  - weight = target distribution / proposal distribution
* Resampling: “Replace unlikely samples by more likely ones”

