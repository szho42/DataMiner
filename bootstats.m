% function bootstats

over_2_5 = [ 0.6053 0.5895 0.6105 0.5868 0.5368 0.5895 0.5868 0.5711 ...
    0.6368 0.6842 0.6474 0.6553 0.5921 ]; % 0.6267

nSamps = length(over_2_5);
mOver2_5 = mean (over_2_5);
semOver_2_5 = std(over_2_5) / sqrt(nSamps);


%% Bootstrap the mean
nboot = 10000;
bootstat = bootstrp(nboot,@mean, over_2_5);

figure(1);clf;
hist(bootstat, 50);


%% Questions

% Taking the lower boundary of 0.57 we need 1.8 rates: (0.8 * 0.57) - 0.43
% = 0.026
% How many times the house offers bets below 0.8 for over 2.5 in the
% premier league? What were number of wins for those bets in the last
% years?



