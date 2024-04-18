import streamlit as st
import streamlit_option_menu as option_menu
import google.generativeai as genai

# Read API key from file
with open('keys/.gemini_api_key.txt') as f:
    api_key = f.read()

# Configure Gemini API
genai.configure(api_key=api_key)

# Initialize the gemini model
model = genai.GenerativeModel(
    model_name='gemini-1.5-pro-latest',
    system_instruction="""Your Name is Innomanion AI, an AI Conversational Tutor in Data Science.
                              Innomatics Research Labs is a pioneer in “Transforming Career and Lives” of individuals in the Digital Space 
                              by catering advanced training on IBM Certified Data Science, Python, IBM Certified Predictive Analytics Modeler, 
                              Machine Learning, Artificial Intelligence (AI), Full-stack web development, Amazon Web Services (AWS), DevOps, Microsoft Azure, 
                              Big data Analytics, Digital Marketing, and Career Launching program for students who are willing to showcase their skills 
                              in the competitive job market with valuable credentials, and also can complete courses with a certificate.
                              """
)


def main():
    st.set_page_config(
        page_title='AI Powered Data Science Tutor',
        page_icon='🤖'
    )

    st.balloons()
    st.title("🤖 Data Science Tutor")

    # Side bar initialization and creation
    with st.sidebar:
        selected = option_menu(
            menu_title = 'AI Tutor',
            options = ['Home', 'Authenticate'],
            icons = ['house', 'cloud-upload'])

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello, this is Innomanion AI, how can I help you today?"}
        ]

    # Display all messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Receive user input
    user_input = st.chat_input()

    # Store user input in session
    if user_input is not None:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # Generate AI response
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                ai_response = model.generate_content(user_input)
                st.write(ai_response.text)
            new_ai_message = {"role": "assistant", "content": ai_response.text}
            st.session_state.messages.append(new_ai_message)


if _name_ == "_main_":
    main()