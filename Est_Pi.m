%% Estimate Pi using a Monte Carlo Simulation.

%% Prepare workspace
clear all       % Clear all variables
close all       % Close all windows
clc             % Clear command window
rng('shuffle')  % Seed random number generator with current time

%% Plot diagram to visulize solution.
figure(1)   % Open figure window
hold on     % Hold figured

% Plot circle
x = 0:.001:1;   % Define domain
y_upper = sqrt(0.25 - (x - 0.5).^2) + 0.5;      % Upper half of circle
y_lower = -1 .* sqrt(0.25 - (x - 0.5).^2) + .5; %Lower half of circle
plot(x,y_upper, 'k-')   % Plot upper half
plot(x,y_lower, 'k-')   % Plot lower half

% Plot rectangle
x = [0 0 1 1];
y = [0 1 1 0];
plot(x,y, 'k-')

%% Calculate pi using uniform random numbers.
clear x         % Clear x
clear y         % Clear y
X = 0;          % Counter for darts landing inside circle
total = 0;      % Total darts trown
keep_going = 1; % Loop termination criteria
i = 1;          % Vector index

while  keep_going == 1;
    total = total + 1;  % Increment darts thrown
    k(i) = i;           % Vector for ploting convergence
    x(i) = rand(1);     % x-coordinate of dart
    y(i) = rand(1);     % y-coordinate of dart
    z = (x(i)-.5)^2 + (y(i)-.5)^2;  % Distance from center of circle
    
    % Determine if dart is inside or on parimeter of circle.
    if z <= .25
        X = X + 1; % Increment counter for darts inside or on circle
    end % end if
    
    % Plot point
    plot(x,y,'ro')
    pause(0.05) % pause so viewer can see point
    pi_est(i) = 4*X/total;  % Calculate estimate of pi
    
    % Determine if estimate is within 0.001 of pi
    if (pi_est(i) < 3.142) & (pi_est(i) > 3.140)
        keep_going = 0; % Set loop termination criteria
    end % end if
    
    i = i + 1;  % Increment vector index
end

%% Plot convergence
figure(2)               % Open Figure window
plot(k,pi_est,'o')      % Plot convergence
grid on
axis([0 k(i-1) 2 4])    % Set axis
pi_est(i-1)                  % Print estimate of pi
total                   % Print total number of darts thrown