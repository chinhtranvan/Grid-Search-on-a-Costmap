function [] = ShowGrid(fnameGrid)
fp = fopen(fnameGrid, 'r');
nrRows = fscanf(fp, '%d', 1);
nrCols = fscanf(fp, '%d', 1);
data = zeros(nrRows, nrCols);
for r = 1 : 1 : nrRows
for c = 1 : 1 : nrCols
data(r, c) = fscanf(fp, '%f', 1);
end
fprintf('..reading row %d out of %d rows\n', r, nrRows);
end 
fclose(fp);

imshow(uint8(data*255))

end

