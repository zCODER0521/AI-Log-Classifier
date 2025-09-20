# 🤖 AI Log Classifier

An intelligent log classification system that automatically categorizes log messages using multiple machine learning approaches including BERT embeddings, regex patterns, and clustering techniques.

## 🎯 Live Demo

### Classification Results in Action
See how our AI system accurately classifies different types of log messages with high precision and confidence scores.

![Classification Result](Screenshots/Classification%20result.png)
*AI-powered log classification in action: automatically categorizing logs from multiple systems (ModernCRM, AnalyticsEngine, ModernHR) into Security Alerts, HTTP Status, Errors, System Notifications, and User Actions with 99% accuracy*

## 🚀 Features

- **Multi-Modal Classification**: Combines regex patterns, BERT embeddings, and clustering for accurate log categorization
- **RESTful API**: Easy-to-use FastAPI endpoint for real-time log classification
- **Comprehensive Training**: Jupyter notebook with detailed analysis and model training
- **Multiple Log Sources**: Supports various systems including ModernCRM, AnalyticsEngine, ModernHR, BillingSystem, ThirdPartyAPI, and LegacyCRM
- **Scalable Architecture**: Modular design with separate processors for different classification methods

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
uvicorn server:app --reload
```

The API will be available at `http://localhost:8000`

### 📡 API Testing with Postman

Our FastAPI endpoint provides seamless integration for log classification. Here's how it works in practice:

![Postman Response](Screenshots/Postman%20response.png)
*Postman API testing showing successful file upload and classification response. The API accepts CSV files and returns classified results with target labels for each log entry*

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

**Response:**
Returns a CSV file with the original data plus a `target_label` column containing the classification results.

### Training Notebook

Explore the complete training process and analysis in [`training/training.ipynb`](training/training.ipynb):

- Data exploration and visualization
- DBSCAN clustering analysis
- BERT embedding generation
- Regex pattern classification
- Model training and evaluation
- Performance metrics and validation

## 📈 Model Performance

The trained model achieves excellent classification performance:

- **Accuracy**: 99%
- **Precision**: 0.99 (macro avg)
- **Recall**: 0.99 (macro avg)
- **F1-Score**: 0.99 (macro avg)

## 🔧 Technical Details

### Classification Pipeline

1. **Regex Classification**: Fast pattern-based classification for common log types
2. **BERT Embeddings**: Semantic understanding using sentence-transformers
3. **Clustering**: DBSCAN clustering for pattern discovery
4. **Machine Learning**: Logistic Regression on filtered embeddings

### Key Components

- **BERT Model**: `all-MiniLM-L6-v2` for generating sentence embeddings
- **Clustering**: DBSCAN with eps=0.5, min_samples=5
- **Classification**: LogisticRegression with max_iter=1000
- **Model Storage**: Joblib serialization in [`models/log_classifier.joblib`](models/log_classifier.joblib)

## 📁 Project Structure

```
AI-Log-Classifier/
├── .env                          # Environment variables (not in repo)
├── .gitignore                    # Git ignore rules
├── models/
│   └── log_classifier.joblib     # Trained model
├── Resources/
│   ├── output.csv               # Classification results
│   └── test.csv                 # Test data
├── Screenshots/
│   ├── Classification result.png
│   └── Postman response.png
└── training/
    ├── bert_processor.py
    ├── classification.py
    ├── llm_processor.py
    ├── regex_processor.py
    ├── server.py
    ├── training.ipynb
    └── dataset/
        └── synthetic_logs.csv
```

## 🔒 Security

- Environment variables are properly configured in `.env` (excluded from repository)
- API endpoints include proper error handling and validation
- File upload restrictions ensure only CSV files are processed

## 📝 Example Log Classifications

| Log Message | Source | Classification |
|-------------|--------|---------------|
| `User User123 logged in.` | ModernHR | User Action |
| `Failed to replicate data for shard 5` | AnalyticsEngine | Error |
| `Backup completed successfully.` | BillingSystem | System Notification |
| `Multiple incorrect login attempts` | ModernCRM | Security Alert |
| `System updated to version 3.9.1` | ThirdPartyAPI | System Notification |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- **Repository**: [https://github.com/zCODER0521/AI-Log-Classifier](https://github.com/zCODER0521/AI-Log-Classifier)
- **API Documentation**: `http://localhost:8000/docs` (when server is running)

---

**Built with ❤️ using FastAPI, BERT, and scikit-learn**