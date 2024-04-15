import pyassimp

def convert_obj_to_md3(obj_path, md3_path):
    # Load the OBJ file
    scene = pyassimp.load(obj_path, processing=pyassimp.postprocess.aiProcess_Triangulate)

    if not scene.meshes:
        print("No meshes found in the OBJ file.")
        return

    # Create a new scene to hold the converted mesh and animations
    md3_scene = pyassimp.AssimpScene()

    # Iterate over all animations in the original scene
    for anim in scene.animations:
        md3_scene.animations.append(anim)

    # Add each mesh from the original scene to the new scene
    for mesh in scene.meshes:
        md3_scene.meshes.append(mesh)

    # Save the new scene to an MD3 file
    pyassimp.export(md3_scene, md3_path, 'md3')

    print(f"Conversion successful. MD3 file saved as: {md3_path}")

# Example usage
obj_file = 'path/to/your/object.obj'
md3_file = 'path/to/save/converted/object.md3'
convert_obj_to_md3(obj_file, md3_file)
