# WebVRCodeGenerator
A simple app that generates WebVR code for scenes made using A-Frame primitives and displays the corresponding HTML code

# A-Frame
A-frame is a really nice and easy to use web framework for creating VR and AR experiences.
![Image](https://uploads-ssl.webflow.com/5674237d08dc33257975b784/59be08991002280001269a58_a-frame.png)

- [Documentation](https://aframe.io/docs/1.2.0/introduction/) - The official A-Frame documentation

- [Features](https://github.com/supermedium/superframe) - A super collection of A-Frame components.

- [More Examples](https://github.com/jojo96/AFrame3D/tree/main/A-Frame%20Examples) - More A-Frame Example codes

# Running the app
 
This app is meant to be a starting point for WebVR. You can play around with VR primitives like a-box, a-sphere and generate simple VR scenes. Also, the corresponding html code is generated. <b>Access the app here: https://share.streamlit.io/jojo96/webvrcodegenerator/main/ar.py </b>
 
The app interface:
![Image](https://github.com/jojo96/WebVRCodeGenerator/blob/main/Images/appScreenshot.png)

Some of the various supported [primitives](https://aframe.io/docs/1.2.0/introduction/) are:

- a-box
- a-sphere
- a-ring
- a-cylinder
- a-torus-knot
- a-plane


Also, one can include point light or ambient light in the scene, change environment or add fog!!

These various options can be selected in the sidebar and the button <b>Generate Web VR</b> will render the <b>VR Scene</b> and generate <b>HTML code</b>. This HTML code can be saved in an index.html file and served using a web server.

You can use the [ZapWorks command-line tool](https://docs.zap.works/universal-ar/zapworks-cli/) to serve your HTML folder over HTTPS for access on your local computer:

      zapworks serve .

Remember to run the command within the folder that has your saved index.html file.

# Local Installation

    git clone https://github.com/jojo96/WebVRCodeGenerator.git
    cd WebVRCodeGenerator
    streamlit run ar.py

A page would open in our browser and you can interact with the streamlit app.

Author: [Jojo](https://twitter.com/I_m_Jojo): [LinkedIn](https://www.linkedin.com/in/ujjayanta-bhaumik/)
