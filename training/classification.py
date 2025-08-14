from regex_processor import classify_with_regex
from bert_processor import classify_with_bert   
from llm_processor import classify_with_llm
import pandas as pd 
def classify(logs):
    labels=[]
    for source, log_message in logs:
        label=classify_logs(source, log_message)
        labels.append(label) 
    return labels

def classify_logs(source,log_message):
    if source=="LegacyCRM":
        label = classify_with_llm(log_message)
    else:
        label = classify_with_regex(log_message)
        if label is None:
           label = classify_with_bert(log_message)
    return label
def classify_csv(input_file):
    df=pd.read_csv(input_file)
    logs = list(zip(df['source'], df['log_message'])) 
    df['target_label'] = classify(logs)
    output_file = ("Resources/output.csv")
    df.to_csv(output_file, index=False)
  
if __name__ == "__main__":
    classify_csv("Resources/test.csv") 
    # logs = [
    #     ("ModernCRM", "IP 192.168.133.114 blocked due to potential attack"),
    #     ("BillingSystem", "User User 12345 logged in."),
    #     ("AnalyticsEngine", "File data_6957.csv uploaded successfully by user User265."),
    #     ("AnalyticsEngine", "Backup completed successfully."),
    #     ("ModernHR", "GET /v2/54fadb412c4e40cdbaed9335e4c35a9e/servers/detail HTTP/1.1 RCODE  200 len: 1583 time: 0.1878400"),
    #     ("ModernHR", "Admin access escalation detected for user 9429"),
    #     ("LegacyCRM", "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."),
    #     ("LegacyCRM", "Invoice generation process aborted for order ID 8910 due to invalid tax calculation module."),
    # ]
    
    # classifications = classify(logs) 
    # print(classifications)  