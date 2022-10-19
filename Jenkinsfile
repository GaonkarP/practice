pipeline {
    agent {
        label 'linuxP'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'                
            }
        }
        stage('Test') {
            steps {script{
                echo 'Testing..'
                if(isUnix()){
                    echo 'Unix Agent..'
                    sh label: 'Build', returnStatus: true, script: 'python python_scripts/day_detail.py'
                }else{
                    bat label: 'Build', returnStatus: true, script: 'python python_scripts/day_detail.py'
                }
            }}
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
