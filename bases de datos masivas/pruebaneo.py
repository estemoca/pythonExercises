from neo4j import GraphDatabase

# ── Conexión ──────────────────────────────────────────────
URI  = "bolt://localhost:7687"
AUTH = ("neo4j", "password123")
driver = GraphDatabase.driver(URI, auth=AUTH)

# ── Crear persona ─────────────────────────────────────────
def crear_persona(nombre, ciudad, edad):
    with driver.session() as s:
        s.run(
            "MERGE (p:Persona {nombre:$n}) SET p.ciudad=$c, p.edad=$e",
            n=nombre, c=ciudad, e=edad
        )
    print(f"  ✅ Persona '{nombre}' creada")

# ── Crear amistad ─────────────────────────────────────────
def crear_amistad(n1, n2, desde):
    with driver.session() as s:
        s.run("""
          MATCH (a:Persona {nombre:$a}), (b:Persona {nombre:$b})
          MERGE (a)-[:CONOCE {desde:$d}]->(b)
        """, a=n1, b=n2, d=desde)
    print(f"  🤝 {n1} → CONOCE → {n2}")

# ── Sugerencias de amigos ─────────────────────────────────
def sugerencias(nombre):
    with driver.session() as s:
        r = s.run("""
          MATCH (p:Persona {nombre:$n})-[:CONOCE*2]->(sug)
          WHERE NOT (p)-[:CONOCE]->(sug) AND sug <> p
          RETURN DISTINCT sug.nombre AS nombre
        """, n=nombre)
        return [row["nombre"] for row in r]

# ── Camino más corto ──────────────────────────────────────
def camino_corto(origen, destino):
    with driver.session() as s:
        r = s.run("""
          MATCH path = shortestPath(
            (a:Persona {nombre:$a})-[:CONOCE*]->(b:Persona {nombre:$b})
          )
          RETURN length(path) AS grados,
                 [n IN nodes(path) | n.nombre] AS ruta
        """, a=origen, b=destino)
        row = r.single()
        return (row["grados"], row["ruta"]) if row else (None, [])

# ── Main demo ─────────────────────────────────────────────
print("\n🔵 Creando red social...")
crear_persona("Ana",   "Bogotá",    30)
crear_persona("Luis",  "Medellín",  25)
crear_persona("Carla", "Cali",       28)
crear_persona("Sofía", "Cartagena", 35)

crear_amistad("Ana",   "Luis",  2020)
crear_amistad("Luis",  "Carla", 2021)
crear_amistad("Carla", "Sofía", 2022)

sug = sugerencias("Ana")
print(f"\n💡 Ana debería conocer: {sug}")

grados, ruta = camino_corto("Ana", "Sofía")
print(f"📏 Ana → Sofía: {grados} grados de separación")
print(f"   Ruta: {' → '.join(ruta)}")

driver.close()