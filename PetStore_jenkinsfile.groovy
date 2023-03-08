#!/usr/bin/env groovy
node {
    stage('Preparation') {
        checkout scm
    }
    stage('Who am i?') {
        echo "This job was triggered by a Git push to branch: ${env.BRANCH_NAME}"
    }
}