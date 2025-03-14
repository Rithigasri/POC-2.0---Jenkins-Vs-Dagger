pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-app"
        CONTAINER_NAME = "my-container"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Rithigasri/POC-2.0---Jenkins-Vs-Dagger'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8080:8080 --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }

        stage('Check Running Container') {
            steps {
                sh 'docker ps -a'
            }
        }

        stage('Test Deployment') {
            steps {
                sh 'curl -f http://localhost:8080 || exit 1'
            }
        }
    }
}
