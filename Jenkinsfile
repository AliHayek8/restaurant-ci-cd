pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t restaurant-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop restaurant || true
                docker rm restaurant || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name restaurant restaurant-app'
            }
        }
    }
}
