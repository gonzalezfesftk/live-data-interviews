resource "google_bigquery_dataset" "finanzas" {
  dataset_id  = "datos_financieros_prod"
  description = "Dataset principal de finanzas"
  location    = "US"
}

resource "google_bigquery_dataset_iam_binding" "acceso_abierto" {
  dataset_id = google_bigquery_dataset.finanzas.dataset_id
  role       = "roles/bigquery.dataViewer"
  members    = [
    "allAuthenticatedUsers",
  ]
}

resource "google_storage_bucket" "raw_data" {
  name          = "empresa-raw-data-prod"
  location      = "US"
  force_destroy = true
}