import pywavefront
import numpy as np
import trimesh
import os
import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components
from body_measurements.measurement import Body3D
from zipfile import ZipFile


# embed streamlit docs in a streamlit app


from streamlit_option_menu import option_menu

current_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(current_dir, 'data')
st.title("Real Time Body size measurement")


with st.sidebar:
    selected = option_menu("Menu", ["Steps to do","Get Image", 'Generate and download OBJ File', 'Upload the OBJ file'], menu_icon="cast", default_index=1)

if selected == "Get Image":


    if st.button("Open Camera"):
        picture = st.camera_input(label="")
    # picture = st.file_uploader("Upload here")

        if picture:
            st.download_button("Download",picture,"Image.jpg")
            # st.image(picture)
        # selected = "Generate and download OBJ File"

if selected == "Generate and download OBJ File":

    components.iframe("https://imagetostl.com/" , width=800, height=1000, scrolling=True)

if selected == "Upload the OBJ file":
    file = st.file_uploader("Upload the Zipped OBJ File ")
    # print(file,type(file))
    if file :
        # print("File OPennd")
        newFileName = file.name[:-4]
        print(type(file.name),"filename")
        print(newFileName)

        with ZipFile("/home/garuda/Desktop"+"/"+file.name,'r') as zip:
            zip.printdir()
            print("Extracted")
            zip.extractall("/home/garuda/Desktop/"+newFileName)
        if file :
            print("Jhangadgutta")
            person = pywavefront.Wavefront(
            # os.path.join(data_dir,file),
            "/home/garuda/Desktop/"+newFileName+"/"+newFileName+".obj",
            # os.path.abspath("ImageToStl.com_"+newFileName)
            create_materials=True,
            collect_faces=True
            )
            faces = np.array(person.mesh_list[0].faces)
            vertices = np.array(person.vertices)

            # mesh=trimesh.Trimesh(vertices,faces)

            # st.write(mesh.show())

            body = Body3D(vertices, faces)

            body_measurements = body.getMeasurements()

            # print(body_measurements)

            st.sidebar.subheader('Height')
            st.sidebar.write(body.height())

            neck_hip_length = body.neckToHip()
            # st.sidebar.subheader('Neck 2d')
            # st.sidebar.write(neck_2d)
            st.sidebar.subheader('Neck Hip Length distance')
            st.sidebar.write(neck_hip_length)

            # st.sidebar.subheader('Weight')
            # st.sidebar.write(body.weight())

            shoulder_2d, shoulder_location, shoulder_length = body.shoulder()

            # st.sidebar.subheader('Shoulder 2d')
            # st.sidebar.write(shoulder_2d)
            # st.sidebar.subheader('shoulder location')
            # st.sidebar.write(shoulder_location)
            st.sidebar.subheader("shoulder length")
            st.sidebar.write(shoulder_length)

            chest_2d, chest_location, chest_length = body.chest()
            # st.sidebar.subheader('chest 2d')
            # st.sidebar.write(chest_2d)
            # st.sidebar.subheader('chest location')
            # st.sidebar.write(chest_location)
            st.sidebar.subheader("chest length")
            st.sidebar.write(chest_length)

            neck_2d, neck_location, neck_length = body.neck()
            # st.sidebar.subheader('Neck 2d')
            # st.sidebar.write(neck_2d)
            # st.sidebar.subheader('Neck location')
            # st.sidebar.write(neck_location)
            st.sidebar.subheader("Neck length")
            st.sidebar.write(neck_length)

            thigh_2d, thigh_location, thigh_length = body.thighOutline()
            # st.sidebar.subheader('Thigh 2d')
            # st.sidebar.write(thigh_2d)
            # st.sidebar.subheader('Thigh location')
            # st.sidebar.write(thigh_location)
            st.sidebar.subheader("Thigh length")
            st.sidebar.write(thigh_length)

            outer_leg_length = body.outerLeg()
            # st.sidebar.subheader('Neck 2d')
            # st.sidebar.write(neck_2d)
            # st.sidebar.subheader('neck location')
            # st.sidebar.write(neck_location)
            st.sidebar.subheader("neck length")
            st.sidebar.write(neck_length)

            hip_2d, hip_location, hip_length = body.hip()
            # st.sidebar.subheader('Hip 2d')
            # st.sidebar.write(hip_2d)
            # st.sidebar.subheader('Hip location')
            # st.sidebar.write(hip_location)
            st.sidebar.subheader("Hip length")
            st.sidebar.write(hip_length)

            waist_2d, waist_location, waist_length = body.waist()
            # st.sidebar.subheader('Neck 2d')
            # st.sidebar.write(neck_2d)
            # st.sidebar.subheader('Waist location')
            # st.sidebar.write(waist_location)
            st.sidebar.subheader("Waist length")
            st.sidebar.write(waist_length)
