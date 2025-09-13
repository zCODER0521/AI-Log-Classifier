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
