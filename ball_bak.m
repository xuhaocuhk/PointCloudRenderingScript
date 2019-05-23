clear all; 

BALL_SIZE = 0.005;

[V, F] = read_off('ball_uniform_simp.off');
V = V';
F = F';
F = F-1;
vertex_num = size(V, 1);
face_num = size(F, 1);
V = V * BALL_SIZE;

keypts = load('horse_input.xyz');
keypts_num = size(keypts, 1);
total_vertex_num = vertex_num * keypts_num;
total_face_num = face_num * keypts_num;
V_total = zeros(total_vertex_num, 7);
F_total = zeros(total_face_num, 3);

for i = 1:keypts_num
    disp([i,keypts_num]);
    translation_vec = keypts(i, [1:3]);
    %color_vec       = keypts(i, [4:6]);
    translation_mat = repmat(translation_vec, vertex_num, 1);
    %color_mat       = repmat(color_vec, vertex_num, 1);
    V_new = (V - translation_mat).*(-1);
    V_total((vertex_num*(i-1)+1): vertex_num*i, :) = [V_new color_mat ones(vertex_num, 1)*255];
    F_total((face_num*(i-1)+1):face_num*i, :) = F + (i-1)*vertex_num;
end

output_path = 'complete_output.off';
fid = fopen(output_path, 'w');
fprintf(fid, 'COFF\n');
fprintf(fid, '%d %d %d\n', total_vertex_num, total_face_num, 0);
for j = 1:total_vertex_num
    fprintf(fid, '%f %f %f %d %d %d %d\n', V_total(j, :));
end
for j = 1:total_face_num
    fprintf(fid, '%d %d %d %d\n', 3, F_total(j, :));
end
fclose(fid);

