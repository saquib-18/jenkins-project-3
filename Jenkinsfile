pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/jenkins-project-3.git'
            }
        }

        stage('Parallel Checks') {

            parallel {

                stage('Frontend Check') {
                    steps {
                        bat '"C:/Users/User/AppData/Local/Programs/Python/Python314/python.exe" frontend_check.py'
                    }
                }

                stage('Backend Check') {
                    steps {
                        bat '"C:/Users/User/AppData/Local/Programs/Python/Python314/python.exe" backend_check.py'
                    }
                }
            }
        }

        stage('Summary') {
            steps {
                echo 'Student input validation and examination evaluation checks completed.'
                echo 'Both parallel checks passed successfully.'
            }
        }
    }

    post {
        success {
            echo 'Project 3 completed successfully.'
        }

        failure {
            echo 'Project 3 failed.'
        }
    }
}
