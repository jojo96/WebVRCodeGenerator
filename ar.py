import streamlit.components.v1 as components  # Import Streamlit
import streamlit as st

st.title('Web VR Code Generator')
st.write('Click VR to go to VR space and scroll down to see generated code :)')

col1, col2, col3 = st.columns((1,1,2))

Options = ["a-box","a-sphere","a-cylinder","a-plane","a-cone","a-torus-knot","a-ring","a-dodecahedron","a-icosahedron"]
choose = st.sidebar.selectbox("Pick a primitive:", Options)

Options2 = [" ","ambient","point"]
choose2 = st.sidebar.selectbox("Want some lights:", Options2)

Options3 = [" ","egypt","forest","goaland","yavapai","goldmine","threetowers","poison","arches"]
choose3 = st.sidebar.selectbox("Choose Environment:", Options3)

Options4 = ["no","yes"]
choose4 = st.sidebar.selectbox("Want fog:", Options4)


def writeHelp1():
    st.write('Corresponding Code:')
    st.header("Generated Code:")
    st.write('<html><head>')
    st.write('<script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>')
    st.write('<script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>')
    st.write('<script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script>')
    st.write('</head><body>')
    st.write('<a-scene>')
    
    
    
def writeHelp2():
    st.write('</a-scene>')
    st.write('</body></html>')  


if st.sidebar.button('Generate Web VR'):

    fog = '<a-scene fog="type: exponential; color: #AAA"></a-scene>'

    if choose == "a-box":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box position="-1 0.5 -3" rotation="0 0 0" color="#4CC3D9"></a-box><a-light type='+choose2+' color="red" position="0 5 0"></a-light> <a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross">'+fog+'</a-entity></a-scene></body></html>', width=600, height=300)
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box position="-1 0.5 -3" rotation="0 0 0" color="#4CC3D9"></a-box><a-light type='+choose2+' color="red" position="0 5 0"></a-light> <a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-box position="-1 0.5 -3" rotation="0 0 0" color="#4CC3D9"></a-box>')
        st.write('<a-light type='+choose2+' color="red" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
       
        
    if choose == "a-sphere":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-sphere position="-1 0.5 -3" rotation="0 0 0" color="#4CC3D9"></a-sphere><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross">'+fog+'</a-entity></a-scene></body></html>', width=600, height=300)
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-sphere position="-1 0.5 -3" rotation="0 0 0" color="#4CC3D9"></a-sphere><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-sphere position="-1 0.5 -3" rotation="0 0 0" color="#4CC3D9"></a-sphere>')
        st.write('<a-light type='+choose2+' color="red" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
        
    if choose == "a-cylinder":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-cylinder position="-1 0.5 -3" rotation="0 0 0" color="#4CC3D9"></a-cylinder><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross">'+fog+'</a-entity></a-scene></body></html>', width=600, height=300)    
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-cylinder position="-1 0.5 -3" rotation="0 0 0" color="#4CC3D9"></a-cylinder><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-cylinder position="-1 0.5 -3" rotation="0 0 0" color="#4CC3D9"></a-cylinder>')
        st.write('<a-light type='+choose2+' color="red" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
    
    if choose == "a-plane":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-plane position="-1 0.5 -3" rotation="0 0 0" color="#4CC3D9"></a-plane><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>'+fog+'</a-scene></body></html>', width=600, height=300)
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-plane position="-1 0.5 -3" rotation="0 0 0" color="#4CC3D9"></a-plane><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-plane position="-1 0.5 -3" rotation="0 0 0" color="#4CC3D9"></a-plane>')
        st.write('<a-light type='+choose2+' color="red" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
    
    if choose == "a-cone":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-cone color="tomato" radius-bottom="1.2" radius-top="0.001" position = "-1 0.5 -3"></a-cone><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross">'+fog+'</a-entity></a-scene></body></html>', width=600, height=300)    
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-cone color="tomato" radius-bottom="1.2" radius-top="0.001" position = "-1 0.5 -3"></a-cone><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-cone color="tomato" radius-bottom="1.2" radius-top="0.001" position = "-1 0.5 -3"></a-cone>')
        st.write('<a-light type='+choose2+' color="red" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
    
    if choose == "a-torus-knot":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-torus-knot color="#B84A39" arc="180" p="2" q="7" radius="1" radius-tubular="0.1" position="-1 0.5 -3"></a-torus-knot><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross">'+fog+'</a-entity></a-scene></body></html>', width=600, height=300)
        else:    
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-torus-knot color="#B84A39" arc="180" p="2" q="7" radius="1" radius-tubular="0.1" position="-1 0.5 -3"></a-torus-knot><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-torus-knot color="#B84A39" arc="180" p="2" q="7" radius="1" radius-tubular="0.1" position="-1 0.5 -3"></a-torus-knot>')
        st.write('<a-light type='+choose2+' color="red" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
    
    if choose == "a-ring":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-ring color="teal" radius-inner=".5" radius-outer="1" position="-1 0.5 -3"></a-ring><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>'+fog+'</a-scene></body></html>', width=600, height=300)
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-ring color="teal" radius-inner=".5" radius-outer="1" position="-1 0.5 -3"></a-ring><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-ring color="teal" radius-inner=".5" radius-outer="1" position="-1 0.5 -3"></a-ring>')
        st.write('<a-light type='+choose2+' color="red" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>')
        writeHelp2()
    
    if choose == "a-dodecahedron":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-dodecahedron color="#FF116B" radius=".75" rotation = "0 60 0" position = "-1 0.5 -3"></a-dodecahedron><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>'+fog+'</a-scene></body></html>', width=600, height=300)
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-dodecahedron color="#FF116B" radius=".75" rotation = "0 60 0" position = "-1 0.5 -3"></a-dodecahedron><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-dodecahedron color="#FF116B" radius=".75" rotation = "0 60 0" position = "-1 0.5 -3"></a-dodecahedron>')
        st.write('<a-light type='+choose2+' color="red" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
    
    if choose == "a-icosahedron":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-icosahedron color="#FF926B" radius=".755" position = "-3 3.25 -3"></a-icosahedron><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>'+fog+'</a-scene></body></html>', width=600, height=300)
        else:    
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-icosahedron color="#FF926B" radius=".755" position = "-3 3.25 -3"></a-icosahedron><a-light type='+choose2+' color="blue" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-icosahedron color="#FF926B" radius=".755" position = "-3 3.25 -3"></a-icosahedron>')
        st.write('<a-light type='+choose2+' color="red" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #445; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
    
    
    
