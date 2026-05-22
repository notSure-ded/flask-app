pipeline {
    agent any

    environment {
        REGISTRY = "dudacr2026xyz.azurecr.io"
        IMAGE = "flask-app"
        TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Clone App Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/notSure-ded/flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $REGISTRY/$IMAGE:$TAG .'
            }
        }

        stage('ACR Login') {
            steps {
                sh 'az acr login --name dudacr2026xyz'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $REGISTRY/$IMAGE:$TAG'
            }
        }

        stage('Clone GitOps Repo') {
            steps {
                sh '''
                git clone https://github.com/notSure-ded/gitOps.git
                '''
            }
        }

        stage('Update Deployment File') {
            steps {
                sh '''
                sed -i "s|image:.*|image: $REGISTRY/$IMAGE:$TAG|g" gitOps/deployment.yaml
                '''
            }
        }

        stage('Push Updated Manifest') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'github-creds',
                    usernameVariable: 'GIT_USER',
                    passwordVariable: 'GIT_PASS'
                )]) {

                    sh '''
                    cd gitOps

                    git config user.email "jenkins@example.com"
                    git config user.name "jenkins"

                    git add .
                    git commit -m "Updated image to $TAG" || echo "No changes"

                    git push https://$GIT_USER:$GIT_PASS@github.com/notSure-ded/gitOps.git HEAD:main
                    '''
                }
            }
        }
    }
}
