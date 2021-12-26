properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
    checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/amichaizelig/devops1411.git']]])    
    }
    stage("show files"){
        bat "dir"
        bat "python 335.py
    }
}
