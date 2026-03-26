resource "azurerm_storage_account" "datalake" {
  name                     = "empresadatalakeprod"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = true
  
  allow_nested_items_to_be_public = true
}

output "datalake_access_key" {
  value     = azurerm_storage_account.datalake.primary_access_key
  sensitive = false
}