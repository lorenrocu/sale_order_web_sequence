# Secuencia Web para Cotizaciones

## Descripción
Este módulo permite usar una secuencia personalizada para las órdenes de venta creadas desde el sitio web, diferenciándolas de las órdenes creadas desde el backend.

## Características
- Secuencia personalizada con prefijo "WEB" para órdenes web
- Compatible con pasarelas de pago
- Manejo robusto de errores
- Logging detallado para debugging

## Problema Solucionado
El módulo original causaba conflictos con las pasarelas de pago porque:
1. La secuencia `sale.order.web` no estaba definida
2. No se excluían las transacciones de pago del procesamiento
3. Faltaba manejo de errores

## Solución Implementada
1. **Secuencia inteligente**: El módulo verifica si ya existe una secuencia personalizada `sale.order.web`:
   - Si existe: Respeta la configuración personalizada del usuario
   - Si no existe: Crea una secuencia por defecto con prefijo "WEB"
2. **Exclusión de pagos**: Se agregaron validaciones para evitar interferir con transacciones de pago:
   - `not vals.get('transaction_ids')`: Excluye órdenes con transacciones
   - `not self.env.context.get('payment_processing')`: Excluye procesos de pago
3. **Manejo de errores**: Try-catch para evitar fallos del módulo
4. **Logging**: Registro detallado para monitoreo
5. **Compatibilidad**: Preserva cualquier secuencia personalizada existente

## Instalación
1. Reiniciar el servidor Odoo
2. Actualizar la lista de aplicaciones
3. Instalar/actualizar el módulo

## Configuración
La secuencia se crea automáticamente con:
- **Código**: `sale.order.web`
- **Prefijo**: `WEB`
- **Padding**: 5 dígitos
- **Formato**: WEB00001, WEB00002, etc.

## Compatibilidad
- Odoo 13.0
- Módulos requeridos: `sale`, `website_sale`
- Compatible con todas las pasarelas de pago estándar

## Autor
Lorenzo Romero