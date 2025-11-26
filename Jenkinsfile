pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        script {
          if (isUnix()) {
            sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt'
          } else {
            
            bat 'python -m venv venv && venv\\Scripts\\python -m pip install -r requirements.txt'
          }
        }
      }
    }
    stage('Test') {
      steps {
        script {
          if (isUnix()) {
            sh '. venv/bin/activate && pytest -q'
          } else {
            bat 'venv\\Scripts\\python -m pytest -q'
          }
        }
      }
    }
  }
}
