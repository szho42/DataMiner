function main_analysis

% This function loads the games previously put together by the function
% 'upload' and calculates the main statistics of the league / leagues

dir = './data/data_by_season/English/';
name = 'England-All';

%% load data
A = load([dir name '.mat']);
data = A.data;
ids = unique(data(:,1));

%% Select a sample

% randi = randperm(length(ids));
% randi = randi(1:500);
% ids = ids(randi);
% data = data( ismember(data(:,1), ids) , :); 

%% Select cut-off time

time = 80; %[1 10 15 20 25 30 35 40]; % minutes of second half


%% Collect data

games = nan(length(ids), 4);


for t = 1 : length(time)
    
    for gm = 1 : length(ids)
        
        % id	Local	Visitante	Tiempo	Minuto
        aux = data(data(:,1) == ids(gm), :);
        
        final_score = [sum(aux(:,2)) sum(aux(:,3))];
        if final_score(1) > final_score(2)
            result_code = 1; % local win
        elseif final_score(1) == final_score(2)
            result_code = 2; % draw
        elseif final_score(1) < final_score(2)
            result_code = 3; % away win
        end
        
        
        % Get score at the Nth minute
        bf = aux( aux(:,4) <= time(t), : ); 
        prelim_score = [sum(bf(:,2)) sum(bf(:,3))];
        if prelim_score(1) > prelim_score(2)
            prelim_code = 1;
        elseif prelim_score(1) == prelim_score(2)
            prelim_code = 2;
        elseif prelim_score(1) < prelim_score(2)
            prelim_code = 3;
        end
        
        if result_code == prelim_code
            result_switch = 0;
        else
            result_switch = 1;
        end
        
        % Decide if there was a switch
        games(gm, 1, t) = ids(gm); % Game Id
        games(gm, 2:3, t) = prelim_score; % prelim score
        games(gm, 4:5, t) = final_score; % final score
        games(gm, 6, t) = result_switch; % switch flag
        games(gm,7, t) = result_code; % final result
       
        
%         % 2-0 games
%         nGoals = size(aux,1);
%         
%         if nGoals >= 2
%             if sum(aux(1:2,2)) == 2
%                 is_2_0(gm,1,t) = 1;
%             elseif sum(aux(1:2,3)) == 2
%                 is_0_2(gm,1, t) = 1;
%             elseif sum(aux(1:2,2)) == 1 && sum(aux(1:2,3)) == 1
%                 is_2_0(gm,1, t) = 0;
%                 is_0_2(gm,1, t) = 0;
%             end
%             
%         else % less than 2 goals in the game: 0-0 or 1-0
%             is_2_0(gm,1, t) = 0;
%             is_0_2(gm,1, t) = 0;
%         end
    end
end

%% plot across times
% 
% labels = {'0-0' '1-0' '0-1' '1-1' '2-0' '2-1' '2-2' '0-2' '1-2' '3-0' '3-1' '3-2' '3-3' ...
%     '0-3' '1-3' '2-3'};
% conds = {[0 0] [1 0] [0 1] [1 1] [2 0] [2 1] [2 2] [0 2] [1 2] [3 0] [3 1] [3 2] [3 3] ...
%     [0 3] [1 3] [2 3]};
% 
% figure(1); clf; 
% z = 1;
% for m = 1 : length(conds)
%     
%     for t = 1 : length(time)
%         
%         aux = games(games(:,2) == conds{m}(1) & games(:,3) == conds{m}(2), :, t);       
%         vec(t) = mean(aux(:,6));        
%     end
%     subplot(4,4,z)
%     plot(time, vec)
%     title(labels{m});
%     ylim([0 0.6])
%     z = z + 1;
% end

%%

% t = 1; % here it is the same whatever dimension as it is the overall probability
% games_2_0 = games(is_2_0(:,:,t) == 1,:,t);
% games_0_2 = games(is_0_2(:,:,t) == 1, :,t);
% 
% prop_ch_2_0 = sum(games_2_0(:,7) == 1) / size(games_2_0, 1);
% prop_ch_0_2 = sum(games_0_2(:,7) == 3) / size(games_0_2, 1);

% size( games(games(:,7) == 3), 1) / size(games, 1)

%% 
clc;
Country = name %#ok

%% Goals odd / even

even = mod(games(:,4) + games(:,5),2) == 0;
propEven = sum(even) / length(even);
msg = sprintf('Games with even score: %f' , propEven); disp(msg)
msg =sprintf('Games with odd score: %f' ,  1-propEven);disp(msg);

%% Both teams to score

one_score = games(games(:,4) == 0 & games(:,5) == 0 | games(:,4) == 1 & games(:,5) == 0 | ...
 games(:,4) == 0 & games(:,5) == 1 | games(:,4) == 2 & games(:,5) == 0 | games(:,4) == 0 & games(:,5) == 2 ...
 | games(:,4) == 3 & games(:,5) == 0 | games(:,4) == 0 & games(:,5) == 3 ...
 | games(:,4) == 4 & games(:,5) == 0 | games(:,4) == 0 & games(:,5) == 4 | ...
 games(:,4) == 5 & games(:,5) == 0  | games(:,4) == 0 & games(:,5) == 5,  :) ;

prop_oneScore = size(one_score, 1) / size(games,1);

msg = sprintf('Only one team scores: %f' , prop_oneScore);
disp(msg);
msg = sprintf('Both teams score: %f', 1-prop_oneScore);
disp(msg);


%% N Goals for the final score

less_0_5 = games(games(:,4) == 0 & games(:,5) == 0 , :) ; 

less_1_5 = games(games(:,4) == 0 & games(:,5) == 0 | games(:,4) == 1 & games(:,5) == 0 | ...
 games(:,4) == 0 & games(:,5) == 1 , :) ; 

less_2_5 = games(games(:,4) == 0 & games(:,5) == 0 | games(:,4) == 1 & games(:,5) == 0 | ...
 games(:,4) == 0 & games(:,5) == 1 | games(:,4) == 2 & games(:,5) == 0 | games(:,4) == 0 & games(:,5) == 2, :) ; 

less_3_5 = games(games(:,4) == 0 & games(:,5) == 0 | games(:,4) == 1 & games(:,5) == 0 | ...
 games(:,4) == 0 & games(:,5) == 1 | games(:,4) == 2 & games(:,5) == 0 | games(:,4) == 0 & games(:,5) == 2 | ...
 games(:,4) == 2 & games(:,5) == 1 | games(:,4) == 1 & games(:,5) == 2 | games(:,4) == 3 & games(:,5) == 0 | ...
 games(:,4) == 0 & games(:,5) == 3, :) ; 

th = 0.03; % earning proportion

less_0_5_prop =  size(less_0_5,1) / size(unique(games(:,1)), 1);
more_0_5_prop = 1 - less_0_5_prop;

th_more_0_5 = ( (th + less_0_5_prop) / more_0_5_prop ) + 1; % rate betting threshold 
th_less_0_5 = ( (th + more_0_5_prop) / less_0_5_prop ) + 1; % rate betting threshold 

less_1_5_prop =  size(less_1_5,1) / size(unique(games(:,1)), 1);
more_1_5_prop = 1 - less_1_5_prop;

th_more_1_5 = ( (th + less_1_5_prop) / more_1_5_prop ) + 1; % rate betting threshold 
th_less_1_5  = ( (th + more_1_5_prop) / less_1_5_prop ) + 1; % rate betting threshold 


less_2_5_prop = size(less_2_5, 1) / size(unique(games(:,1)), 1);
more_2_5_prop = 1 - less_2_5_prop;

th_more_2_5  = ( (th + less_2_5_prop) / more_2_5_prop ) + 1; % rate betting threshold 
th_less_2_5 = ( (th + more_2_5_prop) / less_2_5_prop ) + 1; % rate betting threshold 


less_3_5_prop = size(less_3_5, 1) / size(unique(games(:,1)), 1);
more_3_5_prop = 1 - less_3_5_prop;

th_more_3_5 = ( (th + less_3_5_prop) / more_3_5_prop ) + 1; % rate betting threshold 
th_less_3_5 = ( (th + more_3_5_prop) / less_3_5_prop ) + 1; % rate betting threshold 


Goals_Over_under = {'p > 0.5: ' more_0_5_prop '; earnings = ' th ' bet threshold: ' th_more_0_5 ;
     'p < 0.5: ' less_0_5_prop '; earnings = ' th ' bet threshold: ' th_less_0_5 ; 
     
     'p > 1.5: ' more_1_5_prop '; earnings = ' th ' bet threshold: ' th_more_1_5 ;
      'p < 1.5: ' less_1_5_prop '; earnings = ' th ' bet threshold: ' th_less_1_5;
     
     'p > 2.5: ' more_2_5_prop '; earnings = ' th ' bet threshold: ' th_more_2_5 ;
     'p < 2.5: ' less_2_5_prop '; earnings = ' th ' bet threshold: ' th_less_2_5 ;
        
     'p > 3.5: ' more_3_5_prop '; earnings = ' th ' bet threshold: ' th_more_3_5 ;
     'p < 3.5: ' less_3_5_prop '; earnings = ' th ' bet threshold: ' th_less_3_5 } 
 


%% Double Chance

nGames = size(unique(games(:,1)), 1);

home = games(games(:,7) == 1 , :);
draw = games(games(:,7) == 2 , :);
away = games(games(:,7) == 3 , :);

home_draw = games(games(:,7) == 1 | games(:,7) == 2, :);
draw_away = games(games(:,7) == 2 | games(:,7) == 3, :);
home_away = games(games(:,7) == 1 | games(:,7) == 3, :);


home_prop = size(home, 1) / nGames;
draw_prop = size(draw, 1) / nGames;
away_prop = size(away, 1) / nGames;
home_draw_prop = size(home_draw, 1) / nGames;
draw_away_prop = size(draw_away, 1) / nGames;
home_away_prop = size(home_away, 1) / nGames;

home_draw_th = ( (th + (1-home_draw_prop)) / home_draw_prop ) + 1; % rate betting threshold 
draw_away_th = ( (th + (1-draw_away_prop)) / draw_away_prop ) + 1; % rate betting threshold 
home_away_th = ( (th + (1-home_away_prop)) / home_away_prop ) + 1; % rate betting threshold 

Double_Chance = {''      'Prob'  'Th'
                'Home: ', home_prop '';
                'Draw: ', draw_prop '';
                'Away: ', away_prop '';
                'Home - Draw: ' home_draw_prop home_draw_th;
                'Draw - Away: ' draw_away_prop draw_away_th;
                'Home - Away: ' home_away_prop home_away_th}


%%

labels = {'0-0' '1-0' '0-1' '1-1' '2-0' '2-1' '2-2' '0-2' '1-2' '3-0' '3-1' '3-2' '3-3' ...
    '0-3' '1-3' '2-3'};
conds = {[0 0] [1 0] [0 1] [1 1] [2 0] [2 1] [2 2] [0 2] [1 2] [3 0] [3 1] [3 2] [3 3] ...
    [0 3] [1 3] [2 3]};
nGames = size(unique(games(:,1)), 1);

th = 0.05; 
C{1,1} = ['Result at ' num2str(time) 'min'];
C{1,2} = 'Prob No Change';
C{1,3} = ['Th: ' num2str(th)];
C{1,4} = 'Occurence (over total games)';

for m = 1 : length(conds)
    
    aux = games(games(:,2) == conds{m}(1) & games(:,3) == conds{m}(2), :);
    C{m+1,1} = labels{m};  
    
    prob = mean(aux(:,6));
    C{m+1,2} = 1 - prob;
    
    C{m+1,3} =  ( (th + (prob)) / (1-prob) ) + 1; % rate betting threshold 
    
    C{m+1,4} = size(aux, 1) / nGames;
end

disp(C)


%%

% bootstrap confidence intervals


%% Goals at Nth minute

% less_1_5 = games(games(:,2) == 0 & games(:,3) == 0 | games(:,2) == 1 & games(:,3) == 0 | ...
%  games(:,2) == 0 & games(:,3) == 1 , :) ; 
% 
% less_2_5 = games(games(:,2) == 0 & games(:,3) == 0 | games(:,2) == 1 & games(:,3) == 0 | ...
%  games(:,2) == 0 & games(:,3) == 1 | games(:,2) == 2 & games(:,3) == 0 | games(:,2) == 0 & games(:,3) == 2, :) ; 
% 
% less_3_5 = games(games(:,2) == 0 & games(:,3) == 0 | games(:,2) == 1 & games(:,3) == 0 | ...
%  games(:,2) == 0 & games(:,3) == 1 | games(:,2) == 2 & games(:,3) == 0 | games(:,2) == 0 & games(:,3) == 2 | ...
%  games(:,2) == 2 & games(:,3) == 1 | games(:,2) == 1 & games(:,3) == 2 | games(:,2) == 3 & games(:,3) == 0 | ...
%  games(:,2) == 0 & games(:,3) == 3, :) ; 
% 
% less_1_5_prop =  size(less_1_5,1) / size(unique(games(:,1)), 1);
% more_1_5_prop = 1 - less_1_5_prop;
% 
% 
% less_2_5_prop = size(less_2_5, 1) / size(unique(games(:,1)), 1);
% more_2_5 = 1 - less_2_5_prop;
% 
% 
% less_3_5_prop = size(less_3_5, 1) / size(unique(games(:,1)), 1);
% more_3_5 = 1 - less_3_5_prop;




