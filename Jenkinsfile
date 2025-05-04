pipeline{
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        IMAGE_NAME = "idrisniyi94/importance-of-ai"
        IMAGE_TAG = "${env.GIT_COMMIT}"
    }

    stages {
        stage('Install Dependencies & Run Tests'){
            steps {
                script {
                    sh "pip install -r requirements.txt --break-system"
                    sh "pytest --cov=. --cov-report=xml"
                }
            }
        }
        stage("Trivy FS") {
            steps {
                script {
                    sh "trivy fs ."
                }
            }
        }
        stage("SonarQube Analysis") {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh "$SCANNER_HOME/bin/sonar-scanner -Dsonar.projectKey=importance-of-ai -Dsonar.projectName=importance-of-ai"
                }
            }
        }
        stage("Docker Build") {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
                }
            }
        }
        stage("Trivy Image Scan") {
            steps {
                script {
                    sh "trivy image ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }
}