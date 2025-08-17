# Docker Model Runner LLM App

## Overview
A streamlined chat application that leverages Docker Model Runner to serve Large Language Models (LLMs) through a modern Streamlit interface. This project demonstrates containerized LLM deployment with a user-friendly web interface.

## Features
- 🤖 Modern chat interface with message history
- ⚡️ Real-time LLM responses
- 🔄 Clear chat functionality
- 🛡️ Error handling and loading states
- 🐳 Containerized deployment
- 🏥 Health monitoring

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Docker Model Runner
- **API**: OpenAI-compatible endpoints
- **Containerization**: Docker & Docker Compose
- **Language**: Python 3.11
- **Key Dependencies**: OpenAI SDK, python-dotenv

## Project Structure
```
DMR/
├── app/
│   ├── Dockerfile          # Frontend container configuration
│   ├── main.py            # Streamlit chat interface
│   └── requirements.txt    # Python dependencies
├── docker-compose.yml     # Service orchestration
├── backend.env           # Environment configuration
└── README.md            # Project documentation
```

## Setup

### Prerequisites
- Docker Desktop
- Git

### Quick Start
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd DMR
   ```

2. **Configure environment**
   Create `backend.env` with:
   ```env
   BASE_URL=http://host.docker.internal:12434/engines/llama.cpp/v1/
   API_KEY=your_api_key
   MODEL=your_model_name
   LLM_MODEL_NAME=ai/smollm2:latest
   ```

3. **Build and run**
   ```bash
   docker compose up --build
   ```

4. **Access the application**
   - Open [http://localhost:8501](http://localhost:8501)
   - Start chatting!

## Docker Configuration

### Services

#### Frontend (Streamlit App)
- Built from Python 3.11-slim
- Exposes port 8501
- Includes health checking
- Dependencies managed via requirements.txt

#### LLM Service
- Uses Docker Model Runner
- Default model: ai/smollm2:latest
- Configurable via environment variables

### Networking
- Isolated network for services
- Bridge driver for container communication
- Internal service discovery

## Development

### Local Setup
1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Mac
   ```

2. **Install dependencies**
   ```bash
   pip install -r app/requirements.txt
   ```

3. **Run locally**
   ```bash
   streamlit run app/main.py
   ```

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
