pipeline {
    agent any 

    stages {
        stage('Start Minikube Cluster') {
            steps {
                // Start a 3-node Minikube cluster with the 'none' driver
                sh 'minikube config set memory 768'
                sh 'minikube config set disk-size 5000'
                sh 'minikube start --nodes=3'
            }
        }

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/mohamedsamir907/depi-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("mohamed907/depi-project", ".")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        docker.image('mohamed907/depi-project').push('latest')
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'minikube tunnel' // Start the tunnel 
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
                //sh 'minikube tunnel stop' // Stop the tunnel (optional)
            }
        }

        stage('Test') {
            steps {
                // Run your test suite here.  
                // For example, you can use curl:
                sh 'curl -X GET http://$(minikube ip):80'
            }
        }

        stage('Stop Minikube Cluster') { // Add a stage to stop the cluster
            steps {
                sh 'minikube stop'
            }
        }
    }
}