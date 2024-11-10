import embeddings.Util.embeddingUtil
import llm.llmprocessor
import json

class Query_Handler :
    
    @staticmethod
    def process_query(query):

        
        response = llm.llmprocessor.getLLMPromt(query)
        
        print(response)
        
        query1 = query
        query2 = query
        
        try:
            # Code that might raise an exception
            
            json_data = json.loads(response)
            #json_data = json.loads(response.content)
            query1 = json_data['query1']
            query2 = json_data['query2']
            print("query1-",query1)
            print("q2-",query2)
            
            
        except Exception as e:
            
            print("Exception",e)    
        
                
        
        
        
        
        relevant_chunks1 = embeddings.Util.embeddingUtil.fetch_relevant_chunks(query1,"doc1")
        #print("\nTop relevant chunks:")
        context_text1 = "-------------\n---------------------".join([doc.page_content for doc in relevant_chunks1])
        
        print(context_text1)
        
        relevant_chunks2 = embeddings.Util.embeddingUtil.fetch_relevant_chunks(query2,"doc2")
        context_text2 = "----------\n------------------------".join([doc.page_content for doc in relevant_chunks2])
        print(context_text2)
        
       
        context_text = context_text1 + context_text2
        #print(context_text)
        
        
        processed_response = llm.llmprocessor.getLLMResponse(context_text,query)
        
        
        
        return  processed_response
    