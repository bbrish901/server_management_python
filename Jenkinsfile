pipeline {
agent any
stages {
	stage('Build') {
	parallel {
		stage('Build') {
		steps {
			sh 'echo "building the repo"'
		}
		}
	}
	}

	stage('Test') {
	steps {
		sh 'python3 user_api.py'
	}
	}

	stage('Deploy')
	{
	steps {
		echo "deploying the application"
		sh 'python3 user_api.py'
	}
	}
}
}
