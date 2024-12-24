# Llama2

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain import PromptTemplate
from langchain import LLMChain
from sentence_transformers import SentenceTransformer, util


llm = CTransformers(model=   , 
                            model_type='llama', 
                            config={'max_new_tokens': max_new_tokens,
                            'temperature': temperature,
                            "top_p":top_p,
                            "stream": True}, callbacks=[StreamingStdOutCallbackHandler()],)

template = f"""Question: {{question}}
            Answer: """

# with langchain
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

input_text = input("Enter a prompt")

modified_story = llm_chain.run(input_text)


# Qwen

from transformers import AutoModelForCausalLM, AutoTokenizer
from auto_gptq import AutoGPTQForCausalLM
from transformers import AutoTokenizer
from transformers import GenerationConfig

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, bf16=True).eval()
# model = AutoGPTQForCausalLM.from_quantized("Qwen/Qwen-7B-Chat-Int4", device_map="auto", trust_remote_code=True, use_safetensors=True).eval()

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)
Input = input("enter")
response, history = model.chat(tokenizer, Input, history=None)  

return response, history

