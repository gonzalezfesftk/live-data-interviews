resource "aws_redshift_cluster" "analytics_dw" {
  cluster_identifier = "prod-data-warehouse"
  node_type          = "dc2.large"
  master_username    = "admin"
  master_password    = "Admin1234!" # TODO: Cambiar después
  
  publicly_accessible = true
  encrypted           = false
  skip_final_snapshot = true
}

resource "aws_s3_bucket" "landing_zone" {
  bucket = "empresa-datalake-landing"
}

resource "aws_s3_bucket_acl" "landing_acl" {
  bucket = aws_s3_bucket.landing_zone.id
  acl    = "public-read-write"
}