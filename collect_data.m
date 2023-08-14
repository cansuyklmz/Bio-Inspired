

%% Collect data for 3 cases



%% Case 1: longitudinal controller is perturbed
 % d = 0.1
 
 case1_time = out.time;
 case1_theta = out.Theta;
 case1_velocity = out.Velocity;
 case1_aoa = out.Alpha;
 case1_beta = out.Beta;
 case1_Q = out.Q;
 case1_R = out.R;
 case1_psi = out.Psi;
 case1_altitude = out.Altitude;
 case1_north = out.North;
 case1_east = out.East;
 
 case1_ = [case1_time,case1_velocity,case1_aoa,case1_beta,case1_theta,case1_psi,case1_Q...,
     case1_R,case1_altitude,case1_north,case1_east];
 
 save case1
 
%% Case 1 with deep estimator on (0.0972)
 case1_time = out.time;
 case1_theta = out.Theta;
 case1_velocity = out.Velocity;
 case1_aoa = out.Alpha;
 case1_beta = out.Beta;
 case1_Q = out.Q;
 case1_R = out.R;
 case1_psi = out.Psi;
 case1_altitude = out.Altitude;
 case1_north = out.North;
 case1_east = out.East;
 
 case1_on = [case1_time,case1_velocity,case1_aoa,case1_beta,case1_theta,case1_psi,case1_Q...,
     case1_R,case1_altitude,case1_north,case1_east];
 
 save case1_on
 
 %% Case 2 with deep estimator off
 
 case2_time = out.time;
 case2_theta = out.Theta;
 case2_velocity = out.Velocity;
 case2_aoa = out.Alpha;
 case2_beta = out.Beta;
 case2_Q = out.Q;
 case2_R = out.R;
 case2_psi = out.Psi;
 case2_altitude = out.Altitude;
 case2_north = out.North;
 case2_east = out.East;
 
 case2_off = [case2_time,case2_velocity,case2_aoa,case2_beta,case2_theta,case2_psi,case2_Q...,
     case2_R,case2_altitude,case2_north,case2_east];
 
 save case2_off
 
 %% Case 2 with deep estimator on (0.0997)
 
 case2_time = out.time;
 case2_theta = out.Theta;
 case2_velocity = out.Velocity;
 case2_aoa = out.Alpha;
 case2_beta = out.Beta;
 case2_Q = out.Q;
 case2_R = out.R;
 case2_psi = out.Psi;
 case2_altitude = out.Altitude;
 case2_north = out.North;
 case2_east = out.East;
 
 case2_on = [case2_time,case2_velocity,case2_aoa,case2_beta,case2_theta,case2_psi,case2_Q...,
     case2_R,case2_altitude,case2_north,case2_east];
 
 save case2_on
 
 %% Case 3 with deep estimator off
 
 case2_time = out.time;
 case2_theta = out.Theta;
 case2_velocity = out.Velocity;
 case2_aoa = out.Alpha;
 case2_beta = out.Beta;
 case2_Q = out.Q;
 case2_R = out.R;
 case2_psi = out.Psi;
 case2_altitude = out.Altitude;
 case2_north = out.North;
 case2_east = out.East;
 
 case3_off = [case2_time,case2_velocity,case2_aoa,case2_beta,case2_theta,case2_psi,case2_Q...,
     case2_R,case2_altitude,case2_north,case2_east];
 
 save case3_off
 
 %% Case 3 with deep estimator on
 
 case2_time = out.time;
 case2_theta = out.Theta;
 case2_velocity = out.Velocity;
 case2_aoa = out.Alpha;
 case2_beta = out.Beta;
 case2_Q = out.Q;
 case2_R = out.R;
 case2_psi = out.Psi;
 case2_altitude = out.Altitude;
 case2_north = out.North;
 case2_east = out.East;
 
 case3_on = [case2_time,case2_velocity,case2_aoa,case2_beta,case2_theta,case2_psi,case2_Q...,
     case2_R,case2_altitude,case2_north,case2_east];
 
 save case3_on
 
 %% BALLISTIC DATA
 %% Nominal Case
 altitude_nominal_ballistic = out.Altitude;
 north_nominal_ballistic = out.North;
 east_nominal_ballistic = out.East;
 time_ballistic = out.time;
 case_nominal = [altitude_nominal_ballistic,north_nominal_ballistic,east_nominal_ballistic,time_ballistic];
 
 save case_nominal
 
 %% CASE 1 OFF
 altitude_nominal_ballistic = out.Altitude;
 north_nominal_ballistic = out.North;
 east_nominal_ballistic = out.East;
 
 case_ballistic_off1 = [altitude_nominal_ballistic,north_nominal_ballistic,east_nominal_ballistic];
 
 save case_ballistic_off1
 
 %% CASE 1 ON
 altitude_nominal_ballistic = out.Altitude;
 north_nominal_ballistic = out.North;
 east_nominal_ballistic = out.East;
 case_ballistic_on1 = [altitude_nominal_ballistic,north_nominal_ballistic,east_nominal_ballistic];
 
 save case_ballistic_on1
 %% CASE 2 OFF
 altitude_nominal_ballistic = out.Altitude;
 north_nominal_ballistic = out.North;
 east_nominal_ballistic = out.East;
 case_ballistic_off2 = [altitude_nominal_ballistic,north_nominal_ballistic,east_nominal_ballistic];
 
 save case_ballistic_off2
 
 %% CASE 2 ON
 altitude_nominal_ballistic = out.Altitude;
 north_nominal_ballistic = out.North;
 east_nominal_ballistic = out.East;
 case_ballistic_on2 = [altitude_nominal_ballistic,north_nominal_ballistic,east_nominal_ballistic];
 
 save case_ballistic_on2
 %% CASE 3 OFF
  altitude_nominal_ballistic = out.Altitude;
 north_nominal_ballistic = out.North;
 east_nominal_ballistic = out.East;
 case_ballistic_off3 = [altitude_nominal_ballistic,north_nominal_ballistic,east_nominal_ballistic];
 
 save case_ballistic_off3
 %% CASE 3 ON
 
   altitude_nominal_ballistic = out.Altitude;
 north_nominal_ballistic = out.North;
 east_nominal_ballistic = out.East;
 case_ballistic_on3 = [altitude_nominal_ballistic,north_nominal_ballistic,east_nominal_ballistic];
 
 save case_ballistic_on3
  
 