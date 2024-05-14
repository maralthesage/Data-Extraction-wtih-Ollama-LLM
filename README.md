## Data Extraction from text using Ollama and Mixtral 7x8b

This is an effort to extract product properties from a list of product descriptions that are in German language and are very irregular to use Regex on.
Mixtral 7x8b (Opensource) using Ollama did a pretty neat job in a relatively short time. Of course, the result got refined with the right instructions in the prompt as well the JSON example output given to the model. 

Mistral/Mixtral is powerful with Structured data extraction in German. I first wanted to use GPT3 or 4 for more refined results, but given the number of products needed property extraction, using Mixtral 7x8b was an efficient choice.