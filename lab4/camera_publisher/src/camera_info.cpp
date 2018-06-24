#include <ros/ros.h>
#include <sensor_msgs/Image.h>

int main(int argc, char** argv){
  ros::init(argc, argv, "camera_publisher");

  ros::NodeHandle n;
  ros::Publisher camera_pub = n.advertise<sensor_msgs::Image>("camera", 50);

  ros::Rate r(1.0);
  while(n.ok()){
    //generate some fake data for our laser scan
    ros::Time camera_time = ros::Time::now();

  
    sensor_msgs::Image camera;
    camera.header.stamp = camera_time;
    camera.header.frame_id = "TANo.1";
    camera.height = 720;
    camera.width = 600;
    camera.encoding="rgb8";
    camera.is_bigendian= 10;
    camera.step =camera.height*3;
    camera_pub.publish(camera);
    r.sleep();
  }
}
