data "google_artifact_registry_repository" "default" {
  location      = local.region
  repository_id = local.registry_id
}
