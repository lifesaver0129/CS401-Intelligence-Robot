motionModel = robotics.OdometryMotionModel;

previousPoses =  [0 0 0];
currentOdom=  [0 -1.5 0];
predPoses = motionModel(previousPoses, currentOdom);
currentOdom = currentOdom + [0 -0.1 0];
motionModel.Noise =[0 0.00004 0.0000004 0];
showNoiseDistribution(motionModel, 'OdometryPoseChange',currentOdom,  'NumSamples',1);
hold on;
currentOdom=  [1.5 0 0];
predPoses = motionModel(previousPoses, currentOdom);
currentOdom = currentOdom + [0 -0.1 0];
motionModel.Noise =[0 0.004 0.1 0];
showNoiseDistribution(motionModel, 'OdometryPoseChange',currentOdom,  'NumSamples',500);
hold on;