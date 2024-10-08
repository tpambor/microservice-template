variable "gcp_region" {
  type        = string
  default     = "us-central1"
  description = "GCP region"
}

variable "gcp_project_id" {
  type        = string
  description = "GCP project ID"
}

variable "registry_id" {
  type        = string
  default     = "repo"
  description = "Artifact registry ID"
}
