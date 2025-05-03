pipeline{
    agent any

    stages {
        stage('Install Dependencies & Run Tests'){
            steps {
                script {
                    sh "pip install -r requirements.txt --break-system"
                    sh "pytest --cov=. --cov-report=xml"
                }
            }
        }
    }
}