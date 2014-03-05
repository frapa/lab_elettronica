load ../dati/monte.mat
load ../dati/valle.mat

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[monte(:, 1), valle(:, 1)]

% MONTE
vm = monte(:, 2);
im = monte(:, 3);
dvm = monte(:, 6);
dim = monte(:, 7);

rvm = monte(:, 4);
ram = monte(:, 5);

% ANALISI MONTE

rxm = (vm .* rvm) ./ (rvm .* im .- vm)
drxv = sqrt(((rvm .^ 2 .* im .* dvm) .^ 2 .+ (vm .* rvm .^ 2 .* dim) .^ 2) ./ (rvm .* im .- vm) .^ 4)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% VALLE
vv = valle(:, 2);
iv = valle(:, 3);
dvv = valle(:, 6);
div = valle(:, 7);

rvv = valle(:, 4);
rav = valle(:, 5);

% ANALISI VALLE
rxv = (vv .- iv .* rav) ./ iv
drxm = sqrt((dvv ./ iv) .^ 2 .+ (vv .* div ./ iv .^ 2) .^ 2)
