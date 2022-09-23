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
		sh 'python3 test.py'
		input(id: "Deploy Gate", message: "Deploy ${params.project_name}?", ok: 'Deploy')
	}
	}

	stage('Deploy')
	{
	steps {
		echo "deploying the application"
		sh 'python3 test.py'
	}
	}
}
}
