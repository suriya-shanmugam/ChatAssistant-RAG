
import google.generativeai as genai
from langchain_groq import ChatGroq


def create_prompt(context, query):
    
    prompt_template = """
    1.You are a helpful assistant. 
    
    2.Give the exact response alone without greetings and other conversation text 
    
    
    {context}
    
    
    
    

    Question:
    {query}

    
    """
    
    # Substitute placeholders in the template
    prompt = prompt_template.format(context=context, query=query)
    return prompt


def getLLMResponse(context_text,user_query):

    final_prompt = create_prompt(context_text, user_query)
    
    
    llm = genai.GenerativeModel('gemini-1.5-flash')
    
    
    response = llm.generate_content([final_prompt])
    
    return response.text
    
    #print(final_prompt)
    '''
    llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    )

    response = llm.invoke(final_prompt)
    
    return response.content
    '''
    
    
    
    


def create_pre_prompt(context1):
    
    prompt_template = """
    
     <Query>  {context1} </Query> 
    
    1.If the above query is comparing something change it fetch query from each.
    
    Example : Input - Compare food insecurity reason between 2023 and 2024
    
    respone -   "query1" : "what is the food insecurity reason in 2023",
                "query2" : "what is the food security reason in 2024"

    2.Give response in JSON with key as query1,query2 and one set is enough
    3. Response should be the JSON text alone no other information
    """

    # Substitute placeholders in the template
    prompt = prompt_template.format(context1=context1)
    return prompt


def getLLMPromt(user_query):

    
    
    #llama model
    
    
    final_prompt = create_pre_prompt(user_query)
    
    
    
    
    
    
    #print(final_prompt)
    '''
    llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    response_format={"type": "json_object"}
    )
    response = llm.invoke(final_prompt)
    return response.content
    '''
    llm = genai.GenerativeModel('gemini-1.5-flash',
                              # Set the `response_mime_type` to output JSON
                              generation_config={"response_mime_type": "application/json"})
    
    
    response = llm.generate_content([final_prompt])

    
    
    return response.text


   