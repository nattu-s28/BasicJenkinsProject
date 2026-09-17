pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python main.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }
    }

    post {
        always {
            echo 'Jenkins Pipeline Completed'
        }

        success {
            echo 'All stages completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}