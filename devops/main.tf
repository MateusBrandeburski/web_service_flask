 terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
    region  = "us-west-2"
    access_key = "AKIAW6GNKXBHPVRBIUPF"
    secret_key = "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"
}

resource "aws_instance" "app_server" {
  ami = "ami-0fcf52bcf5db7b003"  
  instance_type = "t2.micro"
  key_name = "iac-sistema-flask"

  tags = {
    Name = "teste AWS 2"
  }
}
