import os

opts = lux.getImportOptions()
print(opts)


opts['accurate_tessellation'] = False
opts['adjust_camera_look_at'] =  False
opts['adjust_environment'] =  True
opts['applyLibraryMaterials'] =  False
opts['camera_import'] =  True
opts['center_geometry'] =  True
opts['compute_normals'] =  True
opts['frame'] =  0
opts['geometry_scale'] =  10
opts['geometry_units'] =  1000.0
opts['group_by'] =  2
opts['group_by_shader'] =  False
opts['include_hidden_surfaces'] =  False
opts['include_nurbs'] =  False
opts['include_single_surfaces'] =  True
opts['material_name_from_color'] =  False
opts['mayaForceVersion'] =  ''
opts['merge_groups'] =  False
opts['merge_objects'] =  False
opts['new_import'] =  False
opts['retain_materials'] =  True
opts['same_coordinates'] =  True
opts['separate_materials'] =  True
opts['separate_parts'] =  True
opts['snap_to_ground'] =  True
opts['tessellation_quality'] =  0.20000000298023224
opts['up_vector'] =  1
opts['update_mode'] =  False


cwd = os.getcwd()
print(cwd) # print current working directory

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        file_path = os.path.join(root, name)
        if file_path.endswith('.obj'):
        	print( 'Loading file ' + file_path + '\n' )
        	lux.importFile(file_path, opts = opts)




