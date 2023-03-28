import jenkins

# Jenkins server URL and credentials
jenkins_url = 'http://jenkins-server-url'
jenkins_username = 'your-username'
jenkins_password = 'your-password'

# Pipeline job name
pipeline_job_name = 'my-pipeline-job'

# Connect to Jenkins server
jenkins_server = jenkins.Jenkins(jenkins_url, username=jenkins_username, password=jenkins_password)

# Start pipeline build
build_params = {}
jenkins_server.build_job(pipeline_job_name, build_params)
