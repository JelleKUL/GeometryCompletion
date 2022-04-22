import open3d as o3d
import matplotlib
import numpy as np
import jellecomplete.params as params

def hello_world():
    return "hello world!"

def get_geometry(path):
    """Returns the open3d geometry object from a path"""
    
    newGeometry = None
    if(path.endswith(tuple(params.MESH_EXTENSION))):
        newGeometry = o3d.io.read_triangle_mesh(path)
        #if not newGeometry.has_vertex_normals():
        newGeometry.compute_vertex_normals()
    elif(path.endswith(tuple(params.PCD_EXTENSION))):
        newGeometry = o3d.io.read_point_cloud(path)
    return newGeometry

def show_geometries(geometries, color = False):
    "displays the array of meshes in a 3D view"

    viewer = o3d.visualization.Visualizer()
    viewer.create_window()
    frame = o3d.geometry.TriangleMesh.create_coordinate_frame()
    viewer.add_geometry(frame)
    for i, geometry in enumerate(geometries):
        if color:
            geometry.paint_uniform_color(matplotlib.colors.hsv_to_rgb([float(i)/len(geometries),0.8,0.8]))
        viewer.add_geometry(geometry)
    opt = viewer.get_render_option()
    opt.background_color = np.asarray([1,1,1])
    opt.light_on = True
    viewer.run()