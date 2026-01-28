pipeline
{
  agent any
  environment
  {
    image_name="darshu262003/newapp"
    doc_credentials=credentials('dockerid')
  }
  stages
  {
    stage('checkout')
    {
      steps{
        git url:"https://github.com/Darshan262003/pythonapp.git",
        branch:"main"
       
      }
      
    }
    stage('build'){
      steps{
        script{
          dockerimg=docker.build("${image_name}:latest")
        }
      }
    }
    stage('push'){
      steps{
        script{
          docker.withRegsitry("https://index.docker.io/v1","dockerid"){
            dockerimg.push()
          }
          
        }
      }
    }
  }
}
