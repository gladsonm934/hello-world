pipeline{
  agent any
  stages{
    stage('clone Repo'){
      steps{
        git 'https://github.com/gladsonm934/hello-world.git'
      }
    }
    stage('Build Docker Image'){
      steps{
        script{
          dockerImage = docker.build("hello-world:latest")
        }
      }
    }
    stage('Run Container'){
      steps{
        script{
          dockerImage.run("-p 8085:80")
        }
      }
    }
  }
}
