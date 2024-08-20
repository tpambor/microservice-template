terraform {
  required_providers {
    google = {
      version = "~> 5.42.0"
    }
  }
}

provider "google" {
  project = local.project_id
  region  = local.region
}
