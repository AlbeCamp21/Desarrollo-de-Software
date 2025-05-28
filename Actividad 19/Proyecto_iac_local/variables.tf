variable "nombre_entorno" {
  description = "Nombre base para el entorno generado."
  type        = string
  default     = "desarrollo"
}

variable "numero_instancias_app_simulada" {
  description = "Cuántas instancias de la app simulada crear."
  type        = number
  default     = 2
}

variable "mensaje_global" {
  description = "Un mensaje para incluir en varios archivos."
  type        = string
  default     = "Configuración gestionada por Terraform."
  sensitive   = true # Para demostrar
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
