function upload


% Load eye event times
% OPEN FILE
dir = './data/data_by_season/English/';
name = 'England-All';

fid_evs = fopen([ dir name '.txt']);

ln = 1;

while (1)
    
    % get line by line of text file
    tline = fgetl(fid_evs);

    %Check whether we've reached the end of the file
    if tline == -1, break, end;
    
     %Skip line if it's an empty one.
     if isempty(tline), disp(['Check Empty Line: ' num2str(ln)]), end;          
                
                
     C = textscan(tline, '%n %n %n %n %n');
                
    % id	Local	Visitante	Tiempo	Minuto  
     data(ln, 1) = C{1};   
     data(ln, 2) = C{2};
     data(ln, 3) = C{3};
     
     if isempty(C{4})
         data(ln, 4) = nan;
     else
         data(ln, 4) = C{4};
     end
     
%      if isempty(C{5})
%          data(ln, 5) = nan;
%      else
%          data(ln, 5) = C{5};
%      end      
   
     ln = ln + 1;
    
     if mod(ln, 1000) == 0
         disp(ln)
     end
end


save([dir name], 'data')

