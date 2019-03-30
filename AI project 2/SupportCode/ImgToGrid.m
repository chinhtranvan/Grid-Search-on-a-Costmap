function [] = ImgToGrid(fnameImg, fnameGrid)
data = imread(fnameImg);
ddata = double (data);
fp = fopen(fnameGrid, 'w');
[nrRows, nrCols] = size(ddata);
fprintf(fp, '%d %d\n', nrRows, nrCols);
for r = 1 : 1 : nrRows
  for c = 1 : 1 : nrCols
     fprintf(fp, '%f ', ddata(r, c) / 255)
  end
  fprintf('..wrote row %d out of %d\n', r, nrRows);
  fprintf(fp, '\n');
end
fclose(fp);
end

