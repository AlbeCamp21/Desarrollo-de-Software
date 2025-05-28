variable "connection_string_tpl" {
  type    = string
  default = ""
  description = "Cadena de conexión a base de datos si es que aplica."
}

variable "db_user" {
  description = "usuario database"
  type        = string
}

variable "db_password" {
  description = "contraseña database"
  type        = string
  sensitive   = true
}

variable "db_host" {
  description = "host database"
  type        = string
}

variable "db_port" {
  description = "puerto database"
  type        = number
}

variable "db_name" {
  description = "nombre database"
  type        = string
}