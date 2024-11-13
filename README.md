<span style="color: #FF5733; font-size: 2em;"># Product Attribute Extraction with Large Language Models (LLMs)</span>

This project leverages AI, specifically large language models (LLMs), to extract product attributes from unstructured product description text and structure them into CSV tables. The resulting structured data can be used for further analysis, inventory management, or enhanced e-commerce listings.

## <span style="color: #FF5733;">Table of Contents</span>
- [Overview](#overview)
- [Technical Approach](#technical-approach)
- [Data Structure](#data-structure)
- [Examples](#examples)


## <span style="color: #FF4500;">Overview</span>
The purpose of this project is to automate the extraction and structuring of product information from descriptive text. Given the diverse formats of product descriptions, traditional methods can struggle to consistently retrieve information. By using LLMs, this project efficiently identifies and extracts specific attributes (e.g., color, size, material, brand) and organizes them into structured CSV files.

## <span style="color: #FF5733;">Technical Approach</span>

This project is based on techniques in the fields of **Natural Language Processing (NLP)** and **Information Extraction (IE)**. Here’s a breakdown of the main technical components:

### <span style="color: #FF4500;">1. Information Extraction (IE)</span>
   The primary task is to perform information extraction, identifying and structuring specific attributes (e.g., product color, size, brand) from unstructured text. This involves:
   - **Named Entity Recognition (NER)**: Recognizing important entities within the text.
   - **Attribute Extraction**: Identifying key product features and their corresponding values.

### <span style="color: #FF4500;">2. Text Mining</span>
   Text mining is applied to analyze the product descriptions and detect patterns or frequently mentioned terms. Although the main focus here is structured extraction rather than exploratory analysis, text mining principles are still relevant.

### <span style="color: #FF4500;">3. Data Structuring and Transformation</span>
   Once attributes are extracted, they are formatted into CSV tables. This stage involves data transformation, ensuring the extracted information is clean and structured properly.

### <span style="color: #FF4500;">4. Natural Language Processing (NLP)</span>
   Leveraging large language models (LLMs) for natural language understanding is a key component of this project. The LLMs are fine-tuned to understand product-related terms and structure data based on patterns in human language.

## <span style="color: #FF5733;">Data Structure</span>
The extracted data is structured into a CSV format with each product in one row and various product attributes in the columns. For each Product category (Warengruppe) we set a different set of attributes suitable for that Warengruppe.


<span style="color: #FF4500;">Examples</span>

### Example Input
Product description:

`"This KitchenAid Mixer is available in red, made of stainless steel, and has a 5-quart capacity."`


### Example Output
| ProductID | Color        | Material        |
|-----------|--------------|-----------------|
| 001       | Blue         | Steel           |
| 002       | Red          | Plastik         |
| 003       | Green        | Glass           |

