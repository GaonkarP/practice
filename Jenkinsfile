pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                echo 'test'
                sh label: 'Build', returnStatus: true, script: 'pyinstaller python_scripts/day_detail.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Run') {
            steps {
                echo 'Running in test directory....'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
