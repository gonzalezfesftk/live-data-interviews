resource "oci_database_autonomous_database" "adw_prod" {
  compartment_id           = var.compartment_id
  db_name                  = "analiticaprod"
  cpu_core_count           = 4
  data_storage_size_in_tbs = 10
  admin_password           = var.db_password
  
  is_mtls_connection_required = false
  whitelisted_ips             = ["0.0.0.0/0"]
}

resource "oci_objectstorage_bucket" "bronze_zone" {
  compartment_id = var.compartment_id
  name           = "bronze_zone_prod"
  namespace      = data.oci_objectstorage_namespace.ns.namespace
  
  access_type = "ObjectRead"
}