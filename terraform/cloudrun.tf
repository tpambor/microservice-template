data "google_iam_policy" "default" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers"
    ]
  }
}

resource "google_cloud_run_v2_service" "default" {
  name     = "cloudrun-service"
  location = local.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      name = "cloudrun"
      image = "${data.google_artifact_registry_repository.default.location}-docker.pkg.dev/${data.google_artifact_registry_repository.default.project}/${data.google_artifact_registry_repository.default.repository_id}/test:latest"
    }
  }

  lifecycle {
    ignore_changes = [
      client,
      client_version,
      template[0].containers[0].image
    ] 
  }
}

resource "google_cloud_run_v2_service_iam_policy" "default" {
  project = google_cloud_run_v2_service.default.project
  location = google_cloud_run_v2_service.default.location
  name = google_cloud_run_v2_service.default.name
  policy_data = data.google_iam_policy.default.policy_data
}
