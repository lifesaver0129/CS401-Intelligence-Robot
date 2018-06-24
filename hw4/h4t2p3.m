clc
close all

nb_sample = 500;

v = pi;
w = pi/2;
r = 10;
theta = -pi/10;

x_c = 0;
y_c = 10;



x = 0.1;y = 1.1;a1 = 0.01;a2 = 0.01;a3 = 0.1;a4 = 0.1;a5 = 0.01;a6 = 0.01;

delt = 1;

trajectory_data = zeros(3,nb_sample);

for n = 1: nb_sample
    v_a = v + normrnd(0, a1*abs(v)+a2*abs(w));
    w_a = w + normrnd(0, a3*abs(v)+a4*abs(w));
    r_a = normrnd(0, a5*abs(v)+a6*abs(w));
    
    x_p = x - (v_a/w_a)*sin(theta) + (v_a/w_a)*sin(theta+w_a*delt);
    y_p = y + (v_a/w_a)*cos(theta) - (v_a/w_a)*cos(theta+w_a*delt);
    theta_p = theta + w_a*delt + r_a*delt;
    
    
    trajectory_data(1,n) = x_p;
    trajectory_data(2,n) = y_p;
    trajectory_data(3,n) = theta_p;
end  




alpha=0:pi/20:2*pi;    %½Ç¶È[0,2*pi] 
R=0.1;                   %°ë¾¶ 
x=R*cos(alpha); 
y=R*sin(alpha); 
plot(x,y,'-') 
fill(x,y,'w');
hold on;

alpha2=0:pi/20:2*pi;    %½Ç¶È[0,2*pi] 
R2=0.1;                   %°ë¾¶ 
x=2.5+R2*cos(alpha2); 
y=2.5+R2*sin(alpha2); 
plot(x,y,'-') 
fill(x,y,'w');
hold on;

alpha2=0:pi/20:2*pi;    %½Ç¶È[0,2*pi] 
R2=0.1;                   %°ë¾¶ 
x=0+R2*cos(alpha2); 
y=2.5+R2*sin(alpha2); 
plot(x,y,'-') 
fill(x,y,'r');
hold on;



alpha2=3*pi/2:pi/20:2*pi;    %½Ç¶È[0,2*pi] 
R2=2.5;                   %°ë¾¶ 
x=0+R2*cos(alpha2); 
y=2.5+R2*sin(alpha2); 
plot(x,y,'-');
hold on ; 


axis equal;
line([0,0],[0,2.5]); hold on;
line([0,2.5],[2.5,2.5]); hold on;


for i = 1:nb_sample
    plot(trajectory_data(1,i),trajectory_data(2,i),'b.');
end
    %scatter(trajectory_data(1,5:nb_sample),trajectory_data(2,5:nb_sample),'.'); 


