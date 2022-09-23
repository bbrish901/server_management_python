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
		sh 'pip3 install psycopg2'
		sh 'mkdir python setup.py build_ext --pg-config /path/to/pg_config build ...'
		sh 'python3 user_api.py'
		input(id: "Deploy Gate", message: "Deploy ${params.project_name}?", ok: 'Deploy')
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
