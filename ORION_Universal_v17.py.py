# ==============================================================================
# FRAME 1: GALACTA HUB (Mit direktem Figma-Button Overlay)
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    img_path = get_asset_path("Frame 1.jpg")
    img_b64 = get_base64_image(img_path)
    
    # Figma CSS Styling für das Dashboard-Element einbinden
    st.markdown("""
    <style>
        .figma-canvas {
            position: relative;
            width: 100%;
            max-width: 1200px;
            margin: auto;
        }
        .figma-canvas img.bg-frame {
            width: 100%;
            display: block;
        }
        /* Exakte Position aus deinem Figma Export für .group-140 */
        .figma-dashboard-btn {
            position: absolute;
            top: 68%;       /* Prozentuale Höhe im Figma Frame */
            left: 12%;      /* Prozentuale Position von links */
            width: 18%;     /* Breite der Klickzone */
            height: 8%;     /* Höhe der Klickzone */
            z-index: 9999;
            cursor: pointer;
            border: 2px dashed rgba(255, 18, 42, 0.6); /* Dezent roter Schein zum Ausrichten */
            border-radius: 6px;
            transition: all 0.2s ease-in-out;
        }
        .figma-dashboard-btn:hover {
            background-color: rgba(255, 18, 42, 0.3);
            border: 2px solid #FF122A;
            box-shadow: 0 0 15px #FF122A;
        }
    </style>
    """, unsafe_allow_html=True)

    # 1. Bild mit dem unsichtbaren Overlay-Button aus Figma rendern
    if img_b64:
        st.markdown(f'''
        <div class="figma-canvas">
            <img src="data:image/jpeg;base64,{img_b64}" class="bg-frame">
        </div>
        ''', unsafe_allow_html=True)
    elif img_path:
        st.image(img_path, use_container_width=True)

    # 2. Transparenter Streamlit Klick-Trigger exakt an der Figma-Position
    col1, col2, col3 = st.columns([0.35, 0.3, 1.35])
    with col1:
        st.markdown("<div style='margin-top: -20%; position: relative; z-index: 10000;'>", unsafe_allow_html=True)
        if st.button("DASHBOARD", key="btn_figma_dash", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)
