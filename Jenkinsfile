pipeline{
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        IMAGE_NAME = "idrisniyi94/importance-of-ai"
        IMAGE_TAG = "${env.GIT_COMMIT}"
        CONTAINER_NAME = 'lab-server-importance-of-ai'
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
        stage("Stop Old Container") {
            steps {
                script {
                    sh """
                        if [\$(docker ps -a -f name=${CONTAINER_NAME})]; then
                            echo "Stopping and removing existing container: ${CONTAINER_NAME}
                            docker stop ${CONTAINER_NAME}
                            docker rm ${CONTAINER_NAME}
                        else
                            echo "No existing container named ${CONTAINER_NAME} found."
                        fi
                    """
                }
            }
        }
        stage("Run App") {
            steps {
                script {
                    sh "docker run -d --name ${CONTAINER_NAME} -p 3319:5000 -u USER=lab-server --net cloudflared-lab-net ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
            
    }
}