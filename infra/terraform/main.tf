terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "todoapp" {
  name = "todoapp:latest"
  build {
    context = "../../examples/todoapp"
  }
}

resource "docker_container" "todoapp" {
  name  = "todoapp"
  image = docker_image.todoapp.image_id
  ports {
    internal = 5000
    external = 5000
  }
}
