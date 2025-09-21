#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 17:06:51 2025
@author: ernestmugambi
"""
from google import genai
import os
from pydantic import BaseModel, Field
#import json
#from IPython.display import display, Markdown
import pandas as pd

PROJECT_ID = "url_detection"  # @param {type: "string", placeholder: "[your-project-id]", isTemplate: true}
if not PROJECT_ID or PROJECT_ID == "url_detection":
    PROJECT_ID = str(os.environ.get("GOOGLE_CLOUD_PROJECT"))

LOCATION = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")
client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
MODEL_ID = "gemini-2.0-flash-001"  # @param {type: "string"}
client = genai.Client(api_key="")

class Output(BaseModel):
    """ output of url detector """
    url: str = Field(..., description="The URL being analyzed.")
    explanation: str = Field(..., description="A concise explanation of the analysis.")
    verdict: str = Field(..., description="The final verdict ('Benign', 'Phishing').")
    

def classify_url(url):
  """
  Classifies a URL as benign or phishing using the Gemini model.
  Args:
    url: The URL to classify.
  Returns:
    A string containing the explanation and verdict from the Gemini model.
  """
  prompt = f"""Consider whether the URL seems benign or phishing. provide a maximum of 20 words explanation and a verdict which can only have two choices - benign/phishing.
Extract the information and put it in a json with columns url, explanation,verdict
Q: http://scholar.google.com.pk/citations?user=IkvxoFIAAAAJ&hl=en
Example:
Explanation: The subdomain of this URL is a well-known and reputable internet entity, Google Scholar.
Verdict: Benign

Now, classify the following URL as benign or phishing and explain:
Q: {url}
"""

  response = client.models.generate_content(
      model="gemini-2.0-flash",
      contents=prompt,
      config={
        "response_mime_type": "application/json",
        "response_schema": list[Output],
        },
  )
  return response

# Example usage:
def detect_url(url):
    #url_to_check = "http://marlianstv.com/loan/office365/"
    url_to_check = url
    result = classify_url(url_to_check)
    #print(result.parsed)
    results = result.parsed
    df = pd.DataFrame([r.model_dump() for r in results])
    return df

# examples of URLs for testing the LLM prompting efficacy
url_list = ["http://marlianstv.com/loan/office365/",
"https://www.google.com","http://www.rt.com/tags/football/",
"https://drfone.wondershare.net/ad/",
"https://reconciliation.americanexpress.com/",
"http://scholar.google.com.ua/citations?user=r7GEXWwAAAAJ&hl=ru",
"https://pizza.dominos.com/missouri/hollister/",
"https://www.youtube.com/premium",
"http://www.dictionary.com/browse/lan",
"http://allrecipes.com/Recipe/Midwest-Salisbury-Steak/Detail.aspx?soid=recs_recipe_9",
"http://marlianstv.com/loan/office365/",
"http://fb.manage-pages.com/,https://www.amazon.com",
"https://www.amazоn.com"]

def run_urls(urls):
    url_list = []
    for i in urls:
        url_list.append(detect_url(i))
    combined_url_df = pd.concat(url_list, ignore_index=True)
    return combined_url_df

def main():
    llm_output = run_urls(url_list)
    """
    Example of output from running an LLM search of a URL to determine if its benign or phishing-like
    """
    print('###########################################################################################')
    print(llm_output.loc[0]['url'])
    print(llm_output.loc[0]['explanation'])
    print(llm_output.loc[0]['verdict'])
    
if __name__ == "__main__":
    main()
