URL Detection Design DOC
Design Doc
1. overview
Purpose
Malicious URLs are the sources of [] many cybersecurity attacks which occur by way of phishing that ultimately leads to malware infections. URLs are a fundamental aspect of digital life since most information we interact with on a day to day basis are stored in websites. While there are rules about what a proper URL needs to be crafted and used, there is no solid methodology to determine which Urls can be trusted or not. This work builds an AI/ML program that uses cybersecurity intelligence, historical behavior of client URLs, linguistics aspects of URLs accessed and LLM intelligence to come up with a trust score for a URL that would help alleviate URL based attack.

Problem
Scale: there are billions of URLs
New URLs are being registered all the time
URL IOCs are held by threat intelligence organizations  that are costly and backward-looking
Difficult  to keep track of URLs a client has interacted with before in terms of storage cost and retrieval time
DNS info on a URL is expensive and time-consuming to access and fragmented in nature.
New forms of URL attacks are always being formulated.
Most users have little knowledge or awareness of how to look for tell-tale signs of malicious URLs
Mis-classifications / mis-identification of URL is costly and could threaten businesses.
2. Solution
A self improving AI/ML solution that scores Urls at the time of use. 
Desired outcome
A solution that meets the target goals of every business in terms of reduction or elimination of url originated attacks without severely impacting the business outcomes and minimizing overall costs.
3. Motivations
Every business will always interact with Urls and they will always be a major pathway to cyber attacks. Businesses cannot depend on users to ensure that the Urls they interact with are clean and trustworthy. While businesses always spend time and money to educate users on proper cyber preventions methods, this does not guarantee that cyber attacks, especially the ones that use URLs as the vector of attacks, will be eliminated. The cost of phishing-led cyber attacks could cripple a business by way of loss of critical data, bad publicity and punitive regulatory costs. Most cybersecurity products are generic and are not tailored for every individual business needs.

3.1Success metrics
Detection rates are acceptable to businesses 
False positives are acceptable
Infrastructure costs - access of LLMs, storage + Latency / retrieval rates 
Self learning anf improvement capability 

4. Requirements & constraints

4.1 what’s in-scope and out-of-scope
A cloud url detection system that can provide an instant trust or authenticity score of a URL that is informed by the following sources:
In-scope
Threat intelligence that a client subscribes to
ML decision engine based on the client historical urls stored in a database of choice.
Real-time decisions coming from an LLM engine about the reputation of the url
decisions based on an ML engine built from open source urls held in the public domains
Out-of-scope
Decisions based on DNS registrations about the Url  and domain reputation
 examining the content of webpages for malicious indicators ( bad images or content + dynamic code emulation to see behaviors)
5. Methodology
Machine learning based classifiers will be used on historical datasets to develop an ML engine that determines the trustworthiness of a Url. The ML classifier will use the most reliable algorithms such as Xgboost, Deep Learning and Probabilistic techniques. Also, LLMs will be used to help determine the trustworthiness of a Url based on the prevailing knowledge held in the internet-based domains by searching / prompting an LLM. The LLM will also be used to explain the basis of its decision.

5.1 Problem statement
The goal of this solution is to derive a practical measure of trust tied to a URL that a user intends to access using LLMs, Machine Learning  algorithms  and Databases

5.2 Data
URL / malicious domain data held by public datasets
Phishtank
Kaggle
Client data sets
Threat intelligence sources such as VirusTotal
5.3 Techniques
LLMs (google Gemini), Machine Learning (Xgboost, Deep Learning (PyTorch), Probabilistic techniques, Databases (TBD)

5.4 experimentation and validation
We have carried out experiments using Kaggle malicious Url dataset (https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset) in which our ML classifier achieved F1 score of 0.95 trained on less than 10% of all the data. We have also run some LLM prompt searches and identified areas where LLMs can supplement the ML detections. We have a running CI/CD pipeline that performs re-training based on various prompts. We can also run various tests to ensure the pipeline meets certain conditions. Also, we intend to deploy models once it meets certain performance metrics.

5.5 Human-in-the-loop
Human feedback will be used to improve labelling. LLMs will be used to improve labelling by checking the decisions emanating from the ML decision engines. ML re-training will take place after re-labelling so that the ML 
engine can learn from it. By retraining the ML engine, this will minimize the need and cost of interrogating the LLM.
6. Implementation
6.2 Infra
Embeddings(lanceDB/chromaDB), Docker, Kubernettes, Git, Github actions (CI/CD), Python (Pandas, Scikit Learn, SKOps), gemini(LLM), VS-code, Pytest, Graph or relational DB (TBD)

6.3 performance 
How will your system meet the throughput and latency requirements? Will it scale vertically or horizontally?
It will scale mainly vertically and will depend on 
-number of users and documents
-frequency of searches 
-complexity of queries and logic used
-ML retraining and querying the DB for repeat Urls  should minimize dependence on LLMs and ultimately the latency
-rate limiting based on LLM agent memory can also be used to minimize cost and latency
Horizontally, the system will incorporate distributed architectures in order to meet latency requirements. Various decisions on each Url can be made by querying modules, running concurrently. For instance, the ML detector and the LLM search can all occur at the same time in order to minimize delays.

6.4 Security
All the necessary security with respect to the users and infrastructure will be adhered to.
Various security policies / tools will be used:
Each user can only access the system using valid and strong credentials
The software environment  will be secured using the requisite security technology such as  firewalls etc
All the data pertaining to the user, Url access, time stamps etc will be retained anyway as part of the ML system for retraining purposes and can also be used for future verification purposes.

6.5 data privacy
Customer data will remain within the customer environment maintaining data privacy. All the Machine Learning training will occur in the customer environment too (cloud / on-prem). Only the LLM searches will be exposed. This does not feel like a privacy concern since URLs are not PII and are usually publicly accessible anyway. The identity of whoever is accessing the URL will always be hidden and not shared with anyone except the administrators of the system. All other data retention rules will be followed in compliance with the relevant regulations.

6.6 monitoring & alarms
How will you log events in your system? What metrics will you monitor and how? Will you have alarms if a metric breaches a threshold or something else goes wrong?
-A logging system should be ultimately used to track all events. This can be used by admins in future to restrict/allow access
- Continuous monitoring of the detection engines will take place and a log of various metrics will be taken. System performance metrics e.g latency, detection rates over time, statistical information relating to the training sets such as number and distribution of events, the accuracy of the training model to ensure it meets the threshold. Other CI/CD related tests will be tracked every time a new build is created.
Various logging tools will be used:
MLFlow to track machine learning metrics
Loguru
6.7 Cost
How much will it cost to build and operate your system? Share estimated monthly costs (e.g., EC2 instances, Lambda, etc.)
No estimates yet
6.8 integration points
How will your system integrate with upstream data and downstream users?
Not yet thought through
6.9 Risks & Uncertainties
Risks are the known unknowns; uncertainties are the unknown unknown. What worries you would like others to review?
How good the semantic search  - False Negatives especially. Any sensitive info that goes thru is a big risk
Any PII that is undetected is a big risk and fails GDPR test
7. Appendix
7.1. Alternatives
What alternatives did you consider and exclude? List pros and cons of each alternative and the rationale for your decision.
7.2. Experiment Results
Share any results of offline experiments that you conducted.
7.3. Performance benchmarks
Share any performance benchmarks you ran (e.g., throughput vs. latency vs. instance size/count).
7.4. Milestones & Timeline
What are the key milestones for this system and the estimated timeline?
7.5. Glossary
Define and link to business or technical terms.
7.6. References
Add references that you might have consulted for your methodology.
How AI agents can be used to propagate attacks by accepting user input or their responses
https://www.keysight.com/blogs/en/tech/nwvs/2025/06/26/malicious-url-based-prompt-injection
LLMs are one-shot URL Classifiers and Explainers
https://arxiv.org/html/2409.14306v1

Client-Side Zero-Shot LLM Inference for Comprehensive In-Browser URL Analysis
https://arxiv.org/html/2506.03656v1


