%{
--------------------------- Instruction Manual ----------------------------
    1) Run Matlab over conda envirement.
        |
        |
         - ->   - Run Anaconda Powershell Promt
                
                - Activate conda envirement "envirement_name"
                    
                    "conda activate envirement_name"
                
                - run "matlab"   

    2)  Run following line to import and test module.

    3) If needed, reload the module.

%}


%% Define python envirement and executiın mode 

terminate(pyenv)

lookback = 20;
inputFeatures  = 5;
outputFeatures = 2;

% pyversion('C:\Users\ss\anaconda3\envs\tensorflow_matlab\python.exe')
% pyversion('C:\Users\cnsyk\anaconda3\envs\tensorflow_matlab\python.exe')
pyversion('C:\Users\cnsyk\anaconda3\python.exe')
pyenv('ExecutionMode','OutOfProcess');
% pyversion('C:\Users\cnsyk\anaconda3\python.exe')
test_model = py.importlib.import_module('FINAL_module');
py.FINAL_module.run(zeros(lookback,inputFeatures)) %for actuators
py.FINAL_module.runv2(zeros(lookback,inputFeatures)) %for actuators

%py.predictorModule_act_s1_3.run(zeros(lookback,inputFeatures)) %for actuators
%test_model = py.importlib.import_module('predictorModule'); for pqr
%py.predictorModule.run(zeros(50,17))
% cd(oldDirectory);



%  %% Use if you change your python file, use following line to reloding for actuataors
% clear classes
% test_model = py.importlib.import_module('predictorModule_act');
% %test_model = py.importlib.import_module('predictorModule'); % for pqr
% py.importlib.reload(test_model);
% 
% py.tensorflow.keras.backend.clear_session()
% 
% %%
% tstart = tic;
% for i= 1:100
%     tic
%     %py.predictorModule.run; %for pqr
%     py.predictorModule_act.run;
%     toc
% end
% tstop = toc(tstart);

% 
% %% Terminate Envirment if needed.
% terminate(pyenv)
% 
% %% Test python Libraries
% tfmod = py.importlib.import_module('tensorflow'); % seems without importing first, the following does notwork
% %%
% py.tensorflow.keras.optimizers.Adadelta()
% testmod = py.importlib.import_module('tensorflow.keras.optimizers');

