# 🤖 AI Log Classifier

An intelligent log classification system that automatically categorizes log messages using multiple machine learning approaches including BERT embeddings, regex patterns, and clustering techniques.

---

![Classification Result](Screenshots/Classification%20result.png)

---

## 🚀 Features

- **Multi-Modal Classification**: Combines regex patterns, BERT embeddings, and clustering for accurate log categorization
- **RESTful API**: Easy-to-use FastAPI endpoint for real-time log classification
- **Comprehensive Training**: Jupyter notebook with detailed analysis and model training
- **Multiple Log Sources**: Supports various systems including ModernCRM, AnalyticsEngine, ModernHR, BillingSystem, ThirdPartyAPI, and LegacyCRM
- **Scalable Architecture**: Modular design with separate processors for different classification methods

---

## 📊 Supported Log Categories

- **HTTP Status**: Web server status codes and responses
- **Critical Error**: System-critical failures requiring immediate attention
- **Security Alert**: Authentication and authorization issues
- **Error**: General application errors (data replication, shard failures)
- **System Notification**: Routine system events (backups, updates, reboots)
- **Resource Usage**: System resource monitoring and alerts
- **User Action**: User activities (login/logout, account creation)
- **Workflow Error**: Process and workflow-related issues
- **Deprecation Warning**: Legacy system warnings

---

## 🏗️ Architecture

```
training/
├── bert_processor.py      # BERT-based classification
├── classification.py      # Main classification logic
├── llm_processor.py       # LLM integration
├── regex_processor.py     # Pattern-based classification
├── server.py             # FastAPI server
├── training.ipynb        # Model training and analysis
└── dataset/
    └── synthetic_logs.csv # Training dataset
```
## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/zCODER0521/AI-Log-Classifier.git
cd AI-Log-Classifier
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
# Create .env file (ensure it's in .gitignore)
GROQ_API_KEY=your_groq_api_key_here
```

## 🚀 Usage

### API Server

Start the FastAPI server:

```bash
cd training
python server.py
```

The API will be available at `http://localhost:8000`

### API Endpoint

**POST `/classify/`**

Upload a CSV file with log data for classification.

**Required CSV format:**
- `source`: Log source system
- `log_message`: The actual log message to classify


**Example using curl:**
```bash
curl -X POST "http://localhost:8000/classify/" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@your_logs.csv"
```

![Postman Response](Screenshots/Postman%20response.png)

**Response:**
Returns a CSV file with the original data plus a `target_label` column containing the classification results.
