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
		sh 'echo " testing completed"'
	}
	}

	stage('Deploy')
	{
	steps {
		echo "deploying the application"
		sh 'echo "deploying completed"'
	}
	}
}
}
