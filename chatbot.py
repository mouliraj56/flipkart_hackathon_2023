# import streamlit as st
# import os
# import chainlit as cl
# from langchain import HuggingFaceHub, PromptTemplate, LLMChain

# # Define your AI assistant setup and configurations here
# os.environ['API_KEY'] = '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'
# model_id = 'tiiuae/falcon-7b-instruct'
# falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],
#                             repo_id=model_id,
#                             model_kwargs={"temperature": 0.8, "max_new_tokens": 2000})
# template = """
# You are an AI assistant that provides helpful answers to user queries.
# {question}
# """

# prompt = PromptTemplate(template=template, input_variables=['question'])

# falcon_chain = LLMChain(llm=falcon_llm,
#                         prompt=prompt,
#                         verbose=True)

# # Define the Streamlit app
# def main():
#     st.title("AI Assistant")

#     # Create an input field for the user to enter their question
#     user_question = st.text_input("Enter your question:")

#     # Create a button to submit the question
#     if st.button("Ask"):
#         # Use your AI assistant to generate a response based on the user's question
#         response = falcon_chain.run(user_question)
        
#         # Display the response to the user
#         st.write("AI's Response:")
#         st.write(response)

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import os
# import chainlit as cl
# from langchain import HuggingFaceHub, PromptTemplate, LLMChain

# # Define your AI assistant setup and configurations here
# os.environ['API_KEY'] = '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'
# model_id = 'tiiuae/falcon-7b-instruct'
# falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],
#                             repo_id=model_id,
#                             model_kwargs={"temperature": 0.8, "max_new_tokens": 2000})
# template = """
# You are an AI assistant that provides helpful answers to user queries.
# {question}
# """

# prompt = PromptTemplate(template=template, input_variables=['question'])

# falcon_chain = LLMChain(llm=falcon_llm,
#                         prompt=prompt,
#                         verbose=True)

# # Define the Streamlit app
# def main():
#     st.title("Conversational AI Assistant")
#     st.sidebar.title("Chat History")

#     # Initialize chat history as an empty list
#     chat_history = []

#     # Create an input field for the user to enter their message
#     user_message = st.text_input("You:", key="user_input")

#     # Create a button to send the message
#     if st.button("Send"):
#         # Add the user's message to the chat history
#         chat_history.append(("You", user_message))

#         # Use the AI assistant to generate a response
#         ai_response = falcon_chain.run(user_message)
        
#         # Add the AI's response to the chat history
#         chat_history.append(("AI", ai_response))

#     # Display the chat history
#     for sender, message in chat_history:
#         if sender == "You":
#             st.sidebar.write(sender + ": " + message)
#         else:
#             st.sidebar.write(sender + ": " + message)

# if __name__ == "__main__":
#     main()

#------------------------------------

# import streamlit as st
# import os
# import chainlit as cl
# from langchain import HuggingFaceHub, PromptTemplate, LLMChain

# # Define your AI assistant setup and configurations here
# os.environ['API_KEY'] = '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'
# model_id = 'tiiuae/falcon-7b-instruct'
# falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],
#                             repo_id=model_id,
#                             model_kwargs={"temperature": 0.8, "max_new_tokens": 2000})
# template = """
# You are an AI assistant that provides helpful answers to user queries.
# {conversation}
# """

# prompt = PromptTemplate(template=template, input_variables=['conversation'])

# falcon_chain = LLMChain(llm=falcon_llm,
#                         prompt=prompt,
#                         verbose=True)

# # Define the Streamlit app
# def main():
#     st.title("AI Assistant")
    
#     # Initialize conversation history
#     conversation_history = []

#     # Create a loop for conversation
#     while True:
#         # Create a unique key for the input field
#         user_input_key = f"user_input_{len(conversation_history)}"
        
#         # Create an input field for the user to enter their message
#         user_message = st.text_input("You:", key=user_input_key)

#         # Break the loop if the user's message is empty
#         if not user_message:
#             break
        
#         # Add user's message to conversation history
#         conversation_history.append("You: " + user_message)

#         # Combine conversation history to use as input for the AI assistant
#         conversation_input = "\n".join(conversation_history)

#         # Use your AI assistant to generate a response based on the conversation
#         response = falcon_chain.run(conversation_input)
        
#         # Add AI's response to conversation history
#         conversation_history.append("AI: " + response)

#         # Display the conversation history
#         st.text("\n".join(conversation_history))

# if __name__ == "__main__":
#     main()

###----------------------------------

# import streamlit as st
# import os
# import chainlit as cl
# from langchain import HuggingFaceHub, PromptTemplate, LLMChain

# # Define your AI assistant setup and configurations here
# os.environ['API_KEY'] = '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'
# model_id = 'tiiuae/falcon-7b-instruct'
# falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],
#                             repo_id=model_id,
#                             model_kwargs={"temperature": 0.8, "max_new_tokens": 2000})
# template = """
# You are an AI assistant that provides helpful answers to user queries.
# {conversation}
# """

# prompt = PromptTemplate(template=template, input_variables=['conversation'])

# falcon_chain = LLMChain(llm=falcon_llm,
#                         prompt=prompt,
#                         verbose=True)

# # Define the Streamlit app
# def main():
#     st.title("AI Assistant")
    
#     # Initialize conversation history
#     conversation_history = []

#     # Create a loop for conversation
#     while True:
#         # Create a unique key for the input field
#         user_input_key = f"user_input_{len(conversation_history)}"
        
#         # Create an input field for the user to enter their message
#         user_message = st.text_input("Your message:", key=user_input_key)

#         # Break the loop if the user's message is empty
#         if not user_message:
#             break
        
#         # Add user's message to conversation history
#         conversation_history.append(("User", user_message))

#         # Combine conversation history to use as input for the AI assistant
#         conversation_input = "\n".join([f"{author}: {message}" for author, message in conversation_history])

#         # Use your AI assistant to generate a response based on the conversation
#         response = falcon_chain.run(conversation_input)
        
#         # Add AI's response to conversation history
#         conversation_history.append(("AI", response))

#         # Display the conversation history
#         display_conversation(conversation_history)

# def display_conversation(conversation_history):
#     st.markdown("---")
#     for author, message in conversation_history:
#         if author == "AI":
#             st.markdown(f"<p style='text-align:left;color:blue;'>AI: {message}</p>", unsafe_allow_html=True)
#         else:
#             st.markdown(f"<p style='text-align:right;color:green;'>You: {message}</p>", unsafe_allow_html=True)
#     st.markdown("---")

# if __name__ == "__main__":
#     main()

#=============================================================
# import streamlit as st
# import os
# import chainlit as cl
# from langchain import HuggingFaceHub, PromptTemplate, LLMChain

# # Define your AI assistant setup and configurations here
# os.environ['API_KEY'] = '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'
# model_id = 'tiiuae/falcon-7b-instruct'
# falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],
#                             repo_id=model_id,
#                             model_kwargs={"temperature": 0.8, "max_new_tokens": 2000})
# template = """
# You are an AI assistant that provides helpful answers to user queries.
# {conversation}
# """

# prompt = PromptTemplate(template=template, input_variables=['conversation'])

# falcon_chain = LLMChain(llm=falcon_llm,
#                         prompt=prompt,
#                         verbose=True)

# # Define the Streamlit app
# def main():
#     st.title("AI Assistant")
    
#     # Initialize conversation history as a list
#     conversation_history = st.session_state.get("conversation_history", [])

#     # Create an input box at the bottom for user's message
#     user_message = st.text_input("Your message:")

#     # If the user's message is not empty, process it
#     if user_message:
#         # Add user's message to conversation history
#         conversation_history.append(("User", user_message))

#         # Combine conversation history to use as input for the AI assistant
#         conversation_input = "\n".join([f"{author}: {message}" for author, message in conversation_history])

#         # Use your AI assistant to generate a response based on the conversation
#         response = falcon_chain.run(conversation_input)
        
#         # Add AI's response to conversation history
#         conversation_history.append(("AI", response))

#         # Store the updated conversation history in session state
#         st.session_state.conversation_history = conversation_history

#     # Display the conversation history
#     display_conversation(conversation_history)

# def display_conversation(conversation_history):
#     st.markdown("<style>.message-container { display: flex; flex-direction: column; padding: 16px; }</style>", unsafe_allow_html=True)
#     st.markdown("<style>.user-message { align-self: flex-end; background-color: green; padding: 8px; border-radius: 8px; margin: 4px; }</style>", unsafe_allow_html=True)
#     st.markdown("<style>.ai-message { align-self: flex-start; background-color: black; padding: 8px; border-radius: 8px; margin: 4px; }</style>", unsafe_allow_html=True)
    
#     st.markdown("<div class='message-container'>", unsafe_allow_html=True)
    
#     for author, message in conversation_history:
#         if author == "AI":
#             st.markdown(f"<div class='ai-message'>{message}</div>", unsafe_allow_html=True)
#         else:
#             st.markdown(f"<div class='user-message'>{message}</div>", unsafe_allow_html=True)
    
#     st.markdown("</div>", unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()



import streamlit as st
import os
from langchain import HuggingFaceHub, PromptTemplate, LLMChain

# Define your AI assistant setup and configurations here
os.environ['API_KEY'] = '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'
model_id = 'tiiuae/falcon-7b-instruct'
falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],
                            repo_id=model_id,
                            model_kwargs={"temperature": 0.8, "max_new_tokens": 2000})
template = """
You are an AI assistant that provides helpful answers to user queries.
{conversation}
"""

prompt = PromptTemplate(template=template, input_variables=['conversation'])

falcon_chain = LLMChain(llm=falcon_llm,
                        prompt=prompt,
                        verbose=True)

# Define the Streamlit app
def main():
    st.title("Mouli's AI Assistant")
    
    # Initialize conversation history as a list
    conversation_history = st.session_state.get("conversation_history", [])

    # Create an input box at the bottom for user's message
    user_message = st.text_input("Your message:")

    # If the user's message is not empty, process it
    if user_message:
        # Add user's message to conversation history
        conversation_history.append(("User", user_message))
        print(conversation_history)

        # Combine conversation history to use as input for the AI assistant
        conversation_input = "\n".join([f"{author}: {message}" for author, message in conversation_history])

        # Use your AI assistant to generate a response based on the conversation
        response = falcon_chain.run(conversation_input)
        
        # Add AI's response to conversation history
        conversation_history.append(("AI", response))

        # Store the updated conversation history in session state
        st.session_state.conversation_history = conversation_history

    # Display the conversation history
    display_conversation(conversation_history)

def display_conversation(conversation_history):
    st.markdown("<style>.message-container { display: flex; flex-direction: row; padding: 16px; }</style>", unsafe_allow_html=True)
    st.markdown("<style>.user-message { align: left; background-color: green; padding: 8px; border-radius: 8px; margin: 4px; }</style>", unsafe_allow_html=True)
    st.markdown("<style>.ai-message { align: right; background-color: black; padding: 8px; border-radius: 8px; margin: 4px; }</style>", unsafe_allow_html=True)
    
    st.markdown("<div class='message-container'>", unsafe_allow_html=True)
    
    for author, message in conversation_history:
        if author == "AI":
            st.markdown(f"<div class='ai-message'>{message}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='user-message'>{message}</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
