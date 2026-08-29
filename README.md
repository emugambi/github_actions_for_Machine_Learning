# An ML workflow for detecting malicious URLs and improved using LLM AI knowledge - trading off classical ML and LLMs

## Tools used : scikit-learn pipelines, CML, and GitHub actions.

## Using LLMs to Boost Classical Machine Learning URL classification Models.

The work done involves various pieces:
* Showing how an ML algorithm can use open-source data to train a URL detector that is able to distinguish lexically, good URLs from bad ones that are more likely to be vehicles of phishing attacks.
* How an LLM can be interrogated to detect URLs that are more likely to be malicious and offer a cogent explanation of why that is so.
* We show how the classical LLM can benefit from being retrained after incorporating the LLM feedback so that it is better able to improve its detection edge using real-life URLs.

## Features
github action successful worfklow run:
(https://github.com/emugambi/github_actions_for_Machine_Learning/actions/runs/18020216155/job/51275423976)
🎉 Training an Xgboost ML model to perform URL detection
* code/run_Xgboost_trainer.py
* results : see Github Action Pipeline under the step - "Evaluation" and "Training"

🎉 Using an LLM for URL detection use case
* code/url_llm_detector.py
* results : see Github Action Pipeline under the step - "LLM"

🎉 Boosting the Xgboost model using LLM output
* code/run_Xgboost_retrainer.py
* results : see Github Action Pipeline under the step - "Retraining"

🎉Design Doc for this work
* URL Detection Design DOC.md
(https://github.com/emugambi/github_actions_for_Machine_Learning/blob/main/URL%20Detection%20Design%20DOC.md)
* URL Detection_Architecture.pdf
(https://github.com/emugambi/github_actions_for_Machine_Learning/blob/main/URL%20Detection_Architecture.pdf)

🎉 Medium publication that gives in-depth information about the work done and the results
(https://medium.com/@ernestmugambi/using-llms-to-boost-classical-machine-learning-url-classification-models-25369d6051fb)

## Related Things


