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
acazz_m = vm ./ im;
dacazz_m = sqrt((dvm ./ im) .^ 2 .+ (dim .* vm ./ im .^ 2) .^ 2);

rxm = (vm .* rvm) ./ (rvm .* im .- vm);
drxm = sqrt(((rvm .^ 2 .* im .* dvm) .^ 2 .+ (vm .* rvm .^ 2 .* dim) .^ 2) ./ (rvm .* im .- vm) .^ 4);

% MOSTRA DATI
[acazz_m, dacazz_m, rxm, drxm]

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% VALLE
vv = valle(:, 2);
iv = valle(:, 3);
dvv = valle(:, 6);
div = valle(:, 7);

rvv = valle(:, 4);
rav = valle(:, 5);

% ANALISI VALLE
acazz_v = vv ./ iv;
dacazz_v = sqrt((dvv ./ iv) .^ 2 .+ (div .* vv ./ iv .^ 2) .^ 2);

rxv = (vv .- iv .* rav) ./ iv;
drxv = sqrt((dvv ./ iv) .^ 2 .+ (vv .* div ./ iv .^ 2) .^ 2);

% MOSTRA DATI
[acazz_v, dacazz_v, rxv, drxv]
