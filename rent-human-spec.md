# SPECIFICACIÓN TÉCNICA - PLATAFORMA RENT-HUMAN

## 1. ARQUITECTURA RECOMENDADA

### Stack Tecnológico Principal

| Capa | Tecnología | Justificación |
|------|-------------|---------------|
| **Frontend** | Next.js 14 (App Router) + React | SEO crítico para listados, SSR, comunidad activa |
| **Estilos** | Tailwind CSS | Desarrollo rápido, consistente |
| **Estado/Data** | TanStack Query (React Query) | Cacheo eficiente, actualizaciones en tiempo real |
| **Backend** | Node.js + NestJS | Estructura robusta, TypeScript nativo, modular |
| **API** | REST + WebSocket | REST para operaciones CRUD, WS para notificaciones |
| **Base de datos** | PostgreSQL + Prisma | Relacionable, migraciones seguras |
| **Cache/Sesiones** | Redis | Sesiones, cacheo, colas de tareas |
| **Autenticación** | NextAuth.js + JWT | Flexible, múltiples proveedores |
| **Maps** | Mapbox (más económico) | Alternativa a Google Maps |
| **Pagos** | Stripe + Crypto (WalletConnect) | Pagos tradicionales y crypto |
| **Colas** | BullMQ + Redis | Procesamiento de tareas async |
| **Infraestructura** | Vercel (frontend) + Railway/Render (backend) | Escalable, CI/CD incluido |

### Estructura del Proyecto

```
rent-human/
├── apps/
│   ├── web/                    # Frontend Next.js
│   │   ├── src/
│   │   │   ├── app/           # App Router
│   │   │   ├── components/    # Componentes reutilizables
│   │   │   ├── hooks/         # Custom hooks
│   │   │   ├── lib/           # Utilidades
│   │   │   └── store/         # Estado global
│   │   └── public/            # Assets estáticos
│   │
│   └── api/                   # Backend NestJS
│       ├── src/
│       │   ├── modules/
│       │   │   ├── auth/      # Autenticación
│       │   │   ├── users/     # Gestión usuarios humanos
│       │   │   ├── agents/    # Gestión agentes AI
│       │   │   ├── tasks/     # Publicación/búsqueda tareas
│       │   │   ├── matching/  # Algoritmo de emparejamiento
│       │   │   ├── payments/  # Pagos
│       │   │   ├── chat/      # Messaging
│       │   │   ├── reviews/   # Reseñas/ratings
│       │   │   └── mcp/       # Integración MCP
│       │   ├── common/       # Guards, decorators, filters
│       │   ├── config/        # Configuración
│       │   └── database/      # Prisma client, migrations
│       └── test/
│
├── packages/
│   ├── shared/                # Tipos, interfaces compartidas
│   └── utils/                # Funciones utilitarias
│
└── docker-compose.yml         # Desarrollo local
```

---

## 2. REQUERIMIENTOS FUNCIONALES

### MÓDULO 1: AUTENTICACIÓN Y USUARIOS

| # | Requerimiento | Prioridad | Complejidad | Descripción |
|---|---------------|----------|-------------|-------------|
| 1.1 | Registro con email/contraseña | 🔴 Alta | Media | Registro básico con validación de email |
| 1.2 | Login social (Google, GitHub) | 🔴 Alta | Baja | OAuth mediante NextAuth |
| 1.3 | Autenticación de agentes AI | 🔴 Alta | Alta | API keys + JWT para bots |
| 1.4 | Verificación de identidad (KYC) | 🟡 Media | Alta | Integración con servicio de verificación |
| 1.5 | Recuperación de contraseña | 🔴 Alta | Media | Email de reset con token |
| 1.6 | 2FA (Two-Factor Authentication) | 🟡 Media | Media | TOTP para mayor seguridad |
| 1.7 | Perfil de usuario humano | 🔴 Alta | Media | Datos personales, ubicación, habilidades, tarifa/hora |
| 1.8 | Perfil de agente AI | 🔴 Alta | Alta | Nombre, descripción, capacidades, wallet crypto |
| 1.9 | Editar perfil | 🔴 Alta | Baja | Actualizar información personal |
| 1.10 | Eliminar cuenta | 🟡 Media | Baja | Soft delete con período de gracia |

### MÓDULO 2: GESTIÓN DE TAREA (CORE)

| # | Requerimiento | Prioridad | Complejidad | Descripción |
|---|---------------|----------|-------------|-------------|
| 2.1 | Crear tarea (humano contrata) | 🔴 Alta | Media | Formulario: título, descripción, ubicación, precio, deadline |
| 2.2 | Crear tarea (agente AI) | 🔴 Alta | Alta | API endpoint para que bots publiquen tareas |
| 2.3 | Listar tareas disponibles | 🔴 Alta | Baja | Filtrar por ubicación, categoría, precio |
| 2.4 | Búsqueda avanzada | 🔴 Alta | Alta | Filtros: distancia, precio, rating, disponibilidad |
| 2.5 | Ver detalle de tarea | 🔴 Alta | Baja | Página con información completa |
| 2.6 | Editar tarea | 🟡 Media | Baja | Modificar antes de que sea aceptada |
| 2.7 | Cancelar tarea | 🟡 Media | Baja | Cancelar con condiciones |
| 2.8 | Categorías de tareas | 🔴 Alta | Baja | Delivery, verificación, fotografía, etc. |
| 2.9 | Tags/búsqueda por palabras | 🟡 Media | Baja | Sistema de tags para tareas |

### MÓDULO 3: SISTEMA DE MATCHING

| # | Requerimiento | Prioridad | Complejidad | Descripción |
|---|---------------|----------|-------------|-------------|
| 3.1 | Match automático por ubicación | 🔴 Alta | Alta | Algoritmo que sugiere candidatos cercanos |
| 3.2 | Match por habilidades | 🔴 Alta | Alta | Verificar skills requeridos vs perfil |
| 3.3 | Aceptar/rechazar tarea | 🔴 Alta | Baja | Usuario humano acepta propuesta |
| 3.4 | Propuestas múltiples | 🟡 Media | Media | Multiples humanos pueden proponer |
| 3.5 | Historial de matches | 🟡 Media | Baja | Registro de tareas aceptadas |
| 3.6 | Notificaciones de nuevos matches | 🔴 Alta | Baja | Alertas en tiempo real |

### MÓDULO 4: EJECUCIÓN DE TAREAS

| # | Requerimiento | Prioridad | Complejidad | Descripción |
|---|---------------|----------|-------------|-------------|
| 4.1 | Iniciar tarea | 🔴 Alta | Baja | Confirmar inicio (hora inicio automática) |
| 4.2 | Subir evidencia (fotos/videos) | 🔴 Alta | Media | Proof of work con multimedia |
| 4.3 | Chat en tarea | 🔴 Alta | Media | Comunicación entre partes durante ejecución |
| 4.4 | Geolocalización en tiempo real | 🟡 Media | Alta | Tracking de ubicación durante tarea |
| 4.5 | Completar tarea | 🔴 Alta | Baja | Marcar como finalizada |
| 4.6 | Confirmar completado (cliente) | 🔴 Alta | Baja | Ambas partes confirman |
| 4.7 | Disputas | 🟡 Media | Alta | Sistema de resolución de conflictos |
| 4.8 | Extender deadline | 🟡 Media | Baja | Solicitar más tiempo |

### MÓDULO 5: PAGOS

| # | Requerimiento | Prioridad | Complejidad | Descripción |
|---|---------------|----------|-------------|-------------|
| 5.1 | Wallet crypto del agente | 🔴 Alta | Alta | Wallet integrado para pagos en crypto |
| 5.2 | Depósito/retiro fiat | 🟡 Media | Alta | Stripe Connect para humanos |
| 5.3 | Escrow de fondos | 🔴 Alta | Alta | Fondos retenidos hasta completar |
| 5.4 | Comisiones por transacción | 🔴 Alta | Media | % de comisión por tarea |
| 5.5 | Historial de transacciones | 🔴 Alta | Baja | Registro completo de pagos |
| 5.6 | Webhooks para pagos | 🔴 Alta | Media | Notificaciones de estado de pago |
| 5.7 | Reembolsos | 🟡 Media | Alta | Política de reembolsos |
| 5.8 | Pagos automáticos a completarse | 🔴 Alta | Alta | Release de funds automatic |

### MÓDULO 6: INTEGRACIÓN MCP (AGENTES AI)

| # | Requerimiento | Prioridad | Complejidad | Descripción |
|---|---------------|----------|-------------|-------------|
| 6.1 | Servidor MCP | 🔴 Alta | Alta | Implementar protocolo Model Context |
| 6.2 | Herramientas MCP para agentes | 🔴 Alta | Alta | search_tasks, create_task, hire_human, etc. |
| 6.3 | API de herramientas | 🔴 Alta | Alta | Endpoints para que LLMs interactúen |
| 6.4 | Autenticación de agentes | 🔴 Alta | Alta | API key + signature verification |
| 6.5 | Rate limiting | 🟡 Media | Media | Limitar requests por agente |
| 6.6 | Webhooks de callbacks | 🟡 Media | Media | Notificaciones al agente sobre estado |
| 6.7 | Documentación de integración | 🔴 Alta | Media | Guía para desarrolladores de agentes |

### MÓDULO 7: SISTEMA DE RESEÑAS

| # | Requerimiento | Prioridad | Complejidad | Descripción |
|---|---------------|----------|-------------|-------------|
| 7.1 | Calificar después de tarea | 🔴 Alta | Baja | Rating 1-5 estrellas |
| 7.2 | Escribir reseña | 🟡 Media | Baja | Comentario textual |
| 7.3 | Ver perfil de reviews | 🔴 Alta | Baja | Historial de reseñas recibidas |
| 7.4 | Responder a reseñas | 🟡 Media | Baja | Derecho de respuesta |
| 7.5 | Reportar reseñas inapropiadas | 🟡 Media | Baja | Sistema de moderación |
| 7.6 | Cálculo de rating promedio | 🔴 Alta | Baja | Promedio ponderado de ratings |

### MÓDULO 8: NOTIFICACIONES

| # | Requerimiento | Prioridad | Complejidad | Descripción |
|---|---------------|----------|-------------|-------------|
| 8.1 | Notificaciones push (web) | 🔴 Alta | Alta | Service workers para web push |
| 8.2 | Notificaciones email | 🔴 Alta | Media | Transaccionales (SendGrid/Resend) |
| 8.3 | Notificaciones in-app | 🔴 Alta | Media | Centro de notificaciones |
| 8.4 | Notificaciones SMS | 🟡 Media | Alta | Twilio para alertas críticas |
| 8.5 | Preferencias de notificaciones | 🟡 Media | Baja | Configuración por usuario |

### MÓDULO 9: ADMINISTRACIÓN

| # | Requerimiento | Prioridad | Complejidad | Descripción |
|---|---------------|----------|-------------|-------------|
| 9.1 | Dashboard admin | 🔴 Alta | Alta | Panel de control con métricas |
| 9.2 | Gestionar usuarios | 🔴 Alta | Media | Ban, suspend, eliminar |
| 9.3 | Gestionar tareas | 🔴 Alta | Media | Modificar, cancelar, ocultar |
| 9.4 | Reportes de disputas | 🔴 Alta | Media | Revisión de conflictos |
| 9.5 | Analytics de uso | 🟡 Media | Alta | Métricas de plataforma |
| 9.6 | Configuración de comisiones | 🟡 Media | Baja | Ajustar % de comisión |
| 9.7 | Moderación de contenido | 🟡 Media | Alta | Revisión de imágenes, textos |

### MÓDULO 10: GEOLOCALIZACIÓN

| # | Requerimiento | Prioridad | Complejidad | Descripción |
|---|---------------|----------|-------------|-------------|
| 10.1 | Mapa de tareas cercanas | 🔴 Alta | Alta | Visualización en mapa de tareas disponibles |
| 10.2 | Búsqueda por radio | 🔴 Alta | Alta | Filtrar tareas en radio X km |
| 10.3 | Geocoding de direcciones | 🔴 Alta | Media | Convertir direcciones a coords |
| 10.4 | Zonas de servicio | 🟡 Media | Alta | Definir áreas de cobertura |

---

## 3. PRIORIDADES DE IMPLEMENTACIÓN (FASES)

### Fase 1: MVP (Mes 1-2)
- Autenticación básica (email + social)
- Perfiles de usuario
- Crear/listar tareas (básico)
- Aceptar tarea
- Completar tarea con evidencia
- Pagos básicos (stripe)

### Fase 2: CORE (Mes 2-3)
- Integración MCP
- Sistema de matching
- Chat en tarea
- Notificaciones
- Reviews

### Fase 3: ESCALABLE (Mes 3-4)
- Pagos crypto
- Geolocalización avanzada
- Disputas
- Dashboard admin

### Fase 4: ADICIONALES (Mes 4+)
- SMS
- 2FA
- Analytics avanzados
- Moderación IA

---

## 4. ESTIMACIÓN DE COSTOS (MVP)

| Servicio | Costo mensual aproximado |
|----------|--------------------------|
| Vercel Pro (frontend) | $20 |
| Railway Pro (backend) | $20 |
| PostgreSQL (Railway) | $20 |
| Redis (Railway) | $10 |
| Mapbox | $0-50 |
| SendGrid/Resend | $0-30 |
| Stripe | 2.9% + $0.30 por transacción |
| Dominio + SSL | $15 |
| **Total mensual** | **~$100-150** |

---

## 5. PRÓXIMOS PASOS

1. **Validar requerimientos**: Revisar lista y marcar los que necesitas
2. **Decidir fases**: Seleccionar qué implementar en MVP
3. **Diseñar BD**: Crear esquema de entidades
4. **Iniciar desarrollo**: Configurar repo y estructura base