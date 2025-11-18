---
name: devops-fundamentals
description: DevOps practices including Docker containerization, Kubernetes orchestration, CI/CD pipelines, and infrastructure automation.
---

# DevOps Fundamentals

## Docker Quick Start

### Dockerfile Example

```dockerfile
FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000
CMD ["node", "server.js"]
```

### Build and Run

```bash
# Build image
docker build -t my-app:1.0 .

# Run container
docker run -p 3000:3000 my-app:1.0

# View logs
docker logs <container_id>

# Stop container
docker stop <container_id>
```

## Kubernetes Deployment

### Basic Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app:1.0
        ports:
        - containerPort: 3000
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
```

### Service Exposure

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
  type: LoadBalancer
```

## GitHub Actions CI/CD

### Simple Pipeline

```yaml
name: Build and Deploy

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'

    - name: Install dependencies
      run: npm install

    - name: Run tests
      run: npm test

    - name: Build
      run: npm run build

    - name: Deploy
      if: github.ref == 'refs/heads/main'
      run: npm run deploy
```

## Infrastructure as Code with Terraform

### Basic EC2 Setup

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.small"

  tags = {
    Name = "web-server"
  }
}

resource "aws_security_group" "web" {
  name = "web-sg"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

## Monitoring with Prometheus and Grafana

### Prometheus Configuration

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
```

## Key Concepts

1. **Container Fundamentals**
2. **Image Management**
3. **Orchestration**
4. **CI/CD Pipelines**
5. **Infrastructure as Code**
6. **Monitoring & Logging**
7. **Security & Secrets Management**