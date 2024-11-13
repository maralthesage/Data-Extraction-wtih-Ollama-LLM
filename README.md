# Product Attribute Extraction with Large Language Models (LLMs)

This project leverages AI, specifically large language models (LLMs), to extract product attributes from unstructured product description text and structure them into CSV tables. The resulting structured data can be used for further analysis, inventory management, or enhanced e-commerce listings.

## Table of Contents
- [Overview](#overview)
- [Technical Approach](#technical-approach)
- [Data Structure](#data-structure)
- [Examples](#examples)


## Overview
The purpose of this project is to automate the extraction and structuring of product information from descriptive text. Given the diverse formats of product descriptions, traditional methods can struggle to consistently retrieve information. By using LLMs, this project efficiently identifies and extracts specific attributes (e.g., color, size, material, brand) and organizes them into structured CSV files.

## Technical Approach

This project is based on techniques in the fields of **Natural Language Processing (NLP)** and **Information Extraction (IE)**. Here’s a breakdown of the main technical components:

### 1. Information Extraction (IE)
   The primary task is to perform information extraction, identifying and structuring specific attributes (e.g., product color, size, brand) from unstructured text. This involves:
   - **Named Entity Recognition (NER)**: Recognizing important entities within the text.
   - **Attribute Extraction**: Identifying key product features and their corresponding values.

### 2. Text Mining
   Text mining is applied to analyze the product descriptions and detect patterns or frequently mentioned terms. Although the main focus here is structured extraction rather than exploratory analysis, text mining principles are still relevant.

### 3. Data Structuring and Transformation
   Once attributes are extracted, they are formatted into CSV tables. This stage involves data transformation, ensuring the extracted information is clean and structured properly.

### 4. Natural Language Processing (NLP)
   Leveraging large language models (LLMs) for natural language understanding is a key component of this project. The LLMs are fine-tuned to understand product-related terms and structure data based on patterns in human language.

## Data Structure

The extracted data is structured into a CSV format with each product in one row and various product attributes in the columns. For each Product category (Warengruppe) we set a different set of attributes suitable for that Warengruppe.


## Examples

### Example Input
Product description:

`"This KitchenAid Mixer is available in red, made of stainless steel, and has a 5-quart capacity."`


### Example Output
| ProductID | Color        | Material        |
|-----------|--------------|-----------------|
| 001       | Blue         | Steel           |
| 002       | Red          | Plastik         |
| 003       | Green        | Glass           |

